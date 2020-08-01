from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CutomsUserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email','username')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username')