from django.contrib import admin
from .models import User


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ['image_b64']
    fields = (
        ('imagem', 'image_tag',), ('username', 'password', 'last_login'), ('nome', 'email'),
        ('is_active', 'is_superuser'),)
        # ('groups', 'user_permissions'))
    readonly_fields = ('image_tag',)
