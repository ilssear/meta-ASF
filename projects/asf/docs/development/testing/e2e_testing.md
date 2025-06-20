<!--
Copyright (c) 2025, Jim Moran
All rights reserved.

This source code is licensed under the MIT-style license found in the
LICENSE file in the root directory of this source tree. 
-->
# End-to-End (E2E) Testing Guide

This document provides guidelines for conducting end-to-end (E2E) testing for projects developed using the SpecFirst framework.

## 1. What is E2E Testing?

End-to-end testing is a methodology used to test whether the flow of an application from start to finish is behaving as expected. The purpose of E2E testing is to identify system dependencies and to ensure that data integrity is maintained between various system components and systems.

## 2. E2E Testing in the SpecFirst Framework

In the SpecFirst framework, E2E tests are derived directly from the user workflows defined in `SPECIFICATIONS.md`. Each E2E test case should represent a complete user journey.

## 3. Creating E2E Test Cases

1.  **Identify User Workflows**: Review the `User Workflows` section in `SPECIFICATIONS.md`. Each defined workflow is a candidate for an E2E test.
2.  **Define Test Steps**: For each workflow, break it down into a sequence of user actions and system responses.
3.  **Specify Expected Outcomes**: For each step, define the expected outcome. This includes changes in the UI, data state, or system behavior.
4.  **Cover Edge Cases**: Consider alternative paths, error conditions, and edge cases for each workflow.

## 4. Example E2E Test Case

**Workflow**: User Registration and Login

| Step | User Action                               | Expected Outcome                                        |
|------|-------------------------------------------|---------------------------------------------------------|
| 1    | Navigate to the registration page.        | The registration form is displayed.                     |
| 2    | Fill in the registration form with valid data. | The form is submitted successfully.                      |
| 3    | Submit the form.                          | A confirmation message is shown.                        |
| 4    | Navigate to the login page.               | The login form is displayed.                            |
| 5    | Enter the newly created credentials.      | The user is successfully logged in.                     |
| 6    | Log in.                                   | The user is redirected to the dashboard.                |

## 5. Tools for E2E Testing

For web applications, consider using tools like:

-   **Selenium**: A powerful browser automation tool.
-   **Cypress**: A modern, all-in-one testing framework.
-   **Playwright**: A framework for web testing and automation.

The choice of tool should be documented in the project's `docs/development/testing/README.md`. 