from __future__ import annotations

import pytest

from pytest_celery_py37 import REDIS_ENV
from pytest_celery_py37 import REDIS_IMAGE
from pytest_celery_py37 import REDIS_PORTS
from pytest_celery_py37 import REDIS_PREFIX
from pytest_celery_py37 import RedisContainer
from pytest_celery_py37 import RedisTestBackend
from pytest_celery_py37 import RedisTestBroker


class test_redis_container:
    def test_version(self):
        assert RedisContainer.version() == "latest"

    def test_env(self):
        assert RedisContainer.initial_env() == REDIS_ENV

    def test_image(self):
        assert RedisContainer.image() == REDIS_IMAGE

    def test_ports(self):
        assert RedisContainer.ports() == REDIS_PORTS

    def test_prefix(self):
        assert RedisContainer.prefix() == REDIS_PREFIX


class test_redis_backend_api:
    @pytest.mark.skip(reason="RedisTestBackend.teardown() breaks the testing environment")
    def test_teardown(self, celery_redis_backend: RedisTestBackend):
        celery_redis_backend.teardown()
        celery_redis_backend.container.teardown.assert_called_once()


class test_redis_broker_api:
    @pytest.mark.skip(reason="Placeholder")
    def test_placeholder(self, celery_redis_broker: RedisTestBroker):
        # The class RedisTestBroker is currently a placeholder
        # so we don't have any specific tests for it yet.
        # This test suite is pre-configured to test the RedisTestBroker
        # and ready to be used once the class is implemented.
        pass
