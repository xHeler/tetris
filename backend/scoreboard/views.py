from datetime import timedelta
from django.utils import timezone
from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Score


def home_page(request):
    context = {}

    start_date, end_date = get_last_and_next_mondays_date()
    context['start_date'] = start_date
    context['end_date'] = end_date

    score_list = Score.objects.filter(edited_at__range=[start_date, end_date])
    context['page_obj'] = create_pagination(request, score_list, 10)
    context['recently_results'] = score_list.order_by('-edited_at')[:5]

    context['best_score_last_week'] = get_best_score(
        Score.objects,
        start_date - timedelta(days=7),
        start_date
    )

    if request.user.is_authenticated and score_list:
        user_score = score_list.filter(author__username=request.user).first()
        user_position = score_list.filter(
            points__gt=user_score.points).count() + 1
        if user_score and user_position:
            context['user_score'] = user_score
            context['user_position'] = user_position

    return render(request, 'scoreboard/score_list.html', context)


def get_last_and_next_mondays_date():
    today = timezone.now()
    monday = today - timedelta(days=today.weekday())
    next_monday = today + timedelta(days=-today.weekday(), weeks=1)
    return monday, next_monday


def create_pagination(request, objects, amount_of_items):
    paginator = Paginator(objects, amount_of_items)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def get_best_score(objects, start_date, end_date):
    return objects.filter(
        edited_at__range=[start_date, end_date]
    ).first()
