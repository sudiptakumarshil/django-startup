from .user_register_abstract_repository import UserRegisterAbstractRepository


class UserRegisterRepository(UserRegisterAbstractRepository):
    def registerUser(self, data: dict) -> object:
        print(data)
        return data

    def updateUser(self, data: dict, id: int) -> object:
        return super().updateUser(data, id)
