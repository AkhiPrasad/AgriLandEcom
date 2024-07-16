from django.contrib import admin

from AgrilandApp.models import Category, Product, Orders, Customer, Profile
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Customer)
admin.site.register(Profile)


class ProfileInline(admin.StackedInline):
    model = Profile


# extending user model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "full_name", "email"]
    inlines = [ProfileInline]


# unregister old user method
admin.site.unregister(User)
# reregistering
admin.site.register(User, UserAdmin)

admin.site.site_header = 'AgriLand'
