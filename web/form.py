#coding=utf-8
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密__码',widget=forms.PasswordInput())