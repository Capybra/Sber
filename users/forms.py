from users.models import Profile
from django.db import models
from django import forms
from django.forms import (ModelForm, TextInput, DateTimeInput, 
                          PasswordInput, EmailInput)


class RegistrationForm(ModelForm):
    password = forms.CharField(label="Пароль")
    password_confirmation = forms.CharField(label="Подтвердите пароль")
    class Meta:
        model = Profile
        fields = ["name", "surname", "lastname", "sex",
                  "birthdate", "email", "password", "password_confirmation"]
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control input-lg",
                "default": "",
            }),
            "surname": TextInput(attrs={
                "class": "form-control input-lg",
                "value": "",
            }),
            "lastname": TextInput(attrs={
                "class": "form-control input-lg",
                "value": "",
            }),
            "sex": forms.Select(attrs={
                "class": "form-control"
            }),
            "birthdate": DateTimeInput(attrs={
                "class": "form-control",
                "value": "",
            }),
            "email": EmailInput(attrs={
                "class": "form-control",
                "default": "",
            }),
            "password": PasswordInput(attrs={
                "class": "form-control input-lg",
            }),
            "password_confirmation": PasswordInput(attrs={
                "class": "form-control input-lg",
            })
        }


class LoginForm(ModelForm):
    password = forms.CharField(label="Пароль")
    class Meta:
        model = Profile
        fields = ["email", "password"]
        widgets = {
            "email": EmailInput(attrs={
                "class": "form-control"
            }),
            "password": PasswordInput(attrs={
                "class": "form-control input-lg",
            }),
        }
