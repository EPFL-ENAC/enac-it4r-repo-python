# ENAC-IT4R Python project template

## Introduction

**What is included on this template?**

🖼️ Templates for starting multiple type of python projects.

📦 A basic `pyproject.toml` file to provide installation, packaging and distribution for your project.

🧪 Testing structure using [pytest](https://docs.pytest.org/en/latest/).

✅ Code linting and formater using [Black](https://github.com/psf/black) and [Ruff](https://github.com/charliermarsh/ruff).

🤝 Typing checking using [mypy](https://mypy.readthedocs.io/en/stable/)

🔄 Continuous integration using [Github Actions](https://github.com/rochacbruno/python-project-template/blob/main/.github/workflows) with jobs to lint, test and release your project on Linux, Mac and Windows environments

📃 Documentation with sphinx.

💬 Auto generation of change log using **gitchangelog** to keep a HISTORY.md file automatically based on your commit history on every release.




## Template structure


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
