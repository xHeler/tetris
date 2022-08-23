from django.conf import settings
from django.db import models
from django.db.models import Count


class Score(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        unique=True,
    )
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_ranking_position(self):
        count = Score.objects.filter(points__gt=self.points).count()
        return count + 1

    class Meta:
        ordering = ['-points']
