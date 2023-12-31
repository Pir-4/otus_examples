import pytest

# doc https://docs.pytest.org/en/7.1.x/example/simple.html
def pytest_addoption(parser):
    parser.addoption(
        "--actual", help="Actual value"
    )

    parser.addoption(
        "--expected", default=200, type=int, help="Expected value"
    )


@pytest.fixture
def actual(request):
    return request.config.getoption("--actual")


@pytest.fixture
def expected(request):
    return request.config.getoption("--expected")