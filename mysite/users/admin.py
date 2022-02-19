from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from .models import UserProfile, EmailVerification

from django.contrib.auth.admin import UserAdmin

# cancel registration of native User class
admin.site.unregister(User)


# define the style of related object
class UserProfileInline(admin.StackedInline):
    model = UserProfile


# linked to UserProfile
class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]


# register User mode
admin.site.register(User, UserProfileAdmin)


@admin.register(EmailVerification)
class Admin(admin.ModelAdmin):
    """Admin View for email verification code"""

    list_display = ('code',)
