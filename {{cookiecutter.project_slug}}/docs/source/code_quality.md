# Code quality


We use Black as a **code formatter**, Ruff as a **code linter**, and mypy as a **static type checker**. These tools aim to guarantee good code quality.

After setting up your development environment, install the git pre-commit hook by executing the following command in the repository’s root:

```bash
pre-commit install
```

Pre-commit can be run as follows:

```bash
pre-commit run --all-files
```

Note that it will only run Ruff, Black and Mypy against staged files.

To run Ruff against all files individually:

```bash
ruff check .
```

And black as well :

```bash
black .
```

To run mypy against all files individually:

```bash
mypy .
```

Note that no error is raised if a function is not typed.

The pre-commit hooks are scripts executed automatically in every commit to identify simple code quality issues.
