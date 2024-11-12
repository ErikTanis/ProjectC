import pytest
from test_setup import clear_test_data

@pytest.fixture(scope="session", autouse=True)
def setup():
    clear_test_data()
