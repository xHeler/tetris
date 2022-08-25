from datetime import date, timedelta

from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Score


# class ScoreListView(ListView):
#     paginate_by = 10
#     model = Score
#     context_object_name = 'score_list'
#     template_name = 'scoreboard/score_list.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of recently 5 results
#         context['recently_results'] = Score.objects.all().order_by(
#             '-created_at')[:5]
#         # Add best player
#         context['best_score'] = Score.objects.first()
#         # Add personal stats
#         if self.request.user.is_authenticated:
#             context['user_score'] = Score.objects.filter(
#                 author__username=self.request.user)[0]
#             context['user_position'] = Score.objects.filter(
#                 points__gt=context['user_score'].points).count() + 1
#         return context


def HomePage(request):
    today = date.today()
    start_date = today - timedelta(days=today.weekday())
    end_date = today + timedelta(days=-today.weekday(), weeks=1)

    score_list = Score.objects.filter(created_at__range=[start_date, end_date])
    paginator = Paginator(score_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    recently_results = score_list.order_by('-created_at')[:5]

    start_date_last_week = start_date - timedelta(days=7)
    end_date_last_week = start_date - timedelta(days=7)
    best_score_last_week = Score.objects.filter(
        created_at__range=[start_date_last_week, end_date_last_week]).first()

    if request.user.is_authenticated:
        user_score = Score.objects.filter(author__username=request.user)[0]
        user_position = Score.objects.filter(
            points__gt=user_score.points).count() + 1

    context = {'page_obj': page_obj,
        'start_date': start_date, 'end_date': end_date,
               'score_list': score_list, 'recently_results': recently_results,
               'best_score_last_week': best_score_last_week,
               'user_score': user_score, 'user_position': user_position}

    return render(request, 'scoreboard/score_list.html', context)
