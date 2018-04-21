from django.contrib import admin
from .models import Character
from .models import House
from .models import Battle

# Register your models here.
admin.site.register(Character)
admin.site.register(House)
admin.site.register(Battle)
