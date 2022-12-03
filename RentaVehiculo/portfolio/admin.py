from django.contrib import admin
from .models import Proyect

# Register your models here.
class ProyectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

admin.site.register(Proyect, ProyectAdmin)
