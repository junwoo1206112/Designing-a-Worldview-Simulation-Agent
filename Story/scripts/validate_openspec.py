#!/usr/bin/env python3
"""
OpenSpec 명세 검증 스크립트
라프라시아 야구 시뮬레이션 RPG 프로젝트
"""

import os
import json
import sys
from datetime import datetime
from pathlib import Path


class OpenSpecValidator:
    """OpenSpec 디렉토리 및 명세 검증"""
    
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir)
        self.openspec_dir = self.root_dir / "openspec"
        self.errors = []
        self.warnings = []
        self.info = []
    
    def validate_directory_structure(self) -> bool:
        """디렉토리 구조 검증"""
        print("📁 Checking directory structure...")
        
        required_dirs = [
            "openspec/changes/active",
            "openspec/changes/archive",
            "openspec/specs",
            "openspec/proposals"
        ]
        
        all_exist = True
        for dir_path in required_dirs:
            full_path = self.root_dir / dir_path
            if not full_path.exists():
                self.errors.append(f"Missing directory: {dir_path}")
                all_exist = False
            else:
                self.info.append(f"✓ {dir_path}")
        
        return all_exist
    
    def validate_active_changes(self) -> bool:
        """활성 변경 사항 검증"""
        print("\n📝 Checking active changes...")
        
        active_dir = self.root_dir / "openspec/changes/active"
        if not active_dir.exists():
            self.warnings.append("No active changes directory")
            return True
        
        changes = [d for d in active_dir.iterdir() if d.is_dir()]
        print(f"   Found {len(changes)} active change(s)")
        
        all_valid = True
        for change in changes:
            required_files = ["proposal.md", "design.md", "tasks.md"]
            missing = []
            
            for file in required_files:
                if not (change / file).exists():
                    missing.append(file)
            
            if missing:
                self.warnings.append(f"{change.name}: Missing {', '.join(missing)}")
                all_valid = False
            else:
                self.info.append(f"✓ {change.name}: Complete")
        
        return all_valid
    
    def validate_spec_files(self) -> bool:
        """명세 파일 검증"""
        print("\n📄 Checking spec files...")
        
        specs_dir = self.root_dir / "openspec/specs"
        if not specs_dir.exists():
            self.warnings.append("No specs directory")
            return True
        
        spec_files = [f for f in specs_dir.iterdir() if f.suffix == ".md"]
        print(f"   Found {len(spec_files)} spec file(s)")
        
        all_valid = True
        for spec in spec_files:
            with open(spec, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Check for minimum content
            if len(content) < 100:
                self.warnings.append(f"{spec.name}: May be too short")
                all_valid = False
            elif "#" not in content:
                self.warnings.append(f"{spec.name}: Missing headers")
                all_valid = False
            else:
                self.info.append(f"✓ {spec.name}: Valid")
        
        return all_valid
    
    def validate_proposals(self) -> bool:
        """제안서 검증"""
        print("\n💡 Checking proposals...")
        
        proposals_dir = self.root_dir / "openspec/proposals"
        if not proposals_dir.exists():
            self.warnings.append("No proposals directory")
            return True
        
        proposal_files = [f for f in proposals_dir.iterdir() if f.suffix == ".md"]
        print(f"   Found {len(proposal_files)} proposal(s)")
        
        for proposal in proposal_files:
            with open(proposal, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Check for required sections
            required_sections = ["배경", "목표", "범위"]
            korean_sections = [s for s in required_sections if s in content]
            english_sections = ["Background", "Goal", "Scope"]
            has_sections = len(korean_sections) >= 2 or len(english_sections) >= 2
            
            if has_sections:
                self.info.append(f"✓ {proposal.name}: Complete")
            else:
                self.warnings.append(f"{proposal.name}: May be missing sections")
        
        return True
    
    def check_spec_code_consistency(self) -> bool:
        """명세 - 코드 일관성 검사"""
        print("\n🔗 Checking spec-code consistency...")
        
        import re
        
        specs_dir = self.root_dir / "openspec/specs"
        if not specs_dir.exists():
            return True
        
        for spec in specs_dir.iterdir():
            if spec.suffix != ".md":
                continue
            
            with open(spec, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Find file references (backtick notation)
            file_refs = re.findall(r"`([^`]+\.(py|json|md))`", content)
            
            for ref, _ in file_refs[:10]:  # Check first 10 references
                ref_path = self.root_dir / ref
                if not ref_path.exists():
                    self.warnings.append(f"{spec.name}: References non-existent {ref}")
        
        return True
    
    def generate_report(self) -> dict:
        """검증 보고서 생성"""
        return {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "project": "라프라시아 야구 시뮬레이션 RPG",
            "status": "valid" if not self.errors else "invalid",
            "summary": {
                "errors": len(self.errors),
                "warnings": len(self.warnings),
                "info": len(self.info)
            },
            "errors": self.errors,
            "warnings": self.warnings,
            "info": self.info,
            "recommendations": self._generate_recommendations()
        }
    
    def _generate_recommendations(self) -> list:
        """권장 사항 생성"""
        recommendations = []
        
        if self.errors:
            recommendations.append("Fix errors before continuing")
        
        if not os.path.exists(self.root_dir / "openspec/changes/active"):
            recommendations.append("Consider starting a new change proposal with '/opsx:propose'")
        
        if len(self.warnings) > 5:
            recommendations.append("Review warnings to improve spec quality")
        
        return recommendations
    
    def run(self) -> int:
        """검증 실행"""
        print("=" * 60)
        print("  OpenSpec Validator")
        print("  라프라시아 야구 시뮬레이션 RPG")
        print("=" * 60)
        
        # Run all validations
        self.validate_directory_structure()
        self.validate_active_changes()
        self.validate_spec_files()
        self.validate_proposals()
        self.check_spec_code_consistency()
        
        # Generate report
        report = self.generate_report()
        
        # Save report
        report_dir = self.root_dir / ".github" / "openspec-reports"
        report_dir.mkdir(parents=True, exist_ok=True)
        report_path = report_dir / "validation-report.json"
        
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        # Print summary
        print("\n" + "=" * 60)
        print("  Summary")
        print("=" * 60)
        print(f"  Errors:   {report['summary']['errors']}")
        print(f"  Warnings: {report['summary']['warnings']}")
        print(f"  Info:     {report['summary']['info']}")
        
        if report["recommendations"]:
            print("\n  Recommendations:")
            for rec in report["recommendations"]:
                print(f"    • {rec}")
        
        print(f"\n  Report saved to: {report_path}")
        print("=" * 60)
        
        # Return exit code
        return 1 if self.errors else 0


def main():
    """메인 함수"""
    import argparse
    
    parser = argparse.ArgumentParser(description="OpenSpec Validator")
    parser.add_argument(
        "--root",
        default=".",
        help="Project root directory"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON report only"
    )
    
    args = parser.parse_args()
    
    validator = OpenSpecValidator(args.root)
    exit_code = validator.run()
    
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
