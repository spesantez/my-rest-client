from unittest.mock import sentinel

import pytest

from my_rest_client.error_handlers import BaseErrorHandler
from my_rest_client.response import RequestsResponse


class TestBaseExceptionHandler:
    handler = BaseErrorHandler

    def test_get_exception_needs_implementation(self):
        with pytest.raises(NotImplementedError):
            self.handler.get_exception(RequestsResponse(sentinel.response))
