from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Company

class RegistrationForm(UserCreationForm):
  class Meta:
    model = User
    fields = [
      'first_name',
      'last_name',
      'username',
      'email',
      'password1',
      'password2',
    ]
    
class CompanyRegistrationForm(ModelForm):
  class Meta:
    model = Company
    fields = '__all__'