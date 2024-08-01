# CI/CD github actions template for Python projects
This repository provides a simple and easy to use CI/CD template for python projects using github actions.

The template is in the `.github/workflows/code_check.yml` file. It contains the following steps to 
check the quality of your code:

Linters:
- `pylint` is one of the most comprehensive linter and catches most linting problems.
- `pydocstyle` helps to have consistent doc-strings throughout the project.
- `black` formats your code in a consistent way.
- `isort` sorts your imports in a consistent way.

Tests:
- `coverage` to run unit tests and generate a test coverage report. The test coverage can 
  give you valuable insides while developing/writing test and is a quality measure for your project.
  In the template a threshold of 80% test coverage is set to ensure high coverage.

