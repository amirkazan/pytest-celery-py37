import pytest
from celery.canvas import Signature
from celery.result import AsyncResult

from pytest_celery_py37 import RESULT_TIMEOUT
from pytest_celery_py37 import CeleryTestSetup
from pytest_celery_py37 import CeleryTestWorker
from pytest_celery_py37 import CeleryWorkerCluster
from pytest_celery_py37 import ping


@pytest.fixture
def celery_worker_cluster(
    celery_worker: CeleryTestWorker,
    myworker_worker: CeleryTestWorker,
) -> CeleryWorkerCluster:
    """Add myworker worker to the workers cluster alongside the parametrize
    plugin worker."""
    cluster = CeleryWorkerCluster(celery_worker, myworker_worker)  # type: ignore
    yield cluster
    cluster.teardown()


def test_ping(celery_setup: CeleryTestSetup):
    """Test ping task for each worker node."""
    worker: CeleryTestWorker
    for worker in celery_setup.worker_cluster:
        sig: Signature = ping.s()
        res: AsyncResult = sig.apply_async(queue=worker.worker_queue)
        assert res.get(timeout=RESULT_TIMEOUT) == "pong"
