from django.contrib import admin

from .models import Score


class ScoreAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'points',
        'edited_at',
    )

    list_editable = (
        'points',
    )


admin.site.register(Score, ScoreAdmin)
