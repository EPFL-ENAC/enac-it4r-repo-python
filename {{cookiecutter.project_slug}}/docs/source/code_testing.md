# Testing

Every code change must be tested!

We recommend to use the third-party [pytest](https://docs.pytest.org/) package.

The tests located in the `/tests`  folder are used to test various functions of the code and are
automatically run when changes are pushed to the main repository through a GitHub Pull Request.

To run all tested functions with pytest, run:

```bash
pytest -vv -s
```

Note that `pytest-cov` has been added to `pyproject.toml`. Therefore, running pytest will display the project coverage and create a folder `/htmlcov` containing the coverage analysis (HTML files).
