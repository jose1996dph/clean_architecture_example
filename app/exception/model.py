import enum
from fastapi import Response


class HttpException(Exception):
    class StatusCode(enum.Enum):
        bad_request = 400
        not_found = 404
        unprocessable_entity = 422

    def __init__(self, code: StatusCode, description: str):
        self.__code = code
        self.__description = description

    def get_response(self, response: Response):
        response.status_code = self.__code.value
        return self.__description
