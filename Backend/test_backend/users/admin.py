from django.contrib import admin
from users.models import User, Group


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass
