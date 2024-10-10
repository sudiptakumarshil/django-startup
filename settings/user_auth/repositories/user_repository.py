from .user_abstract_repository import UserAbstractRepository


class UserRepository(UserAbstractRepository):
    def register_user(self, data: list) -> object:
        # return data
        raise InterruptedError("LOL")

    def update_user(self, data: list, id: int) -> object:
        return data
