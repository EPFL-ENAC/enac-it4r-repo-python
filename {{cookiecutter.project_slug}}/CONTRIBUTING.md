# {{cookiecutter.github_repo_name}} Contributing Guide

Hi! Thanks for taking the time to contribute to {{cookiecutter.github_repo_name}}.

_You can contribute in many ways_

- Join the [discussion](https://github.com/{{cookiecutter.github_repo_name}}/discussions)

_Before submitting your contribution, please make sure to take a moment and read through the following guidelines_

- [Code of Conduct](https://github.com/{{cookiecutter.github_repo_name}}/blob/main/CODE_OF_CONDUCT.md)
- [Issue Reporting Guidelines](#issue-reporting-guidelines)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Development Setup](#development-setup)
- [Commit Lint](#commit-lint)

## Issue Reporting Guidelines

- Always use [ issue templates ](https://github.com/{{cookiecutter.github_repo_name}}/issues/new/choose)
- If you don't find a corresponding issue template please use the template to ask a new template

## Pull Request Guidelines

### Timeline example

1. Create an issue (fix/feature/etc..)
2. Create branch from issue
   - the issue's title should be what you expect your branch name to be
3. Checkout locally, push commits to github
4. Create pull-request from branch
5. Merge pull-request

   - To avoid merge commit like this:
     'Merge pull request #3 from EPFL-ENAC/2-bug-remove-ecoinvent-embodied-data
   - Replace the github automatic merge commit message by the a conventional-changelog valid commit message usually a simple copy/paste from the pull-request title is enough
   - see this [blog post](https://mokacoding.com/blog/better-merging-for-github-pull-requests/) for an example

6. Issue is auto-close

### We Develop with Github

We use github to host code, to track issues and feature requests, as well as accept pull requests.

### We Use [Github Flow](https://docs.github.com/en/get-started/quickstart/github-flow),

- All Code Changes Happen Through Pull Requests.
  Pull requests are the best way to propose changes to the codebase (we use [Github Flow](https://docs.github.com/en/get-started/quickstart/github-flow)). We actively welcome your pull requests:

- If your pull request addresses an issue, link the issue so that issue stakeholders are aware of the pull request and vice versa.

- It's better to create a branch from an issue, the issue number will directly be in the branch name
  - see [discussion for reference](https://github.com/github-community/community/discussions/12290)



### maybe todo ?

1. Fork the repo and create your branch from `dev`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs or added breaking change, update the documentation and notify the users.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

### Recommendation for the pull request

- Add screenshots or GIFs for any UI changes. This will help the person reviewing your code to understand what you’ve changed and how it works.
  - _Hint: use [Kap](https://getkap.co/) or [Licecap](https://www.cockos.com/licecap/) to record your screen._
- If your team uses a particular template for pull requests, fill it. Otherwise at least make sure you have:

  - the user problem you are solving;
  - acceptance criteria of the ticket;
  - testing you have done or plan to do before release;
  - any pull request that are dependent on this one, or any tickets on which this pull request depends.

- The `main` branch is just a snapshot of the latest stable release. All development should be done in dedicated branches. **Do not submit PRs against the `main` branch.**

- Checkout a topic branch from the relevant branch, e.g. `dev`, and merge back against that branch.

- Work in the `frontend` folder and **DO NOT** checkin `dist` in the commits.

- It's OK to have multiple small commits as you work on the PR - GitHub will automatically squash it before merging.

- If adding a new feature:

  - Add accompanying test case.
  - Provide a convincing reason to add this feature. Ideally, you should open a suggestion issue first and have it approved before working on it.
  - Present your issue in the 'discussion' part of this repo

- If fixing bug:
  - If you are resolving a special issue, add `(fix #xxxx[,#xxxx])` (#xxxx is the issue id) in your PR title for a better release log, e.g. `update entities encoding/decoding (fix #3899)`.
  - Provide a detailed description of the bug in the PR. Live demo preferred.
  - Add appropriate test coverage if applicable.

### Code review checklist

- Ask to people to review your code:
  - a person who knows the domain well and can spot bugs in the business logic;
  - an expert in the technologies you’re using who can help you improve the code quality.
- When you’re done with the changes after a code review, do another self review of the code and write a comment to notify the reviewer, that the pull request is ready for another iteration.
- Review all the review comments and make sure they are all addressed before the next review iteration.
- Make sure you don’t have similar issues anywhere else in your pull request.
- If you’re not going to follow any of the code review recommendations, please add a comment explaining why.
- Avoid writing comment like "done" of "fixed" on each code review comment. Reviewers assume you’ll do all suggested changes, unless you have a reason not to do some of them.
- Sometimes it’s okay to postpone changes — in this case you’ll need to add a ticket number to the pull request and to the code itself.

## Development Setup

You will need [Node.js](http://nodejs.org) **lts** and [npm](https://pnpm.io/). And also Gnu Make

After cloning the repo, run:

```bash
$ make install # install the dependencies of the project
```

## Financial Contribution

We also welcome financial contributions. Please contact us directly.

## Commit Lint

We follow a commit message convention, to have consistent git messages. The goal is to increase readability and ease of contribution. We use [commit-lint with the conventional-changelog extension](https://github.com/conventional-changelog/commitlint)

## Credits

Thank you to all the people who have already contributed to {YOUR-REPO-NAME} repository!
