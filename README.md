# Getting Started

## **Python quick setup**

For a quick guide to installing Python and setting it up, please take a look at the [ENAC-IT4R Python webpage](https://www.notion.so/Python-quick-setup-55d1e813f24d4a37a57e14c71c641a0e).

This repository contains the following files and folders:

```
📦 Repository
 ┣ 📁 .github : contain the github settings
 ┣ 📁 ISSUE_TEMPLATE : contains issues templates
 ┃ ┗ 📜 *.yaml
 ┣ 📁 workflows : contains CICD processes
 ┃ ┣ 📜 code_quality.yml : Ruff + Black + mypy
 ┃ ┗ 📜 tests.yml : pytest + CodeCov
 ┣ 📁 docs: contains the documentation.
 ┣ 📁 project_name: contains the project code.
 ┃ ┗ 📜 *.py
 ┣ 📁 test: contains the project tests.
 ┃ ┗ 📜 test_*.py
 ┣ 📜 .gitignore: lists the files/folders to ignore for git.
 ┣ 📜 pre-commit-config.yaml: configuration file for pre-commit.
 ┣ 📜 LICENSE: license file.
 ┣ 📜 pyproject.toml: project configuration file.
 ┣ 📜 README.md: markdown file containing the project's readme.
 ```


## Python environment

All external packages are defined into the `pyproject.toml`.

While not mandatory, utilizing a virtual environment is recommended. Using a virtual environment for installing packages provides isolation of dependencies, easier package management, easier maintenance, improved security, and improved development
workflow.

To set up a virtual environment with venv, follow these steps :

- Windows: Create a virtual environment with venv

    ```bash
    python -m venv venv
    cd venv/Scripts
    activate
    ```

- Mac/Linux: Create a virtual environment with venv:

    ```bash
    virtualenv -p python3 disdrodb-dev
    source disdrodb-dev/bin/activate
    ```


To install the project dependencies, run `pip` as follows:

```bash
pip install .
```

The `pyproject.toml` contains the following selection to define the dev dependencies:

```toml
[project.optional-dependencies]
dev = [
	"pre-commit==3.3.1",
	"pytest",
	"pytest-cov",
	"pytest-mock",
	"black==22.8.0",
	"ruff==0.0.257"
	]
```

To install these dependencies, run:

```bash
pip install .[dev]
```

## Code quality (linter + formatter)

We use Black as a code formatter and Ruff as a linter to guarantee good code quality.

After setting up your development environment, install the git pre-commit hook by executing the following command in the repository’s root:

```bash
pre-commit install
```

Pre-commit can be run as follows:

```bash
pre-commit run --all-files
```

Note that it will only run Ruff and Black against staged files.

To run Ruff against all files individually:

```bash
ruff check .
```

And black as well :

```bash
black .
```

The pre-commit hooks are scripts executed automatically in every commit to identify simple code quality issues.

## Testing

Every code change must be tested !

We recommend to use the third-party [pytest](https://docs.pytest.org/) package.

The tests located in the `/tests`  folder are used to test various functions of the code and are
automatically run when changes are pushed to the main repository through a GitHub Pull Request.

To run all tested functions wih pytest, run :

```bash
pytest -vv -s
```

Note that `pytest-cov` has been added to `pyproject.toml`. Therefore, running pytest will display the project coverage and create a folder `/htmlcov` containing the coverage analysis (HTML files).
