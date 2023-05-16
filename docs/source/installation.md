
# Installation

## Project settings

All external packages are defined into the `pyproject.toml`.



## Project installation

To install the project dependencies, run `pip` as follows:

```bash
pip install .
```

The `pyproject.toml` contains the `[project.optional-dependencies]` selection to define the development dependencies:



To install these dependencies, run:

```bash
pip install .[dev]
```


## Virtual environment

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
