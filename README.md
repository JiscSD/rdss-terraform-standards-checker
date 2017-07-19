# RDSS Terraform Standards Checker
A script which checks Terraform configs against the standards described here: https://jiscdev.atlassian.net/wiki/display/RDSS/Terraform+coding+standards.

## Usage

To configure a project to use `terrachecker` follow these steps:

 1) Install Terrachecker:

```
pip install terrachecker
```

Or simple add `terrachecker` to *requirements.txt* of your project.

 2) Run Terrachecker:

```
terrachecker infra/
```

*Note: Replace `infra/` with path to Terraform configs.*

## Development

### Developer Setup

Install `virtualenv` globall using pip and then run the following:

```
make env
source env/bin/activate
make deps
```

### Testing

To run linter and unit tests:

```
make lint
make autopep8
make test
```

### Developer FAQ

 1) How do I change the encrypted PyPi password in `.travis.yml`?

The `.travis.yml` file contains an encrypted password which can be decrypted by Travis-CI when pushing to PyPi.

To change this password, you will first need to install the [Travis CLI tool](https://github.com/travis-ci/travis.rb#installation).

Next, login to Travis CLI using the `--pro` flag (you **must** use this flag otherwise the encrypted string you generate will be useless).

```
travis login --pro
```

From the project directory run:

```
travis encrypt '<NEW_PASSWORD>' --add deploy.password --pro
```

**Important: Remember the `--pro` flag.**
