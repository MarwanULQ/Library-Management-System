from threading import Lock
from typing import Any, Dict

class Cache:
    _instance = None
    _lock = Lock()
    _store: Dict[str, Any]

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:                
                cls._instance = super().__new__(cls)
                cls._instance._store = {}
        return cls._instance

    def get(self, key: str, default=None):
        return self._store.get(key, default)

    def set(self, key: str, value: Any):
        self._store[key] = value

    def delete(self, key: str):
        self._store.pop(key, None)

    def clear(self):
        self._store.clear()