from abc import ABC, abstractmethod


class RoleAbstractStoreableService(ABC):
    @abstractmethod
    def create(self, data: dict):
        raise NotImplementedError("Create must implement")

    @abstractmethod
    def update(self, data: dict, id: int):
        raise NotImplementedError("Update must implement")


class RoleAbstractReadableService(ABC):
    @abstractmethod
    def reads(self, data: dict):
        raise NotImplementedError("Reads must implement")

    @abstractmethod
    def read(self, id: int):
        raise NotImplementedError("Read must implement")
