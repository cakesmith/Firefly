#!/usr/bin/env python3
"""
Test Runner for Petri Net Memory Allocator
Discovers and runs all test files in the tests/ directory
"""

import os
import sys
import subprocess
import importlib.util
import traceback
from pathlib import Path

def discover_test_files(test_dir="tests"):
    """Discover all Python test files in the test directory"""
    test_files = []
    test_path = Path(test_dir)
    
    if not test_path.exists():
        print(f"❌ Test directory '{test_dir}' not found!")
        return test_files
    
    for file_path in test_path.glob("*.py"):
        if file_path.name.startswith(("test_", "debug_")):
            test_files.append(file_path)
    
    return sorted(test_files)

def load_and_run_test(test_file_path):
    """Load a test file and run its main function"""
    test_name = test_file_path.stem
    
    try:
        print(f"\n{'='*80}")
        print(f"🧪 RUNNING: {test_name}")
        print(f"{'='*80}")
        
        # Execute the test file directly as a script
        # This ensures the if __name__ == "__main__": block runs
        import subprocess
        import sys
        
        # Set environment to handle Unicode properly on Windows
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        
        result = subprocess.run([
            sys.executable, str(test_file_path)
        ], capture_output=True, text=True, cwd=os.getcwd(), env=env, encoding='utf-8')
        
        # Print the output
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        if result.returncode == 0:
            print(f"\n✅ {test_name} completed successfully")
            return True
        else:
            print(f"\n❌ {test_name} failed with return code {result.returncode}")
            return False
            
    except Exception as e:
        print(f"\n❌ {test_name} failed with error:")
        print(f"   {str(e)}")
        print(f"\nFull traceback:")
        traceback.print_exc()
        return False

def run_all_tests():
    """Discover and run all tests"""
    print("🚀 PETRI NET MEMORY ALLOCATOR TEST SUITE")
    print("="*80)
    
    # Discover test files
    test_files = discover_test_files()
    
    if not test_files:
        print("❌ No test files found in tests/ directory!")
        return False
    
    print(f"📋 Discovered {len(test_files)} test files:")
    for test_file in test_files:
        print(f"   • {test_file.name}")
    
    # Run each test
    results = {}
    for test_file in test_files:
        success = load_and_run_test(test_file)
        results[test_file.name] = success
    
    # Summary
    print(f"\n{'='*80}")
    print("📊 TEST SUITE SUMMARY")
    print(f"{'='*80}")
    
    passed = sum(1 for success in results.values() if success)
    total = len(results)
    
    print(f"Tests run: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    
    if passed == total:
        print(f"\n🎉 ALL TESTS PASSED! 🎉")
        print(f"Memory allocator is working correctly across all test scenarios.")
    else:
        print(f"\n💥 {total - passed} TEST(S) FAILED!")
        print(f"Failed tests:")
        for test_name, success in results.items():
            if not success:
                print(f"   ❌ {test_name}")
    
    print(f"\n{'='*80}")
    return passed == total

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)