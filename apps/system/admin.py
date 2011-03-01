from django.contrib import admin
from system.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
	search_fields = ("user",)
	
admin.site.register(UserProfile, UserProfileAdmin)
