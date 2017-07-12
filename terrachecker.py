import sys

from app import TerraformChecker


checker = TerraformChecker('sample-terraform/')
if not checker.is_valid():
    for error in checker.validation_errors:
        print('{}: {}'.format(error['path'], error['error']))
    sys.exit(1)

sys.exit(0)
