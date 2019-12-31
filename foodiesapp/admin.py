from django.contrib import admin
from .models import  Meal,Food,BEVERAGES,COMBOS,Slider,Gallery

# Register your models here.



# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    pass









admin.site.register(Meal)
admin.site.register(Food)
admin.site.register(BEVERAGES)
admin.site.register(COMBOS)


admin.site.register(Slider)

admin.site.register(Gallery)