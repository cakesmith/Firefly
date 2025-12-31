#!/usr/bin/env python3
"""
Organized Test Suite Runner for Petri Net VM Compiler
Groups tests by category and provides detailed reporting
"""

import os
import sys
import subprocess
import traceback
from pathlib import Path

class TestCategory:
    def __init__(self, name, description, test_files):
        self.name = name
        self.description = description
        self.test_files = test_files
        self.results = {}

def get_test_categories():
    """Define test categories and their associated files"""
    return [
        TestCategory(
            "Core Operations",
            "Basic Petri net operations and stack management",
            [
                "test_insert_operation.py",
                "test_dup_branching.py"
            ]
        ),
        TestCategory(
            "VM Operations", 
            "Virtual machine instruction parsing and compilation",
            [
                "test_push_constant.py"
            ]
        ),
        TestCategory(
            "Memory Management",
            "Memory allocation and optimization algorithms", 
            [
                "test_memory_allocator.py",
                "test_interference_analysis.py",  # renamed from debug_interference.py
                "test_allocation_debugging.py"   # renamed from debug_memory_allocation.py
            ]
        ),
        TestCategory(
            "Large Scale Testing",
            "Performance and scalability with large networks",
            [
                "test_large_network_optimization.py"
            ]
        ),
        TestCategory(
            "Edge Cases",
            "Pathological cases and stress testing",
            [
                "test_pathological_cases.py"
            ]
        )
    ]

def run_test_file(test_file_path):
    """Run a single test file and return success status"""
    try:
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        
        result = subprocess.run([
            sys.executable, str(test_file_path)
        ], capture_output=True, text=True, cwd=os.getcwd(), env=env, encoding='utf-8')
        
        return result.returncode == 0, result.stdout, result.stderr
        
    except Exception as e:
        return False, "", str(e)

def run_category_tests(category):
    """Run all tests in a category"""
    print(f"\n{'='*80}")
    print(f"🧪 {category.name.upper()}: {category.description}")
    print(f"{'='*80}")
    
    category_success = True
    
    for test_file in category.test_files:
        test_path = Path("tests") / test_file
        
        if not test_path.exists():
            print(f"⚠️  SKIPPED: {test_file} (file not found)")
            category.results[test_file] = "SKIPPED"
            continue
            
        print(f"\n🔹 Running {test_file}...")
        success, stdout, stderr = run_test_file(test_path)
        
        if success:
            print(f"✅ {test_file} PASSED")
            category.results[test_file] = "PASSED"
        else:
            print(f"❌ {test_file} FAILED")
            if stdout:
                print("STDOUT:", stdout[-500:])  # Last 500 chars
            if stderr:
                print("STDERR:", stderr[-500:])
            category.results[test_file] = "FAILED"
            category_success = False
    
    return category_success

def print_summary(categories):
    """Print comprehensive test summary"""
    print(f"\n{'='*80}")
    print("📊 TEST SUITE SUMMARY")
    print(f"{'='*80}")
    
    total_tests = 0
    total_passed = 0
    total_failed = 0
    total_skipped = 0
    
    for category in categories:
        print(f"\n🏷️  {category.name}:")
        
        category_passed = sum(1 for result in category.results.values() if result == "PASSED")
        category_failed = sum(1 for result in category.results.values() if result == "FAILED") 
        category_skipped = sum(1 for result in category.results.values() if result == "SKIPPED")
        category_total = len(category.results)
        
        print(f"   Tests: {category_total}, Passed: {category_passed}, Failed: {category_failed}, Skipped: {category_skipped}")
        
        for test_file, result in category.results.items():
            status_icon = {"PASSED": "✅", "FAILED": "❌", "SKIPPED": "⚠️"}[result]
            print(f"   {status_icon} {test_file}")
        
        total_tests += category_total
        total_passed += category_passed
        total_failed += category_failed
        total_skipped += category_skipped
    
    print(f"\n{'='*80}")
    print(f"OVERALL RESULTS:")
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_failed}")
    print(f"Skipped: {total_skipped}")
    
    if total_failed == 0:
        print(f"\n🎉 ALL TESTS PASSED! 🎉")
        return True
    else:
        print(f"\n💥 {total_failed} TEST(S) FAILED!")
        return False

def main():
    """Main test runner"""
    print("🚀 PETRI NET VM COMPILER - ORGANIZED TEST SUITE")
    print("="*80)
    
    categories = get_test_categories()
    overall_success = True
    
    for category in categories:
        category_success = run_category_tests(category)
        if not category_success:
            overall_success = False
    
    success = print_summary(categories)
    
    if success:
        print("\n🏆 Test suite completed successfully!")
    else:
        print("\n🔥 Test suite has failures that need attention.")
    
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)