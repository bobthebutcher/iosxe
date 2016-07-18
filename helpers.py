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
    def __init__(self,
                 ok=False, response=None, status_code=None,
                 error=None, message=None, json=None):
        self.ok = ok
        self.response = response
        self.status_code = status_code
        self.error = error
        self.message = message
        self.json = json


def parse_result(response):

    result = Result()

    if response.status_code in HTTP_ERROR_CODES:
        result.ok = False
        result.error = HTTP_ERROR_CODES[response.status_code]

    elif response.status_code in HTTP_SERVER_ERRORS:
        result.ok = False
        result.error = HTTP_SERVER_ERRORS[response.status_code]

    elif response.status_code in HTTP_SUCCESS_CODES:
        result.ok = True
        result.message = HTTP_SUCCESS_CODES[response.status_code]

    result.status_code = response.status_code
    result.json = response.json()
