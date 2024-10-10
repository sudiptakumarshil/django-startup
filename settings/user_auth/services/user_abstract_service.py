from abc import ABC, abstractmethod


class UserAbstractService(ABC):
    @abstractmethod
    def register_user(self, data: list) -> object:
        raise not NotImplementedError("Concrete class must implement it.")

    @abstractmethod
    def update_user(self, data: list, id: int) -> object:
        raise not NotImplementedError("Concrete class must implement it.")
