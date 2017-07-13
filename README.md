# RDSS Terraform Standards Checker
A script which checks Terraform configs against the standards described here: https://jiscdev.atlassian.net/wiki/display/RDSS/Terraform+coding+standards.

## Usage

To configure a project to use `terrachecker` follow these steps:

 1) Install Terrachecker:

```
pip install -e git+git@github.com:JiscRDSS/rdss-terraform-standards-checker.git@develop#egg=terrachecker
```

Or simple add `git+git@github.com:JiscRDSS/rdss-terraform-standards-checker.git@develop#egg=terrachecker` to *requirements.txt* of your project.

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
