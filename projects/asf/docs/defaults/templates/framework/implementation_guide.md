<!--
Copyright (c) 2025, Jim Moran
All rights reserved.

This source code is licensed under the MIT-style license found in the
LICENSE file in the root directory of this source tree. 
-->
# Implementation Guide Template

This document provides a template for guiding the implementation phase of a project within the SpecFirst framework.

## 1. Guiding Principles

- **Specification is King**: The `SPECIFICATIONS.md` file is the single source of truth for all implementation work. No feature should be built that is not described in the specifications.
- **Incremental Value**: Implement features in small, testable increments that deliver value.
- **Clarity and Simplicity**: Write clear, simple, and maintainable code. Avoid over-engineering.
- **Test Everything**: All new code must be accompanied by corresponding unit and integration tests.

## 2. Pre-Implementation Checklist

- [ ] The `SPECIFICATIONS.md` file is complete and has been approved.
- [ ] The development environment is set up according to `docs/development/setup/environment_setup.md`.
- [ ] All required tools and dependencies are installed.
- [ ] The project structure has been created.

## 3. Implementation Workflow

1.  **Select a Feature**: Choose a feature from `SPECIFICATIONS.md` to implement.
2.  **Create a Feature Branch**: Create a new git branch for the feature (e.g., `feature/user-authentication`).
3.  **Develop the Code**:
    -   Write the application code, following the style guides in `docs/framework/style`.
    -   Adhere to the architectural patterns defined in `docs/framework/patterns`.
4.  **Write Tests**:
    -   Write unit tests that cover the new code.
    -   Write integration tests to ensure the new feature works with the existing system.
5.  **Update Documentation**:
    -   Update the `README.md` if necessary.
    -   Add or update API documentation.
    -   Ensure all changes are reflected in the project's documentation.
6.  **Submit a Pull Request**:
    -   Push the feature branch to the remote repository.
    -   Create a pull request and link it to the relevant section of `SPECIFICATIONS.md`.
    -   Ensure all automated checks and tests pass.
7.  **Code Review**:
    -   The code is reviewed for correctness, style, and adherence to specifications.
8.  **Merge**:
    -   Once approved, the feature branch is merged into the main development branch.

## 4. Post-Implementation

- Verify that the feature is working as expected in the integrated environment.
- Close the corresponding task or user story. 