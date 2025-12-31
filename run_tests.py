#!/usr/bin/env python3
"""
Legacy Test Runner - Redirects to Organized Test Suite
For backward compatibility, this runner now delegates to the organized test suite
"""

import sys
import subprocess

def main():
    """Run the organized test suite"""
    print("🔄 Redirecting to organized test suite...")
    print("   Use 'python tests/test_suite_runner.py' for the new organized runner")
    print("="*80)
    
    # Run the organized test suite
    result = subprocess.run([sys.executable, "tests/test_suite_runner.py"])
    return result.returncode == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)