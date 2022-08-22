from django.contrib import admin

from .models import Score


class ScoreAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'points',
        'created_at',
    )


admin.site.register(Score, ScoreAdmin)
