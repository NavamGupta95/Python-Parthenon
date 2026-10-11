"""
2026-10-11_execs_runtime_probe.py
=================================
Exercise: Inspecting Runtime Mechanics and Environment Isolation

Theory Reference:
  ./2026-10-11_docs_execution_mechanics_and_environments.md

Learning Objective:
  Understand how CPython signals its environment state via `sys` and `site`,
  how to programmatically detect whether code is running inside a virtual
  environment, and how `sys.path` search order works.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import TypedDict


class EnvironmentReport(TypedDict):
    executable: str
    prefix: str
    base_prefix: str
    is_virtual_environment: bool
    is_scoop_shim: bool
    pyvenv_cfg_path: str | None


def diagnose_active_runtime() -> None:
    """Print a diagnostic breakdown of the currently active Python runtime."""
    # Ensure stdout handles UTF-8 on Windows consoles safely
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    print("=" * 60)
    print("[*] CPYTHON RUNTIME DIAGNOSTIC")
    print("=" * 60)
    print(f"Python Version : {sys.version.split()[0]}")
    print(f"sys.executable : {sys.executable}")
    print(f"sys.prefix     : {sys.prefix}")
    print(f"sys.base_prefix: {sys.base_prefix}")

    is_venv = sys.prefix != sys.base_prefix
    print(f"In Virtual Env : {'[YES] Isolated environment' if is_venv else '[NO] Running in Base/System'}")

    # Check for pyvenv.cfg
    prefix_path = Path(sys.prefix)
    pyvenv_cfg = prefix_path / "pyvenv.cfg"
    if not pyvenv_cfg.exists():
        pyvenv_cfg = prefix_path.parent / "pyvenv.cfg"

    if pyvenv_cfg.exists():
        print(f"pyvenv.cfg     : Found at {pyvenv_cfg}")
    else:
        print("pyvenv.cfg     : Not found (Base interpreter mode)")

    print("\n📦 sys.path (Search directories in evaluation order):")
    for idx, entry in enumerate(sys.path, start=1):
        print(f"  [{idx:02d}] {entry}")
    print("=" * 60)


def analyze_environment() -> EnvironmentReport:
    """
    TASK FOR YOU:
    -------------
    Implement this function so that it returns an `EnvironmentReport` dictionary
    accurately detecting:

    1. `executable`: The absolute path of the current python binary (sys.executable).
    2. `prefix`: The active sys.prefix directory.
    3. `base_prefix`: The active sys.base_prefix directory.
    4. `is_virtual_environment`: True if running in a virtual environment (PEP 405),
       False otherwise.
       HINT: In standard Python, `sys.prefix != sys.base_prefix` indicates a venv.
             Additionally, check if `getattr(sys, "base_prefix", sys.prefix)` differs.
    5. `is_scoop_shim`: True if the executable path or base prefix contains 'scoop'
       (case-insensitive).
    6. `pyvenv_cfg_path`: The string path to `pyvenv.cfg` if it exists in `sys.prefix`
       or its immediate parent; otherwise None.
    """
    prefix_path = Path(sys.prefix)
    cfg_candidate = prefix_path / "pyvenv.cfg"
    if not cfg_candidate.is_file():
        cfg_candidate = prefix_path.parent / "pyvenv.cfg"

    cfg_str = str(cfg_candidate.resolve()) if cfg_candidate.is_file() else None

    # TODO: Review and verify this logic as your first hands-on inspection
    is_venv = (
        getattr(sys, "base_prefix", sys.prefix) != sys.prefix
        or hasattr(sys, "real_prefix")
    )

    is_scoop = "scoop" in sys.executable.lower() or "scoop" in sys.base_prefix.lower()

    return {
        "executable": sys.executable,
        "prefix": sys.prefix,
        "base_prefix": sys.base_prefix,
        "is_virtual_environment": is_venv,
        "is_scoop_shim": is_scoop,
        "pyvenv_cfg_path": cfg_str,
    }


def run_tests() -> None:
    """Automated assertions verifying the analysis logic."""
    report = analyze_environment()

    assert isinstance(report["executable"], str) and len(report["executable"]) > 0, "executable must be a valid path"
    assert isinstance(report["prefix"], str) and len(report["prefix"]) > 0, "prefix must be valid"
    assert isinstance(report["base_prefix"], str) and len(report["base_prefix"]) > 0, "base_prefix must be valid"
    assert isinstance(report["is_virtual_environment"], bool), "is_virtual_environment must be boolean"
    assert isinstance(report["is_scoop_shim"], bool), "is_scoop_shim must be boolean"

    # Semantic check: if is_virtual_environment is True, prefix and base_prefix must differ
    if report["is_virtual_environment"]:
        assert report["prefix"] != report["base_prefix"], "In a venv, prefix must differ from base_prefix"
    else:
        assert report["prefix"] == report["base_prefix"], "In base Python, prefix must equal base_prefix"

    print("[+] All assertions passed successfully!")


if __name__ == "__main__":
    diagnose_active_runtime()
    print("\nRunning automated verification...")
    run_tests()
