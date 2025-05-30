from __future__ import annotations

import pytest

from pytest_celery_py37 import MEMCACHED_ENV
from pytest_celery_py37 import MEMCACHED_IMAGE
from pytest_celery_py37 import MEMCACHED_PORTS
from pytest_celery_py37 import MEMCACHED_PREFIX
from pytest_celery_py37 import MemcachedContainer
from pytest_celery_py37 import MemcachedTestBackend


class test_memcached_container:
    def test_version(self):
        assert MemcachedContainer.version() == "latest"

    def test_env(self):
        assert MemcachedContainer.initial_env() == MEMCACHED_ENV

    def test_image(self):
        assert MemcachedContainer.image() == MEMCACHED_IMAGE

    def test_ports(self):
        assert MemcachedContainer.ports() == MEMCACHED_PORTS

    def test_prefix(self):
        assert MemcachedContainer.prefix() == MEMCACHED_PREFIX


class test_memcached_backend_api:
    @pytest.mark.skip(reason="Placeholder")
    def test_placeholder(self, celery_memcached_backend: MemcachedTestBackend):
        # The class MemcachedTestBackend is currently a placeholder
        # so we don't have any specific tests for it yet.
        # This test suite is pre-configured to test the MemcachedTestBackend
        # and ready to be used once the class is implemented.
        pass
