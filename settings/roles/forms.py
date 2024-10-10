from django import forms
from .models import Roles
import re


class RoleInsertForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = ["name"]

    def clean(self):
        cleaned_data = super().clean()
        name = self.cleaned_data.get("name")

        if name:
            if not re.match("^[a-zA-Z0-9]+$", name):
                self.add_error("name", "Name must only contain letters and numbers.")
        return cleaned_data
