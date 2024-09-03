import os.path

import pytest

from common import logger
from request import req
from common import getAuth

log = logger.logger

class TestHandcards:

    def test_createHandcard(self):
        auth = getAuth.createAuth()
        log.info(auth)
        req.send_request_from_yaml('tuwen.yaml', auth)

    # def test_product_rank_tuwen(self):
    #     response = req.send_request_from_yaml('tuwen.yaml', self.auth)
    #     log.info(response)

# if __name__ == '__main__':
#     TestHandcards.test_createHandcard()

    @pytest.mark.parametrize("name, age", [pytest.param(*pytest.fixture.getfixturevalue('setup_data'), id='parametrize_test')])
    def test_example(name, age):
        assert isinstance(name, str)
        assert isinstance(age, int)