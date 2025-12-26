#!/usr/bin/env python3
"""
Test a single VM file with both current and legacy VM translators
"""

import os
import sys
import tempfile
import shutil
import argparse

# Add current directory to path
sys.path.append('.')

from VirtualMachine import VMTranslator as LegacyVMTranslator
from Petri.VMToPetri import VMToPetriTranslator as CurrentVMTranslator
from vm_parser import parse_vm_file

def test_vm_file(vm_file_path, show_assembly=False):
    """Test a single VM file with both translators"""
    
    if not os.path.exists(vm_file_path):
        print(f"Error: VM file {vm_file_path} not found")
        return False
    
    print(f"Testing VM file: {vm_file_path}")
    print("=" * 60)
    
    # Parse VM file for Petri net translator
    commands = parse_vm_file(vm_file_path)
    print(f"Parsed {len(commands)} VM commands")
    
    results = {}
    
    # Test with current Petri net VM translator
    print("\n--- Testing with Current Petri Net VM Translator ---")
    try:
        current_translator = CurrentVMTranslator()
        
        # Execute the program to build the Petri net
        result = current_translator.execute_program(commands)
        print(f"Petri net execution result: {result}")
        
        # Generate assembly code (single core)
        execution_plan = current_translator._analyze_execution_dependencies()
        core_assignments = current_translator._assign_operations_to_cores(execution_plan, 1)
        memory_map = current_translator._optimize_memory_allocation()
        
        current_assembly = current_translator._generate_core_rom(0, core_assignments[0], memory_map, 1)
        current_asm_text = '\n'.join(current_assembly)
        
        results['current'] = {
            'success': True,
            'assembly': current_asm_text,
            'line_count': len(current_assembly),
            'instruction_count': len([line for line in current_assembly 
                                    if line.strip() and not line.strip().startswith('//') 
                                    and not (line.strip().startswith('(') and line.strip().endswith(')'))])
        }
        
        print(f"✅ Success! Generated {results['current']['line_count']} lines of assembly")
        print(f"   Instructions: {results['current']['instruction_count']}")
        print(f"   Petri net: {len(current_translator.net.places)} places, {len(current_translator.net.transitions)} transitions")
        
    except Exception as e:
        results['current'] = {'success': False, 'error': str(e)}
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    # Test with legacy stack-based VM translator
    print("\n--- Testing with Legacy Stack-Based VM Translator ---")
    
    # Create temporary directory for legacy translator
    with tempfile.TemporaryDirectory() as temp_dir:
        # Copy VM file to temp directory
        vm_filename = os.path.basename(vm_file_path)
        temp_vm_dir = os.path.join(temp_dir, 'vm_files')
        os.makedirs(temp_vm_dir)
        shutil.copy2(vm_file_path, temp_vm_dir)
        
        try:
            legacy_translator = LegacyVMTranslator(
                programdir=temp_vm_dir,
                overwrite=True,
                debug=True
            )
            
            # Find generated assembly file
            asm_files = [f for f in os.listdir(temp_vm_dir) if f.endswith('.asm')]
            if asm_files:
                legacy_asm_path = os.path.join(temp_vm_dir, asm_files[0])
                with open(legacy_asm_path, 'r') as f:
                    legacy_asm = f.read()
                
                results['legacy'] = {
                    'success': True,
                    'assembly': legacy_asm,
                    'line_count': len(legacy_asm.split('\n')),
                    'instruction_count': len([line for line in legacy_asm.split('\n') 
                                            if line.strip() and not line.strip().startswith('//') 
                                            and not (line.strip().startswith('(') and line.strip().endswith(')'))])
                }
                
                print(f"✅ Success! Generated {results['legacy']['line_count']} lines of assembly")
                print(f"   Instructions: {results['legacy']['instruction_count']}")
            else:
                # Check if assembly was generated in parent directory
                parent_dir = os.path.dirname(temp_vm_dir)
                asm_files = [f for f in os.listdir(parent_dir) if f.endswith('.asm')]
                if asm_files:
                    legacy_asm_path = os.path.join(parent_dir, asm_files[0])
                    with open(legacy_asm_path, 'r') as f:
                        legacy_asm = f.read()
                    
                    results['legacy'] = {
                        'success': True,
                        'assembly': legacy_asm,
                        'line_count': len(legacy_asm.split('\n')),
                        'instruction_count': len([line for line in legacy_asm.split('\n') 
                                                if line.strip() and not line.strip().startswith('//') 
                                                and not (line.strip().startswith('(') and line.strip().endswith(')'))])
                    }
                    
                    print(f"✅ Success! Generated {results['legacy']['line_count']} lines of assembly")
                    print(f"   Instructions: {results['legacy']['instruction_count']}")
                else:
                    results['legacy'] = {'success': False, 'error': 'No assembly file generated'}
                    print("❌ No assembly file generated")
                        
        except Exception as e:
            results['legacy'] = {'success': False, 'error': str(e)}
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
    
    # Compare results
    print("\n--- Comparison ---")
    if results.get('current', {}).get('success') and results.get('legacy', {}).get('success'):
        current = results['current']
        legacy = results['legacy']
        
        print(f"Line count difference: {current['line_count'] - legacy['line_count']:+d}")
        print(f"Instruction count difference: {current['instruction_count'] - legacy['instruction_count']:+d}")
        
        # Check if assembly is identical
        if current['assembly'] == legacy['assembly']:
            print("✅ Generated assembly is IDENTICAL")
        else:
            print("⚠️  Generated assembly is DIFFERENT")
            
            if show_assembly:
                print("\n--- Petri Net VM Assembly ---")
                print(current['assembly'][:1000] + ("..." if len(current['assembly']) > 1000 else ""))
                print("\n--- Legacy Stack VM Assembly ---")
                print(legacy['assembly'][:1000] + ("..." if len(legacy['assembly']) > 1000 else ""))
    
    elif results.get('current', {}).get('success'):
        print("✅ Only Petri net VM translator succeeded")
    elif results.get('legacy', {}).get('success'):
        print("✅ Only legacy stack-based VM translator succeeded")
    else:
        print("❌ Both translators failed")
    
    return results

def main():
    parser = argparse.ArgumentParser(description='Test a single VM file with both translators')
    parser.add_argument('vm_file', help='Path to the .vm file to test')
    parser.add_argument('--show-assembly', action='store_true', help='Show generated assembly code')
    
    args = parser.parse_args()
    
    test_vm_file(args.vm_file, args.show_assembly)

if __name__ == "__main__":
    main()