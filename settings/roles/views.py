from django.shortcuts import render
from django.views import View
from .forms import RoleInsertForm
from django.http import JsonResponse
from .repositories.role_repository import RoleRepository
from .services.role_service import RoleService
import json


class StoreRoleView(View):
    def __init__(self, role_service=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role_service = role_service or RoleService(repository=RoleRepository())

    def get(self, request):
        return render(request, "create_update.html")

    def post(self, request):
        data = json.loads(request.body)
        data["user"] = request.user
        form = RoleInsertForm(data)
        if form.is_valid():
            try:
                if data["id"] is not None or "":
                    role = self.role_service.update(data, data["id"])
                else:
                    role = self.role_service.create(data)
                return JsonResponse(role)
            except Exception as e:
                return JsonResponse({"success": False, "errors": str(e)}, status=500)

        errors = form.errors.as_json()
        return JsonResponse({"success": False, "errors": errors}, status=400)


class RoleListView(View):
    def __init__(self, role_service=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role_service = role_service or RoleService(repository=RoleRepository())

    def get(self, request):
        context = {}
        context["data"] = self.role_service.reads()
        print(context)
        return render(request, "list.html", context)

    def post(self, request):
        return request
