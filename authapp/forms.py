from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from authapp.models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    class Meta:
        pass

