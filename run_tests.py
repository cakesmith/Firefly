#!/usr/bin/env python3
"""
Comprehensive Test Runner for Petri-Net VM
==========================================

Automatically discovers and runs all tests in the tests/ directory structure.
Tests are organized by category:
- tests/unit/: Unit tests for individual components
- tests/integration/: Integration tests for complete workflows  
- tests/property/: Property-based tests using hypothesis or similar

Usage:
    python run_all_tests.py [--category CATEGORY] [--verbose] [--stop-on-fail]

Categories:
    unit        - Run only unit tests
    integration - Run only integration tests  
    property    - Run only property-based tests
    all         - Run all tests (default)
"""

import os
import sys
import subprocess
import argparse
import time
from pathlib import Path

class TestRunner:
    def __init__(self):
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
        self.test_results = []
        
    def discover_tests(self, category='all'):
        """Discover test files in the specified category"""
        test_files = []
        base_path = Path('tests')
        
        if category == 'all':
            # Search all subdirectories
            for test_dir in ['unit', 'integration', 'property']:
                test_path = base_path / test_dir
                if test_path.exists():
                    test_files.extend(self._find_test_files(test_path, test_dir))
        else:
            # Search specific category
            test_path = base_path / category
            if test_path.exists():
                test_files.extend(self._find_test_files(test_path, category))
            else:
                print(f"Warning: Test category '{category}' not found")
                
        return test_files
    
    def _find_test_files(self, path, category):
        """Find all Python test files in a directory"""
        test_files = []
        for file in path.glob('test_*.py'):
            test_files.append({
                'path': file,
                'category': category,
                'name': file.stem
            })
        return test_files
    
    def run_test(self, test_info, verbose=False, stop_on_fail=False):
        """Run a single test file"""
        test_path = test_info['path']
        test_name = test_info['name']
        category = test_info['category']
        
        print(f"Running {category}/{test_name}...", end=' ')
        
        start_time = time.time()
        
        try:
            # Set up environment to include current directory in Python path
            env = os.environ.copy()
            current_dir = os.getcwd()
            if 'PYTHONPATH' in env:
                env['PYTHONPATH'] = f"{current_dir}{os.pathsep}{env['PYTHONPATH']}"
            else:
                env['PYTHONPATH'] = current_dir
            
            # Set UTF-8 encoding for Windows console
            env['PYTHONIOENCODING'] = 'utf-8'
            env['PYTHONLEGACYWINDOWSSTDIO'] = '0'
            
            # Handle special cases that need arguments
            if test_name == 'test_single_vm':
                # This test needs a VM file argument
                result = subprocess.run([
                    sys.executable, str(test_path), 'test_simple.vm'
                ], capture_output=True, text=True, timeout=30, env=env, 
                encoding='utf-8', errors='replace')
            else:
                result = subprocess.run([
                    sys.executable, str(test_path)
                ], capture_output=True, text=True, timeout=30, env=env,
                encoding='utf-8', errors='replace')
            
            duration = time.time() - start_time
            
            if result.returncode == 0:
                print(f"PASSED ({duration:.2f}s)")
                self.passed_tests += 1
                self.test_results.append({
                    'name': test_name,
                    'category': category,
                    'status': 'PASSED',
                    'duration': duration,
                    'output': result.stdout if verbose else ''
                })
            else:
                print(f"FAILED ({duration:.2f}s)")
                self.failed_tests += 1
                self.test_results.append({
                    'name': test_name,
                    'category': category,
                    'status': 'FAILED',
                    'duration': duration,
                    'output': result.stdout,
                    'error': result.stderr
                })
                
                if verbose or stop_on_fail:
                    print(f"STDOUT:\n{result.stdout}")
                    print(f"STDERR:\n{result.stderr}")
                    
                if stop_on_fail:
                    return False
                    
        except subprocess.TimeoutExpired:
            duration = time.time() - start_time
            print(f"TIMEOUT ({duration:.2f}s)")
            self.failed_tests += 1
            self.test_results.append({
                'name': test_name,
                'category': category,
                'status': 'TIMEOUT',
                'duration': duration,
                'output': '',
                'error': 'Test timed out after 30 seconds'
            })
            
        except Exception as e:
            duration = time.time() - start_time
            print(f"ERROR ({duration:.2f}s): {e}")
            self.failed_tests += 1
            self.test_results.append({
                'name': test_name,
                'category': category,
                'status': 'ERROR',
                'duration': duration,
                'output': '',
                'error': str(e)
            })
            
        self.total_tests += 1
        return True
    
    def print_summary(self):
        """Print test execution summary"""
        print("\n" + "="*60)
        print("TEST EXECUTION SUMMARY")
        print("="*60)
        
        # Overall stats
        print(f"Total tests: {self.total_tests}")
        print(f"Passed: {self.passed_tests}")
        print(f"Failed: {self.failed_tests}")
        
        if self.total_tests > 0:
            success_rate = (self.passed_tests / self.total_tests) * 100
            print(f"Success rate: {success_rate:.1f}%")
        
        # Category breakdown
        categories = {}
        for result in self.test_results:
            cat = result['category']
            if cat not in categories:
                categories[cat] = {'passed': 0, 'failed': 0, 'total': 0}
            categories[cat]['total'] += 1
            if result['status'] == 'PASSED':
                categories[cat]['passed'] += 1
            else:
                categories[cat]['failed'] += 1
        
        if categories:
            print("\nBy Category:")
            for cat, stats in categories.items():
                rate = (stats['passed'] / stats['total']) * 100 if stats['total'] > 0 else 0
                print(f"  {cat}: {stats['passed']}/{stats['total']} ({rate:.1f}%)")
        
        # Failed tests details
        failed_results = [r for r in self.test_results if r['status'] != 'PASSED']
        if failed_results:
            print(f"\nFailed Tests ({len(failed_results)}):")
            for result in failed_results:
                print(f"  [X] {result['category']}/{result['name']} - {result['status']}")
                if result.get('error'):
                    print(f"      Error: {result['error']}")
        
        # Success message
        if self.failed_tests == 0:
            print("\n[SUCCESS] ALL TESTS PASSED!")
        else:
            print(f"\n[WARNING] {self.failed_tests} test(s) failed")
            
        return self.failed_tests == 0

def main():
    parser = argparse.ArgumentParser(
        description='Run Petri-Net VM tests',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        '--category', '-c',
        choices=['unit', 'integration', 'property', 'all'],
        default='all',
        help='Test category to run (default: all)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show detailed output for all tests'
    )
    parser.add_argument(
        '--stop-on-fail', '-s',
        action='store_true',
        help='Stop execution on first test failure'
    )
    
    args = parser.parse_args()
    
    print("Petri-Net VM Test Suite")
    print("="*60)
    print(f"Running {args.category} tests...")
    print()
    
    runner = TestRunner()
    test_files = runner.discover_tests(args.category)
    
    if not test_files:
        print(f"No test files found for category: {args.category}")
        return 1
    
    print(f"Discovered {len(test_files)} test files")
    print()
    
    # Run tests
    for test_info in test_files:
        if not runner.run_test(test_info, args.verbose, args.stop_on_fail):
            break  # Stop on fail was requested and we failed
    
    # Print summary
    success = runner.print_summary()
    
    return 0 if success else 1

if __name__ == '__main__':
    sys.exit(main())