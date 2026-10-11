# Module 01: Runtime Anatomy & Execution Environments

Understanding how Python boots, locates libraries, isolates dependencies, and interfaces with version control and the operating system.

---

## 🗺️ Module Map

| Resource | Type | Purpose |
| :--- | :--- | :--- |
| [01_execution_mechanics_and_environments.md](./docs/01_execution_mechanics_and_environments.md) | **Deep-Dive Theory** | Mental models, OS path resolution, shims, `pyvenv.cfg`, environment taxonomy, Git boundaries, and comparative tradeoffs. |
| [01_runtime_probe.py](./exercises/01_runtime_probe.py) | **Executable Lab** | Hands-on diagnostic script and challenges introspecting `sys.prefix`, `sys.base_prefix`, `sys.path`, and environment isolation. |

---

## 🎯 Learning Objectives

By the end of this module, you will understand:
1. **The Execution Path**: Exactly what happens between pressing `Enter` on `python myscript.py` and CPython executing bytecode.
2. **Environment Detection**: The exact C-level mechanism (`pyvenv.cfg`) CPython uses to determine if it is in a virtual environment.
3. **The Tooling Landscape**: When to choose `venv`, `uv`, `conda`, or `Docker`, and why global package installations are an anti-pattern.
4. **Git Hygiene**: How environments interact with version control, why environments must never be committed, and how to track dependencies reproducibly with lockfiles and `pyproject.toml`.
