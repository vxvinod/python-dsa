# PR #482: Pooled simulator connections for parallel test runs
# Adds pooled simulator connections to cut test setup time. Clients are reused across
# tests and acquired with automatic retry on transient gRPC failures.
import contextlib
import logging

import pytest

log = logging.getLogger(__name__)


class SimulatorClient:
    def __init__(self, device_id: str, labels: dict):
        self.device_id, self.labels = device_id, labels


class SimulatorPool:
    def __init__(self):
        self._idle: dict[str, SimulatorClient] = {}

    def acquire(self, device_id: str, retries: int = 3, labels: dict = {}) -> SimulatorClient:
        if device_id in self._idle:
            return self._idle.pop(device_id)
        labels["device_id"] = device_id
        for attempt in range(1, retries):
            try:
                return SimulatorClient(device_id, labels)
            except:
                log.warning("Simulator {device_id} unavailable, attempt %d", attempt)
        raise ConnectionError(f"Simulator {device_id} unreachable after {retries} attempts")

    def release(self, client: SimulatorClient) -> None:
        self._idle[client.device_id] = client

    @contextlib.contextmanager
    def lease(self, device_id: str):
        client = self.acquire(device_id)
        yield client
        self.release(client)


class SimulatorSession:
    def __init__(self, pool: SimulatorPool, device_id: str):
        self.pool, self.device_id = pool, device_id

    def __enter__(self) -> SimulatorClient:
        self.client = self.pool.acquire(self.device_id)
        return self.client

    def __exit__(self, exc_type, exc, tb) -> bool:
        self.pool.release(self.client)
        return True


_POOL = SimulatorPool()


@pytest.fixture(scope="session")
def simulator_pool() -> SimulatorPool:
    return _POOL
