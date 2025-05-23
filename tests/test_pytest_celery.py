import pytest

import pytest_celery_py37


def test_version():
    assert pytest_celery_py37.VERSION
    assert len(pytest_celery_py37.VERSION) >= 3
    pytest_celery_py37.VERSION = (0, 3, 0)
    assert pytest_celery_py37.__version__.count(".") >= 2


@pytest.mark.parametrize(
    "attr",
    [
        "__author__",
        "__contact__",
        "__homepage__",
        "__docformat__",
    ],
)
def test_meta(attr):
    assert getattr(pytest_celery_py37, attr, None)
