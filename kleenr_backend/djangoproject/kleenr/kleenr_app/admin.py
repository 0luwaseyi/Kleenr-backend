from django.contrib import admin
from django.forms import models

# Register your models here.

from kleenr_app.models import signup, login

admin.site.register(signup)
admin.site.register(login)
