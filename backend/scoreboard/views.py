from django.views.generic import ListView

from .models import Score


class ScoreListView(ListView):
    paginate_by = 10
    model = Score
    context_object_name = 'score_list'
    template_name = 'scoreboard/score_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of recently 5 results
        context['recently_results'] = Score.objects.all().order_by('-created_at')[:5]
        # Add best player
        context['best_score'] = Score.objects.first()
        return context