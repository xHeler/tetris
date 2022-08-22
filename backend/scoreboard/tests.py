from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Score


class ScoreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@mail.com',
            password='testpassword',
        )

        cls.score = Score.objects.create(
            author=cls.user,
            points=300,
        )

    def test_post_model(self):
        self.assertEqual(self.score.author.username, 'testuser')
        self.assertEqual(self.score.points, 300)
