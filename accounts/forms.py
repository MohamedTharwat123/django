from unicodedata import name
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User
from django import forms
from django.forms import fields


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "User name"}
        )
        self.fields["username"].label = ""

        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Password"}
        )
        self.fields["password1"].label = ""

        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Confirm Password"}
        )
        self.fields["password2"].label = ""

        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None

    email = forms.EmailField(label="")
    first_name = forms.CharField(label="")
    last_name = forms.CharField(label="")

    email.widget.attrs.update({"class": "form-control", "placeholder": "email"})
    first_name.widget.attrs.update(
        {"class": "form-control", "placeholder": "first name"}
    )
    last_name.widget.attrs.update({"class": "form-control", "placeholder": "last name"})

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )


# class SignUpForm(UserCreationForm):
#     username = forms.CharField(
#         forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"})
#     )
#     first_name = forms.CharField(
#         forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
#         max_length=32,
#         help_text="First name",
#     )
#     last_name = forms.CharField(
#         forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
#         max_length=32,
#         help_text="Last name",
#     )
#     email = forms.EmailField(
#         forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
#         max_length=64,
#         help_text="Enter a valid email address",
#     )
#     password1 = forms.CharField(
#         forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
#     )
#     password2 = forms.CharField(
#         forms.PasswordInput(
#             attrs={"class": "form-control", "placeholder": "Password Again"}
#         )
#     )

#     # class Meta(UserCreationForm.Meta):
#     #     model = User
#     #     # I've tried both of these 'fields' declaration, result is the same
#     #     # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
#     #     fields = UserCreationForm.Meta.fields + (
#     #         "first_name",
#     #         "last_name",
#     #         "email",
#     #     )

#     class Meta:
#         model = User
#         fields = (
#             "username",
#             "first_name",
#             "last_name",
#             "email",
#             "password1",
#             "password2",
#         )
