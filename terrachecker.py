import os
import hcl


class TerraformChecker(object):
    """Terraform checking class."""

    root_dir_path = ''
    walks = []
    errors = []

    def __init__(self, dir_path):
        """Read the Terraform from the provided path."""
        self.root_dir_path = dir_path
        self.walks = self._get_walks(dir_path)

    def _get_walks(self, dir_path):
        """Finds all Terraform configs in the given dir path."""
        ret = []
        for root, subdirs, files in os.walk(dir_path):
            ret.append({
                'root': root,
                'subdirs': subdirs,
                'files': files
            })
        return ret

    def check(self):
        """Checks the Terraform configs."""
        print(self.walks)

        for walk in walks:
            root = walk['root']
            subdirs = walk['subdirs']
            files = walk['files']

            for file_name in files:
                self._check_file(root + file_name)

    def _check_file(self, file_path):
        """Loop through and validates list of files."""
        for file_name in files:
            full_path = root + file_name
            for error in self._root_tf_file_errors(full_path):
                self.errors.append(self._error_dict(full_path, error))

    def _root_tf_file_errors(self, path):
        """Check the root terraform and return a list of errors or None."""

        # Check module names do not contain resource with hyphen.
        with open(path) as f:

        return []

    def _check_file(self, file_path):
        """Checks a specific file path."""
        pass

    def _check_module(self, file_path):
        """Checks a specific module."""
        pass

    def _error_dict(self, path, error):
        """Adds an error to the errors array."""
        self.errors.append({'path': path, 'error': error})


checker = TerraformChecker('sample-terraform/')
checker.check()
