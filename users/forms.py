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


class SignUpForm(forms.ModelForm):
    class Meta:
        model=models.User
        fields=("first_name","last_name","email")

    passsword = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confiirm Password")

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("passsword1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password
    def save(self, *args, **kwargs):
        user= super().save(commit=False)
        email=self.cleaned_data.get("email")
        password=self.cleaned_data.get("password")
        user.username=email
        user.set_password(password)
        user.save()
