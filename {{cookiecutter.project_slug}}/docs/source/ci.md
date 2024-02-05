
## Github continuous integration

### Code quality

The file `.github/workflows/code_quality.yml` runs Ruff and Black on every push and pull request to verify the conformity of the code.

We recommend adding the following tools to your repository. You do not need to install them on your computer, as they will automatically run when you push changes to the main repository via a GitHub Pull Request.

- [pre-commit.ci](http://pre-commit.ci) : Run pre-commit (as defined in .pre-commit-config.yaml).
- [CodeBeat](https://codebeat.co/) : Automated code review and analysis tools.
- [CodeScene](https://codescene.com/) : Automated code review and analysis tools.
- [CodeFactor](https://www.codefactor.io/) : Automated code review and analysis tools

### Code Testing

The file `.github/workflows/tests.yml` runs pytest on every push and pull request to verify the conformity of the code with different versions of python.

We recommend adding the following tools to your repository. You do not need to install them on your computer, as they will automatically run when you push changes to the main repository via a GitHub Pull Request.

- [CodeCov](https://about.codecov.io/) : Uses the “coverage” package to generate a code coverage report.
- [Coveralls](https://coveralls.io/) : Uses the “coverage” to track the quality of your code over time.
