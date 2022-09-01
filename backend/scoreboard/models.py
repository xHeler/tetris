from datetime import timedelta, datetime
from django.conf import settings
from django.db import models


class Score(models.Model):
    author = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    points = models.IntegerField()
    edited_at = models.DateTimeField(auto_now=True)

    def get_ranking_position(self):
        today = datetime.today()
        start_date = today - timedelta(days=today.weekday())
        end_date = today + timedelta(days=-today.weekday(), weeks=1)

        score_list = Score.objects.filter(
            edited_at__range=[start_date, end_date])

        count = score_list.filter(points__gt=self.points).count()
        return count + 1

    def __str__(self):
        return "username: " + self.author.username + ", points: " + str(self.points)

    class Meta:
        ordering = ['-points']
