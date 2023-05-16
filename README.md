# ENAC-IT4R Python project template

## Introduction

**What is included on this template?**

🖼️ Templates for starting multiple type of python projects.

📦 A basic `pyproject.toml` file to provide installation, packaging and distribution for your project.

🧪 Testing structure using [pytest](https://docs.pytest.org/en/latest/).

✅ Code linter [Ruff](https://github.com/charliermarsh/ruff).

✏️ Code formatter using [Black](https://github.com/psf/black).

🤝 Typing checking using [Mypy](https://mypy.readthedocs.io/en/stable/).

🔄 Continuous integration using [Github Actions](https://github.com/rochacbruno/python-project-template/blob/main/.github/workflows) with jobs to lint, test and release your project on Linux, Mac and Windows environments.

📃 Documentation with [Sphinx](https://www.sphinx-doc.org/en/master/) and [Readthedocs](https://readthedocs.org/).



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
 ┣ 📜 CITATION.cff: citation information.
 ┣ 📜 CODE_OF_CONDUCT.md: code of conduct.
 ┣ 📜 CONTRIBUTING.md: contributing guidelines.
 ┣ 📜 LICENSE: license file.
 ┣ 📜 pyproject.toml: project configuration file.
 ┣ 📜 README.md: markdown file containing the project's readme.
 ┣ 📜 readthedocs.yml: Settings for readthedocs.
 ```

## Documentation

Please take a look at the following resources:

* [Template documentation](https://enac-it4r-repo-python.readthedocs.io)
* [ENAC-IT4R python guidelines](https://enacit4r.notion.site/Python-quick-setup-55d1e813f24d4a37a57e14c71c641a0e)
* [ENAC-IT4R git guidelines](https://enacit4r.notion.site/Install-Git-0a608fb1909f471284c189cf172c9016)



## Todo when setting up your github repo

- [ ] Learn how to use github template repository: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template
- [ ] Activate discussion (https://github.com/EPFL-ENAC/{YOUR-REPO-NAME}/settings)
- [ ] Replace `{YOUR-REPO-NAME}` by the name of your repo
- [ ] Modifiy or remove the `CITATION.cff` file. [How to format it ?](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)
- [ ] Check if you need all those labels: https://github.com/EPFL-ENAC/{YOUR-REPO-NAME}/labels
- [ ] Create your first milestone: https://github.com/EPFL-ENAC/{YOUR-REPO-NAME}/milestones
- [ ] Protect your branch if you're a pro user: https://github.com/EPFL-ENAC/{YOUR-REPO-NAME}/settings/branches
- [ ] Change `project_name` in the code with your project name.
