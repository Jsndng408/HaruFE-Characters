from django.contrib import admin
from .models import (
	Role, 
	CharacterSheet, 
	Equipment, 
	Stat, 
	Growth
)

# Register your models here.
admin.site.register(Role)
admin.site.register(CharacterSheet)
admin.site.register(Equipment)
admin.site.register(Stat)
admin.site.register(Growth)