# coding:utf-8
from django import forms

from user.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname','password','age','icon','sex']
    password2 = forms.CharField(max_length=128)

    def clean_password2(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            raise forms.ValidationError('两次密码输入不一致')
