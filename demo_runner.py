#!/usr/bin/env python3
"""
PETRI NET VM COMPILER - DEMO RUNNER
===================================
Runs all demonstration scripts in the demos/ folder.
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def run_demo(demo_path):
    """Run a single demo and return success status."""
    try:
        result = subprocess.run(
            [sys.executable, str(demo_path)],
            capture_output=True,
            text=True,
            timeout=120,
            cwd=os.path.dirname(os.path.abspath(__file__)),
            encoding='utf-8',
            errors='replace'
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "TIMEOUT: Demo took longer than 120 seconds"
    except Exception as e:
        return False, "", str(e)

def main():
    print("=" * 72)
    print("  PETRI NET VM COMPILER - DEMO RUNNER")
    print("=" * 72)
    
    # Find all demo files
    demos_dir = Path(__file__).parent / "demos"
    
    if not demos_dir.exists():
        print(f"\n[ERROR] demos/ directory not found")
        return 1
    
    demo_files = sorted(demos_dir.glob("demo_*.py"))
    
    if not demo_files:
        print(f"\n[ERROR] No demo files found in demos/")
        return 1
    
    print(f"\n[INFO] Found {len(demo_files)} demo files")
    print("=" * 72)
    
    results = []
    total_time = 0
    
    for demo_path in demo_files:
        demo_name = demo_path.name
        print(f"\n[RUN] {demo_name}")
        print("-" * 72)
        
        start_time = time.time()
        success, stdout, stderr = run_demo(demo_path)
        elapsed = time.time() - start_time
        total_time += elapsed
        
        if success:
            print(stdout)
            print(f"\n[PASS] {demo_name} ({elapsed:.1f}s)")
            results.append((demo_name, True, elapsed))
        else:
            print(f"STDOUT:\n{stdout[:500]}..." if len(stdout) > 500 else f"STDOUT:\n{stdout}")
            print(f"\nSTDERR:\n{stderr[:500]}..." if len(stderr) > 500 else f"\nSTDERR:\n{stderr}")
            print(f"\n[FAIL] {demo_name} ({elapsed:.1f}s)")
            results.append((demo_name, False, elapsed))
    
    # Summary
    print("\n" + "=" * 72)
    print("  DEMO RESULTS SUMMARY")
    print("=" * 72)
    
    passed = sum(1 for _, success, _ in results if success)
    failed = sum(1 for _, success, _ in results if not success)
    
    print(f"\n{'Demo':<45} {'Status':<10} {'Time':<10}")
    print("-" * 65)
    
    for demo_name, success, elapsed in results:
        status = "[PASS]" if success else "[FAIL]"
        print(f"{demo_name:<45} {status:<10} {elapsed:.1f}s")
    
    print("-" * 65)
    print(f"{'Total':<45} {'':<10} {total_time:.1f}s")
    
    print(f"\n  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(results)}")
    
    if failed == 0:
        print("\n[SUCCESS] ALL DEMOS PASSED!")
        return 0
    else:
        print(f"\n[ERROR] {failed} DEMO(S) FAILED!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
