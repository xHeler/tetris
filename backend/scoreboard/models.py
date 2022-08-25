from datetime import timezone,  timedelta, date
from django.conf import settings
from django.db import models


class Score(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        unique=True,
    )
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=False)

    def get_ranking_position(self):
        today = date.today()
        start_date = today - timedelta(days=today.weekday())
        end_date = today + timedelta(days=-today.weekday(), weeks=1)

        score_list = Score.objects.filter(created_at__range=[start_date, end_date])
        
        count = score_list.filter(points__gt=self.points).count()
        return count + 1

    @classmethod
    def create(cls, author, points):
        score = cls(autor=author, points=points, created_at=timezone.now())
        return score

    class Meta:
        ordering = ['-points']
