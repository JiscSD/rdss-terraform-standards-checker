import pytest

from terrachecker.terraform_checker import TerraformChecker


class TestTerraformChecker(object):
    """Test the Terraform checker module."""

    def test_ensure_trailing_slash_adds_slash(self):
        """Ensure the trailing slash function adds a slash."""
        root = 'something/test'
        checker = TerraformChecker('test/')
        new_root = checker._ensure_trailing_slash(root)
        assert new_root == root + '/'
