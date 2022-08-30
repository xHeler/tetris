from datetime import date, timedelta

from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Score

def HomePage(request):
    context = {}
    today = date.today()
    start_date = today - timedelta(days=today.weekday())
    end_date = today + timedelta(days=-today.weekday(), weeks=1)
    context['start_date'] = start_date
    context['end_date'] = end_date

    score_list = Score.objects.filter(edited_at__range=[start_date, end_date])
    
    paginator = Paginator(score_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    
    recently_results = score_list.order_by('-edited_at')[:5]
    context['recently_results'] = recently_results

    start_date_last_week = start_date - timedelta(days=7)
    best_score_last_week = Score.objects.filter(
        edited_at__range=[start_date_last_week, start_date]).first()
    if best_score_last_week:
        context['best_score_last_week'] = best_score_last_week

    user_score = None
    user_position = None
    if request.user.is_authenticated and score_list:
        try:
            user_score = score_list.filter(author__username=request.user)[0]
            user_position = score_list.filter(
                points__gt=user_score.points).count() + 1
        except:
            pass
        if user_score:
            context['user_score'] = user_score
            context['user_position'] = user_position

    return render(request, 'scoreboard/score_list.html', context)
