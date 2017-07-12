import os
import hcl


class TerraformChecker(object):
    """Terraform checking class."""

    tf_file_paths = []
    validation_errors = []

    def __init__(self, root_path):
        """Read the Terraform from the provided path."""
        self.validation_errors = []
        self.tf_file_paths = self._get_tf_file_paths(root_path)

    def _get_tf_file_paths(self, root_path):
        """List paths for all the Terraform files to check."""
        ret = []
        for root, subdirs, files in os.walk(root_path):
            for file_name in files:
                if file_name.endswith('.tf'):
                    root_path = self._ensure_trailing_slash(root)
                    full_path = root_path + file_name
                    ret.append(full_path)

        return ret

    def validate(self):
        """Checks the Terraform configs."""

        for file_path in self.tf_file_paths:
            self._validate_tf_file(file_path)
            self._validate_tf_file_name(file_path)

        return self.validation_errors

    def _validate_tf_file_name(self, file_path):
        """Check tf file name is either main.tf, output.tf or variables.tf."""

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

    def _validate_tf_section_names(self, file_path, hcl_obj):
        """Check that tf module, resource, variable, etc... names are valid."""
        for section, v in hcl_obj.items():
            for name, v2 in hcl_obj[section].items():
                if '-' in name:
                    self._add_error(
                        file_path,
                        '{} "{}" contains a "-" in the name. Use '
                        '"_" instead.'.format(section.capitalize(), name)
                    )

    def _ensure_trailing_slash(self, root):
        """Ensures the given path has a trailing slash."""
        return root if root.endswith('/') else root + '/'

    def _add_error(self, path, error):
        """Adds an error to the validation errors."""
        self.validation_errors.append({'path': path, 'error': error})


checker = TerraformChecker('sample-terraform/')
checker.validate()
print(checker.validation_errors)
