import os
import hcl


class TerraformChecker(object):
    """Terraform checker."""

    tf_file_paths = []
    validation_errors = []

    def __init__(self, root_path):
        """Read the Terraform configs from the provided path."""
        self.validation_errors = []
        self.tf_file_paths = self._get_tf_file_paths(root_path)

    def _get_tf_file_paths(self, root_path):
        """Retrieve paths for all the Terraform files to check."""
        ret = []
        for root, subdirs, files in os.walk(root_path):
            for file_name in files:
                if '.terraform' in root:
                    continue
                if file_name.endswith('.tf'):
                    root_path = self._ensure_trailing_slash(root)
                    full_path = root_path + file_name
                    ret.append(full_path)

        return ret

    def is_valid(self):
        """Validate Terraform configs and return True if pass else False"""
        for file_path in self.tf_file_paths:
            self._validate_tf_file(file_path)
            self._validate_tf_file_name(file_path)
        if len(self.validation_errors) > 0:
            return False
        return True

    def _validate_tf_file_name(self, file_path):
        """Check tf file name is valid."""
        file_name = file_path.split('/')[-1]
        if file_name not in ['main.tf', 'variables.tf', 'outputs.tf']:
            self._add_error(
                file_path,
                'Name {} is invalid. Please use only '
                '"main.tf", "variables.tf" or "outputs.tf"'.format(
                    file_name, file_path))

    def _validate_tf_file(self, file_path):
        """Load Terraform file at given path and validate."""
        with open(file_path) as f:
            try:
                obj = hcl.load(f)
            except ValueError as ve:
                self._add_error(file_path, str(ve))
                return

            self._validate_tf_section_names(file_path, obj)
            if 'module' in obj:
                self._validate_tf_module(file_path, obj['module'])

    def _validate_tf_section_names(self, file_path, hcl_obj):
        """Check that tf module, resource, variable, etc... names are valid."""
        for section, v in hcl_obj.items():
            if section in ['resource', 'data']:
                self._validate_tf_section_names(file_path, hcl_obj[section])
                continue
            for name, v2 in hcl_obj[section].items():
                if '-' in name:
                    self._add_error(
                        file_path,
                        '{} "{}" contains a "-" in the name. Use '
                        '"_" instead.'.format(section, name)
                    )

    def _validate_tf_module(self, file_path, hcl_modules):
        """Validate a terraform module reference."""
        for k, v in hcl_modules.items():
            source = hcl_modules[k]['source']
            if source.startswith('./') and 'modules' not in source:
                self._add_error(
                    file_path,
                    'Module {} source does not contain "modules" in the '
                    'path name. Place all modules in a subdirectory called '
                    '"modules".'.format(k)
                )

    def _ensure_trailing_slash(self, root):
        """Ensures the given path has a trailing slash."""
        return root if root.endswith('/') else root + '/'

    def _add_error(self, path, error):
        """Adds an error to the validation errors."""
        self.validation_errors.append({'path': path, 'error': error})
