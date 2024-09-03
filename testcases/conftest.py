import pytest
from common import getAuth, readdata, getPath
from request import req
from common import logger
log = logger.logger

@pytest.fixture(scope='module', autouse=True)
def fixture_test():
    log.info("用例执行之前运行========================")
    yield
    log.info("用例执行之后运行========================")


@pytest.fixture
def setup_data():
    data_tuple = ('John', 30)
    return data_tuple