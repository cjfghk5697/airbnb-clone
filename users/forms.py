from django import forms
from . import models


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    # clean 이거 쓰면 언제나 지워줌

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.object.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error(
                    "passowrd", form.ValiValidationError("Password is wrong")
                )
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))
