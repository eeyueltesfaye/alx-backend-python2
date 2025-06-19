#!/usr/bin/env python3
"""Unit tests for GithubOrgClient.org method
"""
from client import GithubOrgClient
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient.org"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        """Test that GithubOrgClient.org returns expected data and get_json is called once"""
        mock_get_json.return_value = expected  # Mock the JSON response

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, expected)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test that _public_repos_url returns expected repo URL from org payload."""
        expected_url = "https://api.github.com/orgs/test_org/repos"

        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": expected_url}

            client = GithubOrgClient("test_org")
            result = client._public_repos_url
            self.assertEqual(result, expected_url)
