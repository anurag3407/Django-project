from django.contrib import admin

from .models import Tweet

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username', 'content')

# Register your models here.
