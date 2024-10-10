from .role_abstract_service import (
    RoleAbstractStoreableService,
    RoleAbstractReadableService,
)
from ..repositories.role_repository import RoleRepository


class RoleService(RoleAbstractStoreableService, RoleAbstractReadableService):
    def __init__(self, repository: RoleRepository):
        self.__repository = repository

    def create(self, data: dict):
        return self.__repository.create(data)

    def update(self, data: dict, id: int):
        return self.__repository.update(data, id)

    def read(self, id: int):
        return self.__repository.read(id)

    def reads(self, data: dict = None):
        return self.__repository.reads(data)
