#!/usr/bin/env python3
"""
Simple Test Runner for Petri Net VM Compiler
Automatically discovers and runs all test files in the tests/ folder
"""

import os
import sys
import subprocess
import glob
from pathlib import Path

def find_test_files():
    """Find all Python test files in the tests directory"""
    test_files = []
    tests_dir = Path("tests")
    
    if not tests_dir.exists():
        print("[ERROR] tests/ directory not found")
        return []
    
    # Find all .py files that start with 'test_'
    for test_file in tests_dir.glob("test_*.py"):
        test_files.append(test_file)
    
    return sorted(test_files)

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

def main():
    """Main test runner"""
    # Fix encoding for Windows console
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    
    print("[START] PETRI NET VM COMPILER - TEST RUNNER")
    print("="*60)
    
    test_files = find_test_files()
    
    if not test_files:
        print("[ERROR] No test files found in tests/ directory")
        return False
    
    print(f"[INFO] Found {len(test_files)} test files")
    print("="*60)
    
    passed = 0
    failed = 0
    
    for test_file in test_files:
        print(f"\n[RUN] {test_file.name}")
        
        success, stdout, stderr = run_test_file(test_file)
        
        if success:
            print(f"[PASS] {test_file.name}")
            passed += 1
        else:
            print(f"[FAIL] {test_file.name}")
            if stdout:
                # Replace unicode characters that can't be encoded
                safe_stdout = stdout[-300:].encode('ascii', errors='replace').decode('ascii')
                print("STDOUT:", safe_stdout)
            if stderr:
                safe_stderr = stderr[-300:].encode('ascii', errors='replace').decode('ascii')
                print("STDERR:", safe_stderr)
            failed += 1
    
    # Summary
    print(f"\n{'='*60}")
    print("[SUMMARY] TEST RESULTS")
    print(f"{'='*60}")
    print(f"Total Tests: {len(test_files)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    
    if failed == 0:
        print("\n[SUCCESS] ALL TESTS PASSED!")
        return True
    else:
        print(f"\n[ERROR] {failed} TEST(S) FAILED!")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)