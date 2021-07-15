from django.models import models
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=%{2:254})

    class Meta:
        model = User
        fields = 
