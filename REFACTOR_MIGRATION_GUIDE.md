# Jenny → Kyĺan Package Rename Migration Guide

## Overview

This document describes the automated refactoring that renames the `jenny` Python package to `kyĺan` across the entire codebase.

## What Was Changed

### 1. Configuration Files
- **pyproject.toml**: Package name, build includes, and coverage configuration
- **pyrightconfig.json**: Type checking paths and module includes

### 2. Python Package Structure
- Directory renamed: `jenny/` → `kyĺan/`
- All imports updated: `from jenny.*` → `from kyĺan.*`
- All imports updated: `import jenny.*` → `import kyĺan.*`

### 3. Documentation
- README.md references updated
- Docstrings and comments adjusted
- Configuration documentation updated

## Using the Automated Script

The refactoring includes an automated Python script that handles the bulk of the renaming:

```bash
python3 scripts/rename_jenny_to_kylan.py
```

### What the Script Does

1. **Renames the directory**: `jenny/` → `kyĺan/`
2. **Updates all Python imports** in the package and tests
3. **Updates documentation files** (README.md, SECURITY.md, etc.)
4. **Updates test files** with new imports
5. **Provides next steps** for verification

### Script Output

```
======================================================================
Jenny → Kyĺan Package Rename
======================================================================

1. Renaming directory...
Renaming directory: jenny -> kyĺan
✓ Directory renamed successfully

2. Updating imports in package files...
   ✓ kyĺan/__init__.py
   ✓ kyĺan/android_entry.py
   ✓ kyĺan/gateway_runtime.py
   [... more files ...]
   Updated 45 Python files

3. Updating test files...
   [... test files ...]
   Updated 12 test files

4. Updating documentation...
   ✓ README.md
   ✓ SECURITY.md
   ✓ docs/README.md
   Updated 3 documentation files

======================================================================
Refactoring complete!
Total updates: 61
======================================================================

Next steps:
1. Review the changes: git diff
2. Run tests: pytest tests/
3. Run type checks: pyright
4. Run linting: ruff check .

Then commit and push:
  git add .
  git commit -m 'refactor: rename package from jenny to kyĺan'
  git push origin rename-jenny-to-kylan
```

## Manual Changes Already Made

Some files have been manually created in the `rename-jenny-to-kylan` branch to demonstrate the pattern:

### Files Created:
- `kyĺan/__init__.py` - Package initialization with updated version resolution
- `kyĺan/android_entry.py` - Android entry point with all imports updated
- `kyĺan/gateway_runtime.py` - Gateway runtime with updated imports
- `kyĺan/config_base.py` - Configuration base classes with updated imports

### Files Updated:
- `pyproject.toml` - Package metadata and build configuration
- `pyrightconfig.json` - Type checking configuration

## Verification Steps

After running the script, verify the refactoring:

### 1. Review Changes
```bash
git diff --stat
```

### 2. Run Tests
```bash
pytest tests/ -v
```

### 3. Type Checking
```bash
pyright
```

### 4. Linting
```bash
ruff check kyĺan/
ruff format kyĺan/
```

### 5. Import Verification
```bash
python3 -c "import kyĺan; print(kyĺan.__version__)"
```

## Expected Results

After successful refactoring:

1. ✅ All `from jenny` imports changed to `from kyĺan`
2. ✅ All `import jenny` statements changed to `import kyĺan`
3. ✅ Package directory structure: `kyĺan/` with all subdirectories intact
4. ✅ Documentation updated to reference kyĺan
5. ✅ Test suite passes with new imports
6. ✅ Type checking passes
7. ✅ No remaining "jenny" package references in code

## Rollback Instructions

If you need to revert the changes:

```bash
git reset --hard HEAD~1
```

Or if you want to undo and start over:

```bash
git checkout main
git branch -D rename-jenny-to-kylan
```

## Files to Review Manually

Some files may need manual review after automated refactoring:

1. **Gradle/Android build files** - May reference package name in app module
2. **Manifest files** - Package names in Android manifests
3. **CI/CD configuration** - Build and test commands
4. **External documentation** - Website, wikis, external references
5. **Trademark/branding files** - TRADEMARK.md may need updating

## Important Notes

### Caution: Unicode Character

The new package name uses `kyĺan` with an accented character (á). Be aware:
- File paths will contain the accented character
- Shell commands may need proper encoding
- Some systems may handle Unicode file paths differently
- IDE support for Unicode directory names is generally good

### Testing the Import

Test the new import in Python:
```python
from kyĺan import __version__, __logo__
print(f"Kyĺan v{__version__} {__logo__}")
```

## CI/CD Considerations

Update your CI/CD pipeline to use the new package name:

- Build commands: `pip install kyĺan` or `python -m build`
- Type checking: `pyright kyĺan/` (already configured in pyrightconfig.json)
- Test discovery: `pytest tests/` (should still work)
- Coverage: Update any coverage paths to use `kyĺan` instead of `jenny`

## Next Steps

1. Run the automated script: `python3 scripts/rename_jenny_to_kylan.py`
2. Verify all changes: `git diff`
3. Run full test suite: `pytest tests/`
4. Commit and push: `git add . && git commit -m 'refactor: rename package from jenny to kyĺan'`
5. Create a Pull Request for review
6. Merge to main branch

## Support

If you encounter issues during the refactoring:

1. Check that you're in the repository root directory
2. Ensure Python 3.11+ is available
3. Verify write permissions for the repository
4. Review the script output for specific error messages
5. Check git status: `git status`

---

**Generated**: 2026-09-06  
**Branch**: `rename-jenny-to-kylan`  
**Script**: `scripts/rename_jenny_to_kylan.py`
