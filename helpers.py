HTTP_SUCCESS_CODES = {
    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    204: 'Accepted but with no JSON body',
}

HTTP_ERROR_CODES = {
    400: 'Bad Request',
    401: 'Unauthorized',
    404: 'Not Found',
    405: 'Method not Allowed',
}

HTTP_SERVER_ERRORS = {
    500: 'Internal Server Error',
    503: 'Service Unavailable',
}


class Result(object):
    def __init__(self, ok=False, error=None, json=None):
        pass
