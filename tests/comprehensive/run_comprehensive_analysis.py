#!/usr/bin/env python3
"""
Master Test Runner for Comprehensive VM and Petri Net Analysis
=============================================================

This master test runner orchestrates all comprehensive analysis test suites:
1. VM and Petri Net Analysis Suite
2. Petri Execution Pattern Analysis
3. Assembly Emission Analysis

Provides unified reporting and cross-analysis insights.
"""

import sys
import os
import json
import time
import subprocess
from pathlib import Path

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class ComprehensiveAnalysisMaster:
    """Master controller for all comprehensive analysis suites"""
    
    def __init__(self):
        self.test_results_dir = "test_results/comprehensive_master"
        self.suite_results = {}
        self.start_time = time.time()
        
        # Create master results directory
        if not os.path.exists(self.test_results_dir):
            os.makedirs(self.test_results_dir)
            print(f"Created master analysis directory: {self.test_results_dir}/")
    
    def run_suite(self, suite_name, suite_module, suite_class):
        """Run a comprehensive analysis suite"""
        print(f"\n{'='*80}")
        print(f"RUNNING COMPREHENSIVE SUITE: {suite_name}")
        print('='*80)
        
        start_time = time.time()
        
        try:
            # Import and run the suite
            module = __import__(suite_module, fromlist=[suite_class])
            suite_instance = getattr(module, suite_class)()
            
            success = suite_instance.run_all_tests()
            
            end_time = time.time()
            duration = end_time - start_time
            
            # Collect results
            self.suite_results[suite_name] = {
                'success': success,
                'duration': duration,
                'passed': getattr(suite_instance, 'passed', 0),
                'failed': getattr(suite_instance, 'failed', 0),
                'detailed_results': getattr(suite_instance, 'analysis_results', {}) or 
                                  getattr(suite_instance, 'execution_traces', {}) or
                                  getattr(suite_instance, 'assembly_analyses', {}),
                'timestamp': end_time
            }
            
            print(f"\n{suite_name} completed in {duration:.2f} seconds")
            print(f"Result: {'SUCCESS' if success else 'FAILED'}")
            
            return success
            
        except Exception as e:
            print(f"Error running {suite_name}: {e}")
            import traceback
            traceback.print_exc()
            
            self.suite_results[suite_name] = {
                'success': False,
                'error': str(e),
                'duration': time.time() - start_time,
                'timestamp': time.time()
            }
            
            return False
    
    def run_all_comprehensive_suites(self):
        """Run all comprehensive analysis suites"""
        print("=" * 100)
        print("COMPREHENSIVE VM AND PETRI NET ANALYSIS - MASTER SUITE")
        print("=" * 100)
        print(f"Starting comprehensive analysis at {time.ctime()}")
        
        # Define all suites to run
        suites = [
            ("VM and Petri Net Analysis", "test_vm_petri_analysis_suite", "VMPetriAnalysisSuite"),
            ("Petri Execution Patterns", "test_petri_execution_patterns", "PetriExecutionPatternAnalyzer"),
            ("Assembly Emission Analysis", "test_assembly_emission_analysis", "AssemblyEmissionAnalyzer")
        ]
        
        # Run each suite
        all_success = True
        for suite_name, module_name, class_name in suites:
            success = self.run_suite(suite_name, module_name, class_name)
            all_success = all_success and success
        
        # Generate master analysis report
        self.generate_master_report()
        
        # Print final summary
        self.print_final_summary()
        
        return all_success
    
    def generate_master_report(self):
        """Generate comprehensive master analysis report"""
        print(f"\n{'='*60}")
        print("GENERATING MASTER ANALYSIS REPORT")
        print('='*60)
        
        total_duration = time.time() - self.start_time
        
        # Calculate aggregate statistics
        aggregate_stats = self.calculate_aggregate_statistics()
        
        # Generate cross-suite insights
        cross_suite_insights = self.generate_cross_suite_insights()
        
        # Create master report
        master_report = {
            'analysis_metadata': {
                'start_time': self.start_time,
                'total_duration': total_duration,
                'timestamp': time.time(),
                'suites_run': len(self.suite_results)
            },
            'suite_results': self.suite_results,
            'aggregate_statistics': aggregate_stats,
            'cross_suite_insights': cross_suite_insights,
            'recommendations': self.generate_recommendations(aggregate_stats, cross_suite_insights)
        }
        
        # Save master report
        master_report_file = os.path.join(self.test_results_dir, "master_analysis_report.json")
        try:
            with open(master_report_file, 'w') as f:
                json.dump(master_report, f, indent=2, default=str)
            print(f"Saved master analysis report: {master_report_file}")
        except Exception as e:
            print(f"Error saving master report: {e}")
        
        # Generate human-readable summary
        self.generate_human_readable_summary(master_report)
        
        return master_report
    
    def calculate_aggregate_statistics(self):
        """Calculate aggregate statistics across all suites"""
        total_tests = 0
        total_passed = 0
        total_failed = 0
        successful_suites = 0
        
        suite_durations = []
        
        for suite_name, results in self.suite_results.items():
            if results.get('success', False):
                successful_suites += 1
            
            total_passed += results.get('passed', 0)
            total_failed += results.get('failed', 0)
            total_tests += results.get('passed', 0) + results.get('failed', 0)
            
            suite_durations.append(results.get('duration', 0))
        
        return {
            'total_suites': len(self.suite_results),
            'successful_suites': successful_suites,
            'total_tests': total_tests,
            'total_passed': total_passed,
            'total_failed': total_failed,
            'overall_success_rate': total_passed / total_tests if total_tests > 0 else 0,
            'suite_success_rate': successful_suites / len(self.suite_results) if self.suite_results else 0,
            'total_analysis_time': sum(suite_durations),
            'average_suite_duration': sum(suite_durations) / len(suite_durations) if suite_durations else 0
        }
    
    def generate_cross_suite_insights(self):
        """Generate insights by comparing results across suites"""
        insights = {
            'petri_net_effectiveness': {},
            'assembly_generation_quality': {},
            'execution_pattern_consistency': {},
            'scalability_assessment': {}
        }
        
        # Extract key metrics from each suite
        vm_analysis = self.suite_results.get("VM and Petri Net Analysis", {})
        execution_analysis = self.suite_results.get("Petri Execution Patterns", {})
        assembly_analysis = self.suite_results.get("Assembly Emission Analysis", {})
        
        # Analyze Petri net effectiveness
        if vm_analysis.get('success', False):
            vm_details = vm_analysis.get('detailed_results', {})
            
            # Count successful Petri net translations
            successful_translations = sum(
                1 for result in vm_details.values()
                if 'net_analysis' in result and result['net_analysis'].get('place_count', 0) > 0
            )
            
            insights['petri_net_effectiveness'] = {
                'successful_translations': successful_translations,
                'total_attempts': len(vm_details),
                'translation_success_rate': successful_translations / len(vm_details) if vm_details else 0
            }
        
        # Analyze assembly generation quality
        if assembly_analysis.get('success', False):
            assembly_details = assembly_analysis.get('detailed_results', {})
            
            successful_assemblies = 0
            total_core_configs = 0
            
            for analysis in assembly_details.values():
                assembly_results = analysis.get('assembly_results', {})
                for cores, result in assembly_results.items():
                    total_core_configs += 1
                    if result.get('generation_successful', False):
                        successful_assemblies += 1
            
            insights['assembly_generation_quality'] = {
                'successful_assemblies': successful_assemblies,
                'total_core_configurations': total_core_configs,
                'assembly_success_rate': successful_assemblies / total_core_configs if total_core_configs > 0 else 0
            }
        
        # Analyze execution pattern consistency
        if execution_analysis.get('success', False):
            execution_details = execution_analysis.get('detailed_results', {})
            
            stack_free_verifications = sum(
                1 for trace in execution_details.values()
                if trace.get('stack_free_verification', {}).get('is_stack_free', False)
            )
            
            insights['execution_pattern_consistency'] = {
                'stack_free_verifications': stack_free_verifications,
                'total_pattern_analyses': len(execution_details),
                'stack_free_rate': stack_free_verifications / len(execution_details) if execution_details else 0
            }
        
        # Cross-suite scalability assessment
        vm_memory_savings = []
        assembly_scalability_scores = []
        
        if vm_analysis.get('success', False):
            for result in vm_analysis.get('detailed_results', {}).values():
                if 'memory_analysis' in result and 'savings_percentage' in result['memory_analysis']:
                    vm_memory_savings.append(result['memory_analysis']['savings_percentage'])
        
        if assembly_analysis.get('success', False):
            for analysis in assembly_analysis.get('detailed_results', {}).values():
                scalability = analysis.get('scalability_analysis', {})
                if 'linear_scaling_score' in scalability:
                    assembly_scalability_scores.append(scalability['linear_scaling_score'])
        
        insights['scalability_assessment'] = {
            'average_memory_savings': sum(vm_memory_savings) / len(vm_memory_savings) if vm_memory_savings else 0,
            'average_scalability_score': sum(assembly_scalability_scores) / len(assembly_scalability_scores) if assembly_scalability_scores else 0,
            'memory_optimization_samples': len(vm_memory_savings),
            'scalability_samples': len(assembly_scalability_scores)
        }
        
        return insights
    
    def generate_recommendations(self, aggregate_stats, cross_suite_insights):
        """Generate recommendations based on analysis results"""
        recommendations = []
        
        # Overall success rate recommendations
        if aggregate_stats['overall_success_rate'] < 0.8:
            recommendations.append({
                'category': 'reliability',
                'priority': 'high',
                'issue': f"Overall test success rate is {aggregate_stats['overall_success_rate']*100:.1f}%",
                'recommendation': "Investigate failing tests and improve system robustness"
            })
        
        # Petri net translation recommendations
        petri_effectiveness = cross_suite_insights.get('petri_net_effectiveness', {})
        if petri_effectiveness.get('translation_success_rate', 0) < 0.9:
            recommendations.append({
                'category': 'petri_translation',
                'priority': 'medium',
                'issue': f"Petri net translation success rate is {petri_effectiveness.get('translation_success_rate', 0)*100:.1f}%",
                'recommendation': "Review VM to Petri net translation logic for edge cases"
            })
        
        # Assembly generation recommendations
        assembly_quality = cross_suite_insights.get('assembly_generation_quality', {})
        if assembly_quality.get('assembly_success_rate', 0) < 0.8:
            recommendations.append({
                'category': 'assembly_generation',
                'priority': 'high',
                'issue': f"Assembly generation success rate is {assembly_quality.get('assembly_success_rate', 0)*100:.1f}%",
                'recommendation': "Improve assembly generator robustness across different core configurations"
            })
        
        # Stack-free execution recommendations
        execution_consistency = cross_suite_insights.get('execution_pattern_consistency', {})
        if execution_consistency.get('stack_free_rate', 0) < 1.0:
            recommendations.append({
                'category': 'execution_model',
                'priority': 'critical',
                'issue': f"Stack-free verification rate is {execution_consistency.get('stack_free_rate', 0)*100:.1f}%",
                'recommendation': "Ensure all execution patterns maintain pure Petri net semantics without hidden stack state"
            })
        
        # Performance recommendations
        scalability = cross_suite_insights.get('scalability_assessment', {})
        if scalability.get('average_scalability_score', 0) < 0.7:
            recommendations.append({
                'category': 'performance',
                'priority': 'medium',
                'issue': f"Average scalability score is {scalability.get('average_scalability_score', 0):.3f}",
                'recommendation': "Optimize multi-core assembly generation and load balancing algorithms"
            })
        
        # Memory optimization recommendations
        if scalability.get('average_memory_savings', 0) < 15:
            recommendations.append({
                'category': 'memory_optimization',
                'priority': 'low',
                'issue': f"Average memory savings is {scalability.get('average_memory_savings', 0):.1f}%",
                'recommendation': "Enhance memory optimization algorithms to achieve higher savings"
            })
        
        return recommendations
    
    def generate_human_readable_summary(self, master_report):
        """Generate a human-readable summary report"""
        summary_file = os.path.join(self.test_results_dir, "analysis_summary.md")
        
        try:
            with open(summary_file, 'w') as f:
                f.write("# Comprehensive VM and Petri Net Analysis Summary\n\n")
                f.write(f"**Analysis Date:** {time.ctime(master_report['analysis_metadata']['timestamp'])}\n")
                f.write(f"**Total Duration:** {master_report['analysis_metadata']['total_duration']:.2f} seconds\n\n")
                
                # Overall Results
                f.write("## Overall Results\n\n")
                stats = master_report['aggregate_statistics']
                f.write(f"- **Total Test Suites:** {stats['total_suites']}\n")
                f.write(f"- **Successful Suites:** {stats['successful_suites']}\n")
                f.write(f"- **Total Tests:** {stats['total_tests']}\n")
                f.write(f"- **Tests Passed:** {stats['total_passed']}\n")
                f.write(f"- **Tests Failed:** {stats['total_failed']}\n")
                f.write(f"- **Overall Success Rate:** {stats['overall_success_rate']*100:.1f}%\n\n")
                
                # Suite Results
                f.write("## Suite Results\n\n")
                for suite_name, results in master_report['suite_results'].items():
                    status = "✅ PASSED" if results.get('success', False) else "❌ FAILED"
                    f.write(f"### {suite_name} {status}\n")
                    f.write(f"- Duration: {results.get('duration', 0):.2f} seconds\n")
                    f.write(f"- Tests Passed: {results.get('passed', 0)}\n")
                    f.write(f"- Tests Failed: {results.get('failed', 0)}\n\n")
                
                # Key Insights
                f.write("## Key Insights\n\n")
                insights = master_report['cross_suite_insights']
                
                petri_eff = insights.get('petri_net_effectiveness', {})
                if petri_eff:
                    f.write(f"- **Petri Net Translation Success Rate:** {petri_eff.get('translation_success_rate', 0)*100:.1f}%\n")
                
                assembly_qual = insights.get('assembly_generation_quality', {})
                if assembly_qual:
                    f.write(f"- **Assembly Generation Success Rate:** {assembly_qual.get('assembly_success_rate', 0)*100:.1f}%\n")
                
                exec_cons = insights.get('execution_pattern_consistency', {})
                if exec_cons:
                    f.write(f"- **Stack-Free Verification Rate:** {exec_cons.get('stack_free_rate', 0)*100:.1f}%\n")
                
                scalability = insights.get('scalability_assessment', {})
                if scalability:
                    f.write(f"- **Average Memory Savings:** {scalability.get('average_memory_savings', 0):.1f}%\n")
                    f.write(f"- **Average Scalability Score:** {scalability.get('average_scalability_score', 0):.3f}\n\n")
                
                # Recommendations
                f.write("## Recommendations\n\n")
                for rec in master_report.get('recommendations', []):
                    priority_emoji = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢"}.get(rec['priority'], "⚪")
                    f.write(f"### {priority_emoji} {rec['category'].title()} ({rec['priority'].title()} Priority)\n")
                    f.write(f"**Issue:** {rec['issue']}\n\n")
                    f.write(f"**Recommendation:** {rec['recommendation']}\n\n")
                
                f.write("---\n")
                f.write("*Generated by Comprehensive VM and Petri Net Analysis Suite*\n")
            
            print(f"Saved human-readable summary: {summary_file}")
            
        except Exception as e:
            print(f"Error generating human-readable summary: {e}")
    
    def print_final_summary(self):
        """Print final summary to console"""
        total_duration = time.time() - self.start_time
        
        print(f"\n{'='*100}")
        print("COMPREHENSIVE ANALYSIS COMPLETE")
        print('='*100)
        
        print(f"Total analysis time: {total_duration:.2f} seconds")
        print(f"Analysis completed at: {time.ctime()}")
        
        # Print suite results
        print(f"\nSuite Results:")
        for suite_name, results in self.suite_results.items():
            status = "PASSED" if results.get('success', False) else "FAILED"
            duration = results.get('duration', 0)
            passed = results.get('passed', 0)
            failed = results.get('failed', 0)
            print(f"  {suite_name}: {status} ({passed} passed, {failed} failed, {duration:.2f}s)")
        
        # Print aggregate statistics
        if self.suite_results:
            stats = self.calculate_aggregate_statistics()
            print(f"\nAggregate Statistics:")
            print(f"  Total tests: {stats['total_tests']}")
            print(f"  Overall success rate: {stats['overall_success_rate']*100:.1f}%")
            print(f"  Suite success rate: {stats['suite_success_rate']*100:.1f}%")
        
        print(f"\nDetailed results saved in: {self.test_results_dir}/")
        print("=" * 100)


if __name__ == "__main__":
    master = ComprehensiveAnalysisMaster()
    success = master.run_all_comprehensive_suites()
    sys.exit(0 if success else 1)