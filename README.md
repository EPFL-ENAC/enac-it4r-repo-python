[![Project Status](https://img.shields.io/badge/status-under%20development-yellow)](https://github.com/EPFL-ENAC/enac-it4r-repo-python)

This project is currently under development.

# ENAC-IT4R Python project template


This template serves as a foundation for developing Python projects using  modern tools and best practices.

**What is included on this template?**

🖼️ Templates for starting multiple type of python projects.

📦 A basic `pyproject.toml` file to provide installation, packaging and distribution for your project.

🧪 Testing structure using [Pytest](https://docs.pytest.org/en/latest/).

✅ Code linter [Ruff](https://github.com/charliermarsh/ruff).

✏️ Code formatter using [Black](https://github.com/psf/black).

🤝 Typing checking using [Mypy](https://mypy.readthedocs.io/en/stable/).

🔄 Continuous integration using [Github Actions](https://github.com/rochacbruno/python-project-template/blob/main/.github/workflows) with jobs to check the quality of your code.

📃 Documentation with [Sphinx](https://www.sphinx-doc.org/en/master/) and [Readthedocs](https://readthedocs.org/). Include necessary details for generating documentation, performing test and code quality checks, and installing the project.




## How to use this template ?

On github (or any other git repository) :

1. Create a brand new Github repository to host your project.

On your local computer :

1. Install Cookiecutter: If you haven't already, you need to install Cookiecutter on your system. You can use pip, the Python package manager, to install Cookiecutter by running the following command:

    ```bash
    pip install cookiecutter  
    ```

1. Generate the project from the template by running the following command with a command prompt or terminal from the clone repository location :

    ```bash
    cookiecutter https://github.com/EPFL-ENAC/enac-it4r-repo-python
    ```
 1. Provide input values: Cookiecutter will prompt you for input values to customize the generated project. The template may define variables or placeholders that need to be filled in. Answer the prompts with the desired values to configure your project.

1. Generate the project: After providing all the necessary input values, Cookiecutter will generate the project based on the template. It will create a new directory with the generated project structure and files.

1. Customize the project: Once the project is generated, you can navigate to the newly created directory and start customizing the project according to your requirements. You can modify files, add additional dependencies, configure settings, and make any other necessary changes. 

1. Link your folder to your repository :

    ```bash
    git init 
    git remote add origin <repository-url>  
    ```




## Documentation

Please take a look at the following resources:

* [Template documentation](https://enacit4r.notion.site/ENAC-IT4R-Python-project-template-eca32ebf56e44a79a55faf2d57b5a796)
* [ENAC-IT4R python guidelines](https://enacit4r.notion.site/Python-quick-setup-55d1e813f24d4a37a57e14c71c641a0e)
* [ENAC-IT4R git guidelines](https://enacit4r.notion.site/Install-Git-0a608fb1909f471284c189cf172c9016)

