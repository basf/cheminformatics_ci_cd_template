# CI/CD github actions template for Python projects
This repository provides a simple and easy to use CI/CD template for python projects using github actions.

The [cheminformatics team at BASF](https://github.com/orgs/basf/teams/cix) created this template to share with
their collaborators and the community.
With the template you can easily check the quality of your code and run tests on every push to your repository.
This ensures that your code is always in a good state and that you can easily collaborate with others.

## How to use

The template is in the [`.github/workflows/code_check.yml`](.github/workflows/code_check.yml) file.
To use the template, copy the `.github` folder to your repository and add the directory names of your
project as indicated by the TODOs at the top of the `code_check.yml` file.

## What does the template do?

The template contains the following steps to check the quality of your code:

Linters:
- `pylint` is one of the most comprehensive linter and catches most linting problems.
- `pydocstyle` helps to have consistent doc-strings throughout the project.
- `black` formats your code in a consistent way.
- `isort` sorts your imports in a consistent way.

Tests:
- `coverage` to run unit tests and generate a test coverage report. The test coverage can 
  give you valuable insides while developing/writing test and is a quality measure for your project.
  In the template a threshold of 80% test coverage is set to ensure high coverage.
