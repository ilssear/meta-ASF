<!--
Copyright (c) 2025, Jim Moran
All rights reserved.

This source code is licensed under the MIT-style license found in the
LICENSE file in the root directory of this source tree. 
-->
# Testing Workflow Guide

This document defines the standard testing workflow for projects developed using the SpecFirst framework.

## 1. Philosophy

Testing is not a separate phase but an integral part of the development process. The goal is to ensure that the software meets the requirements defined in `SPECIFICATIONS.md` and is of high quality.

## 2. Testing Levels

The testing workflow incorporates several levels of testing:

-   **Unit Testing**: Testing individual components in isolation.
-   **Integration Testing**: Testing how different components work together.
-   **End-to-End (E2E) Testing**: Testing complete user workflows.
-   **Acceptance Testing**: Validating the software against user and business requirements.

## 3. Testing Workflow Steps

### Step 1: Test Planning

-   For each feature defined in `SPECIFICATIONS.md`, a set of test cases should be created.
-   Test cases for all levels of testing should be considered.
-   Test data required for the test cases should be identified and prepared.

### Step 2: Test Implementation

-   **Unit Tests**: Developers are responsible for writing unit tests for the code they produce. Unit tests should be written alongside the application code. See `docs/development/testing/unit_testing.md`.
-   **Integration Tests**: These tests are created to verify interactions between components. See `docs/development/testing/integration_testing.md`.
-   **E2E Tests**: These tests are based on user workflows and should be created as described in `docs/development/testing/e2e_testing.md`.

### Step 3: Test Execution

-   **Continuous Integration (CI)**: All unit and integration tests should be run automatically by the CI server on every commit.
-   **Staging Environment**: E2E tests should be run in the staging environment before deploying to production.
-   **Manual Testing**: Some scenarios may require manual testing, especially for exploratory testing and usability checks.

### Step 4: Defect Management

-   Any test failures or bugs found during testing should be reported in the project's issue tracking system.
-   Each bug report should include:
    -   A clear and descriptive title.
    -   Steps to reproduce the bug.
    -   The expected result vs. the actual result.
    -   Any relevant logs or screenshots.
-   The priority of the bug should be assessed, and it should be assigned to a developer for fixing.

## 4. Code Coverage

-   The project should aim for a high level of code coverage for unit tests.
-   Code coverage reports should be generated as part of the CI process to track progress.
-   While 100% coverage is not always practical, critical parts of the application should be thoroughly tested. 