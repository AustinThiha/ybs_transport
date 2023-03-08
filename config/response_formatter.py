from rest_framework import status
from rest_framework.response import Response


def success(args):
    return Response(_response_formatter(args, status_code=status.HTTP_200_OK), status=status.HTTP_200_OK)


def fail(error=None, status_code=status.HTTP_400_BAD_REQUEST):
    return Response(_response_formatter([], status_code=status_code, error=error),
                    status=status.HTTP_400_BAD_REQUEST)


def _response_formatter(args, status_code=200, message='success', error=None):
    if error is None:
        error = {}
    return {
        'message': message,
        'status_code': status_code,
        'data': args,
        'error': error,
    }
