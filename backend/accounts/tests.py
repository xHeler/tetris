from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class CustomUserTest(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(
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
        admin_user = get_user_model().objects.create_superuser(
            username="adminuser",
            email="adminuser@mail.com",
            password="adminpassword123"
        )
        self.assertEqual(admin_user.username, "adminuser")
        self.assertEqual(admin_user.email, "adminuser@mail.com")
        self.assertEqual(admin_user.avatar, "avatar.jpg")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignUpPageTest(TestCase):
    username = "newuser"
    email = "newuser@email.com"

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")

    def test_signup_form(self):
        get_user_model().objects.create_user(
            self.username,
            self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username,
                         self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
