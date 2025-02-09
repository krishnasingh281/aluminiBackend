from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'student_id', 'graduation_year', 'major', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('graduation_year', 'major', 'student_id')}),
    )
