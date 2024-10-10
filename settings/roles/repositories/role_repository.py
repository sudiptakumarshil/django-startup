from .role_abstract_repository import (
    RoleAbstractStorableRepository,
    RoleAbstractReadableRepository,
)
from ..models import Roles
from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict
from django.db import transaction
from django.shortcuts import get_object_or_404


class RoleRepository(RoleAbstractStorableRepository, RoleAbstractReadableRepository):
    def create(self, data: dict) -> dict:
        try:
            with transaction.atomic():
                role = Roles()
                role.name = data["name"]
                role.admin = data["user"]
                role.full_clean()
                role.save()
                return model_to_dict(role)
        except KeyError as e:
            raise ValueError(f"Missing required field: {e}")
        except ValidationError as e:
            raise ValueError(f"Validation error: {e.messages}")

    def update(self, data: dict, id: int) -> dict:
        try:
            with transaction.atomic():
                role = get_object_or_404(Roles, id=id)
                role.name = data["name"]
                role.admin = data["user"]
                role.full_clean()
                role.save()
                return model_to_dict(role)
        except KeyError as e:
            raise ValueError(f"Missing required field: {e}")
        except ValidationError as e:
            raise ValueError(f"Validation error: {e.messages}")

    def read(self, id: int) -> dict:
        return get_object_or_404(Roles, id=id)

    def reads(self, condition: dict = None) -> list:
        if not condition:
            return list(Roles.objects.prefetch_related("admin").all().values())

        return list(
            Roles.objects.prefetch_related("admin").filter(**condition).values()
        )
