from abc import ABC, abstractmethod


class UserRegisterAbstractRepository(ABC):
    @abstractmethod
    def registerUser(self, data: dict) -> object:
        pass

    def updateUser(self, data: dict, id: int) -> object:
        pass
