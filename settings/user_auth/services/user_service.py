from .user_abstract_service import UserAbstractService
from ..repositories.user_repository import UserRepository


class UserService(UserAbstractService):
    def __init__(self, repository: UserRepository):
        self.__repository = repository

    def register_user(self, data: list) -> object:
        return self.__repository.register_user(data)

    def update_user(self, data: list, id: int) -> object:
        return self.__repository.update_user(data, id)
