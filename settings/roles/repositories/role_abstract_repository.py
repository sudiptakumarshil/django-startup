from abc import ABC, abstractmethod


class RoleAbstractStorableRepository(ABC):
    @abstractmethod
    def create(self, data: dict) -> dict:
        raise NotImplementedError("Create Must implement")

    @abstractmethod
    def update(self, data: dict, id: int) -> dict:
        raise NotImplementedError("Update Must Implement")


class RoleAbstractReadableRepository(ABC):
    @abstractmethod
    def read(self, id: int) -> dict:
        raise NotImplementedError("Read Must Implement")

    @abstractmethod
    def reads(self, condition: dict) -> list:
        raise NotImplementedError("Read Must Implement")
