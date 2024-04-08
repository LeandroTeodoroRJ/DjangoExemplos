from django.contrib import admin
from .models import Condutor, Carro

# Register your models here.
@admin.register(Condutor)
class CondutorAdmin(admin.ModelAdmin):
    pass

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    pass


#Registrando de outro modo
#admin.site.register(Condutor, CondutorAdmin)
#admin.site.register(Carro, CarroAdmin)
