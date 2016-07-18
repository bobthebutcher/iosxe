"""
Tests are performed against csr1000v-universalk9.03.15.00.S.155-2.S-std.
"""
import unittest

from iosxe.iosxe import IOSXE
from iosxe.exceptions import AuthError

node = '172.16.92.134'
username = 'cisco'
password = 'cisco'
port = 55443


class TestIOSXE(unittest.TestCase):

    def setUp(self):
        self.xe = IOSXE(node=node, username=username, password=password, disable_warnings=True)

    def test_iosxe_is_a_IOSXE(self):
        self.assertIsInstance(self.xe, IOSXE)

    def test_invalid_user_pass_returns_auth_error(self):

        self.assertRaises(AuthError, IOSXE, node=node, username='stuff', password='things',
                          disable_warnings=True)

    def test_url_base(self):
        self.assertEqual(self.xe.url_base, 'https://{0}:{1}/api/v1'.format(node, port))

    def test_token_uri(self):
        self.assertEqual(self.xe.token_uri, '/auth/token-services')

    def test_save_config_success(self):
        resp = self.xe.save_config()
        self.assertEqual(204, resp.status_code)

