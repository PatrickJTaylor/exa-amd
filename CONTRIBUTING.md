# Contributing to exa-AMD

Thank you for your interest in contributing to exa-AMD.
We welcome contributions that improve performance and extend functionality.

This document describes the conventions, expectations, and workflow for contributors.

---

## Developer Workflow

1. Fork or branch:
   - If you don’t have write access, fork the repo and work on your fork.
   - If you do have write access, create a branch on this repo.
   - Create a feature branch (e.g., `feature/new-dft-engine`).
2. Implement changes following the coding, testing, and performance guidelines below.
3. Add or update unit tests for new functionality (when feasible).
4. Run all workflows in [`workflows/`](https://github.com/ML-AMD/exa-amd/tree/main/workflows) on the CeFeIn system:
   - Verify scientific correctness of outputs.
   - Confirm all CI checks pass.
   - Confirm no performance regressions.
5. Update documentation (docstrings, README/tutorials) if relevant.
6. Commit with a meaningful message that follows the [50/72 rule](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).
7. Open a Pull Request/Merge Request (PR/MR) to `main`:
   - Assign at least one reviewer.
   - Both the contributor and the reviewer must run/validate the workflows on CeFeIn and confirm correct results (some features require licensed tools like VASP and are not covered by unit tests).
   - Resolve all review comments before merging.

---

## Coding Standards

- Adhere to PEP 8.
- Prefer automated tools to enforce style.
- Use type hints where practical.
- Keep code modular and well-documented with clear docstrings (use standard triple-quoted strings).

---

## Testing Guidelines

- Place tests under `tests/` using `pytest` conventions.
- Write unit tests for all new functionality (when possible).
- All PRs must pass tests locally and in CI.
- For components that rely on licensed tools (e.g., VASP):
  - Validate via by running the [`workflows/`](https://github.com/ML-AMD/exa-amd/tree/main/workflows) on the CeFeIn system.
  - Summarize manual validation steps and results in the PR description.

---

## Performance Requirements

Performance (how fast we explore new structures for a given system) is critical for exa-AMD:

- Ensure every change does not degrade performance.
- Optimize hardware usage:
  - Use GPUs when possible.
  - Utilize all physical cores with proper task mapping (e.g., using Parsl).
  - Enable hyperthreading only when benchmarking confirms a net gain.
- Avoid unnecessary synchronization or serial bottlenecks: prefer asynchronous and parallel patterns where possible.

---

## Dependencies

- Add new dependencies only when strictly required.
- Prefer existing dependencies and internal utilities:
  - Example: use Parsl for parallelism instead of adding `mpi4py` when feasible.
- Document any new dependency in the PR description and pin it in `pyproject.toml` or `amd_env.yml`.

---

## Current Priorities

- Investigate new DFT engines beyond VASP (e.g., Quantum ESPRESSO).
- Explore new ML models for formation-energy prediction and compare their performance and accuracy with CGCNN.

---
