import requests

from . exceptions import AuthError


class IOSXE(object):
    def __init__(self, node, user, password, port=55443, verify=False, disable_warnings=False, timeout=2):
        """
        Class to manage Cisco IOS-XE devices via the REST API
        :param node: IP address or Hostname
        :param user:  User with privilege level 15 access
        :param password: Users password
        :param verify: Verify SSL certificate
        :param disable_warnings: Disable SSL warnings
        :param timeout: Request timeout value
        """
        self.node = node
        self.user = user
        self.password = password
        self.port = port

        self.url_base = 'https://{0}:{1}/api/v1'.format(self.node, self.port)
        self.xe = requests.session()
        self.xe.auth = (self.user, self.password)
        self.xe.verify = verify  # http://docs.python-requests.org/en/latest/user/advanced/#ssl-cert-verification
        self.disable_warnings = disable_warnings
        self.timeout = timeout
        self.xe.headers.update({
            'Accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded'
        })

        if self.disable_warnings:
            requests.packages.urllib3.disable_warnings()

        # Authentication Token
        token_uri = '/auth/token-services'
        resp = self.xe.post('{0}{1}'.format(self.url_base, token_uri))
        if resp.status_code == 401:
            raise AuthError('Authorisation failed, check username and password')
        elif resp.status_code == 200:
            self.api_token = resp.json()['token-id']
            self.xe.headers.update({'x-auth-token': self.api_token})

    def get_bgp(self):
        uri = '/routing-svc/bgp'
        resp = self.xe.get('{0}{1}'.format(self.url_base, uri))
        return resp
