from datetime import timedelta

from django.utils import timezone
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Score


class ScoreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@mail.com',
            password='testpassword',
        )

        cls.user2 = get_user_model().objects.create_user(
            username='testuser2',
            email='test2@mail.com',
            password='testpassword',
        )

        cls.score = Score.objects.create(
            author=cls.user,
            points=300,
        )

        cls.score2 = Score.objects.create(
            author=cls.user2,
            points=600,
        )

    def test_score_listing(self):
        self.assertEqual(self.score.author.username, 'testuser')
        self.assertEqual(self.score.points, 300)

    def test_player_ranking(self):
        self.assertEqual(self.score2.get_ranking_position(), 1)
        self.assertEqual(self.score.get_ranking_position(), 2)

    def test_score_view_context_pagination(self):
        response = self.client.get(reverse('score_list'))
        self.assertEqual(response.context['page_obj'][0], self.score2)
        self.assertFalse(response.context['page_obj'].has_previous())
        self.assertFalse(response.context['page_obj'].has_next())

    def test_score_view_context_dates(self):
        response = self.client.get(reverse('score_list'))
        today = timezone.now()
        start_date = today - timedelta(days=today.weekday())
        end_date = today + timedelta(days=-today.weekday(), weeks=1)
        self.assertEqual(
            response.context['start_date'].date(),
            start_date.date()
        )
        self.assertEqual(response.context['end_date'].date(), end_date.date())

    def test_score_view_context_recently_results(self):
        response = self.client.get(reverse('score_list'))
        self.assertEqual(response.context['recently_results'][0], self.score2)

    def test_score_view_for_logged_in_user(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse('score_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "scoreboard/score_list.html")
        self.assertEqual(response.context['user_score'], self.score)
        self.assertEqual(response.context['user_position'], 2)

    def test_score_view_for_logged_out_user(self):
        response = self.client.get(reverse('score_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "scoreboard/score_list.html")
