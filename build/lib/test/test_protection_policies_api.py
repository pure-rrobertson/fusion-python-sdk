# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import fusion
from fusion.api.protection_policies_api import ProtectionPoliciesApi  # noqa: E501
from fusion.rest import ApiException


class TestProtectionPoliciesApi(unittest.TestCase):
    """ProtectionPoliciesApi unit test stubs"""

    def setUp(self):
        self.api = ProtectionPoliciesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_protection_policy(self):
        """Test case for create_protection_policy

        Creates a Protection Policy.  # noqa: E501
        """
        pass

    def test_delete_protection_policy(self):
        """Test case for delete_protection_policy

        Deletes a specific protection policy.  # noqa: E501
        """
        pass

    def test_get_protection_policy(self):
        """Test case for get_protection_policy

        Gets a specific Protection Policy.  # noqa: E501
        """
        pass

    def test_get_protection_policy_by_id(self):
        """Test case for get_protection_policy_by_id

        Gets a specific Protection Policy.  # noqa: E501
        """
        pass

    def test_list_protection_policies(self):
        """Test case for list_protection_policies

        Gets a list of all Protection Policies.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
