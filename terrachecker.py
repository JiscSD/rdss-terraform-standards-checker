import os
import hcl


class TerraformChecker(object):
    """Terraform checking class."""

    root_dir_path = None
    walks = []
    errors = []

    def __init__(self, dir_path):
        """Read the Terraform from the provided path."""
        self.root_dir_path = dir_path
        self.walks = self._get_path_walks(dir_path)

    def _get_path_walks(self, dir_path):
        """Finds all Terraform configs in the given dir path."""
        ret = []
        for root, subdirs, files in os.walk(dir_path):
            ret.append({
                'root': root,
                'subdirs': subdirs,
                'files': files
            })
        return ret

    def validate(self):
        """Checks the Terraform configs."""
        for walk in self.walks:
            root = self._ensure_trailing_slash(walk['root'])
            subdirs = walk['subdirs']
            files = walk['files']

            for file_name in files:
                self._check_file(root + file_name)

    def _ensure_trailing_slash(self, root):
        """Ensures the given path has a trailing slash."""
        return root if root.endswith('/') else root + '/'

    def _check_file(self, file_path):
        """Loop through and validates list of files."""

        if file_path.endswith('.tf'):
            self.errors.extend(self._root_tf_file_errors(file_path))

    def _root_tf_file_errors(self, path):
        """Check the root terraform and return a list of errors or None."""
        ret = []

        # Check module names do not contain resource with hyphen.
        with open(path) as f:
            print("Checking file at path: {}".format(path))
            try:
                obj = hcl.load(f)
                ret.append(self._hcl_tf_errors(path, obj))
            except ValueError as ve:
                ret.append(self._error_dict(path, str(ve)))

        return []

    def _hcl_tf_errors(self, path, hcl_obj):
        """Check a givn hcl object and return any validation errors."""
        ret = []
        if 'module' in hcl_obj:
            ret.append(self._tf_module_errors(path, hcl_obj['module']))

        return ret

    def _tf_names_not_using_underscore_errors(self, path, modules):
        """Find any errors in the provided module."""
        ret = []
        for k, v in modules.items():
            if '-' in k:
                ret.append(self._error_dict(
                    path,
                    'Module "{}" contains a "-", use "_" instead.'.format(k)))

        return ret

    def _error_dict(self, path, error):
        """Adds an error to the errors array."""
        self.errors.append({'path': path, 'error': error})


checker = TerraformChecker('sample-terraform/')
checker.validate()
print(checker.errors)
