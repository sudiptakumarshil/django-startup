from abc import ABC, abstractmethod


class UserAbstractRepository(ABC):
    @abstractmethod
    def register_user(self, data: list) -> object:
        raise NotImplementedError("Concrete class must implement it")

    @abstractmethod
    def update_user(self, data: list, id: int) -> object:
        raise NotImplementedError("Concrete class must implement it")
