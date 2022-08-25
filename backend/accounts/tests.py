from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="test",
            email="test@mail.com",
            password="testpassword1"
        )
        self.assertEqual(user.username, "test")
        self.assertEqual(user.email, "test@mail.com")
        self.assertEqual(user.avatar, "avatar.jpg")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="adminuser", email="adminuser@mail.com", password="adminpassword123"
        )
        self.assertEqual(admin_user.username, "adminuser")
        self.assertEqual(admin_user.email, "adminuser@mail.com")
        self.assertEqual(admin_user.avatar, "avatar.jpg")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
