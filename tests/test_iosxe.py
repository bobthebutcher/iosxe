"""
Tests are performed against csr1000v-universalk9.03.15.00.S.155-2.S-std.
"""
import unittest

from iosxe.iosxe import IOSXE

node = '172.16.92.134'
username = 'cisco'
password = 'cisco'
port = 55443


class TestIOSXE(unittest.TestCase):

    def setUp(self):
        self.xe = IOSXE(node=node, username=username, password=password, disable_warnings=True)

    def test_iosxe_is_a_IOSXE(self):
        self.assertIsInstance(self.xe, IOSXE)

    def test_url_base(self):
        self.assertEqual(self.xe.url_base, 'https://{0}:{1}/api/v1'.format(node, port))

    def test_token_uri(self):
        self.assertEqual(self.xe.token_uri, '/auth/token-services')
