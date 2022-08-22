from django.views.generic import ListView

from .models import Score


class ScoreListView(ListView):
    model = Score
    context_object_name = 'score_list'
    template_name = 'scoreboard/score_list.html'
