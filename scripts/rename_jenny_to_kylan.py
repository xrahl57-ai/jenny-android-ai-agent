#!/usr/bin/env python3
"""
Automated refactoring script to rename 'jenny' package to 'kyĺan'.

Run this script from the root of the repository to perform the rename:
    python3 scripts/rename_jenny_to_kylan.py

This script:
1. Renames the jenny/ directory to kyĺan/
2. Updates all Python imports from 'jenny' to 'kyĺan'
3. Updates documentation and configuration files
4. Updates comments that reference 'jenny' (where appropriate)
"""

import os
import re
import shutil
from pathlib import Path


def rename_directory():
    """Rename jenny/ directory to kyĺan/."""
    src = Path("jenny")
    dst = Path("kyĺan")
    
    if src.exists() and not dst.exists():
        print(f"Renaming directory: {src} -> {dst}")
        shutil.move(str(src), str(dst))
        print("✓ Directory renamed successfully")
    elif dst.exists():
        print(f"✓ Directory {dst} already exists")
    else:
        print(f"✗ Source directory {src} not found")
        return False
    return True


def update_file_imports(file_path: Path) -> bool:
    """Update imports in a Python file."""
    try:
        content = file_path.read_text(encoding='utf-8')
        original = content
        
        # Update imports: from jenny.xxx import -> from kyĺan.xxx import
        content = re.sub(
            r'from\s+jenny\s*\.',
            r'from kyĺan.',
            content
        )
        
        # Update imports: import jenny.xxx -> import kyĺan.xxx
        content = re.sub(
            r'import\s+jenny\s*\.',
            r'import kyĺan.',
            content
        )
        
        # Update string references in docstrings/comments (jenny -> kyĺan)
        # But preserve user-visible names like "Jenny gateway"
        content = re.sub(
            r'(?<![A-Z])jenny(?=\.|\s*[,)])',
            r'kyĺan',
            content,
            flags=re.IGNORECASE
        )
        
        if content != original:
            file_path.write_text(content, encoding='utf-8')
            return True
    except Exception as e:
        print(f"  ✗ Error processing {file_path}: {e}")
    return False


def update_python_files():
    """Update all Python files with new imports."""
    kylan_dir = Path("kyĺan")
    updated_count = 0
    
    if not kylan_dir.exists():
        print("✗ kyĺan directory not found. Run rename_directory() first.")
        return 0
    
    print("\nUpdating Python imports...")
    for py_file in kylan_dir.rglob("*.py"):
        if update_file_imports(py_file):
            updated_count += 1
            print(f"  ✓ {py_file}")
    
    return updated_count


def update_documentation():
    """Update documentation files."""
    print("\nUpdating documentation...")
    
    files_to_update = [
        Path("README.md"),
        Path("docs/README.md"),
        Path("SECURITY.md"),
        Path("CONTRIBUTING.md"),
    ]
    
    updated_count = 0
    for file_path in files_to_update:
        if not file_path.exists():
            continue
        
        try:
            content = file_path.read_text(encoding='utf-8')
            original = content
            
            # Replace "Jenny" with "Kyĺan" in documentation (case-sensitive)
            # Note: Be careful to preserve proper nouns and brand names
            content = content.replace("jenny", "kyĺan")
            content = content.replace("Jenny", "Kyĺan")
            
            if content != original:
                file_path.write_text(content, encoding='utf-8')
                updated_count += 1
                print(f"  ✓ {file_path}")
        except Exception as e:
            print(f"  ✗ Error processing {file_path}: {e}")
    
    return updated_count


def update_tests():
    """Update test files and imports."""
    print("\nUpdating tests...")
    
    test_dir = Path("tests")
    if not test_dir.exists():
        print("  No tests directory found")
        return 0
    
    updated_count = 0
    for py_file in test_dir.rglob("*.py"):
        if update_file_imports(py_file):
            updated_count += 1
            print(f"  ✓ {py_file}")
    
    return updated_count


def main():
    """Main refactoring orchestration."""
    print("=" * 70)
    print("Jenny → Kyĺan Package Rename")
    print("=" * 70)
    
    if not Path("pyproject.toml").exists():
        print("\n✗ Error: pyproject.toml not found. Run this script from repo root.")
        return False
    
    print("\n1. Renaming directory...")
    if not rename_directory():
        return False
    
    print("\n2. Updating imports in package files...")
    py_count = update_python_files()
    print(f"   Updated {py_count} Python files")
    
    print("\n3. Updating test files...")
    test_count = update_tests()
    print(f"   Updated {test_count} test files")
    
    print("\n4. Updating documentation...")
    doc_count = update_documentation()
    print(f"   Updated {doc_count} documentation files")
    
    print("\n" + "=" * 70)
    print("Refactoring complete!")
    print(f"Total updates: {py_count + test_count + doc_count + 1}")
    print("=" * 70)
    
    print("\nNext steps:")
    print("1. Review the changes: git diff")
    print("2. Run tests: pytest tests/")
    print("3. Run type checks: pyright")
    print("4. Run linting: ruff check .")
    print("\nThen commit and push:")
    print("  git add .")
    print("  git commit -m 'refactor: rename package from jenny to kyĺan'")
    print("  git push origin rename-jenny-to-kylan")
    
    return True


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
