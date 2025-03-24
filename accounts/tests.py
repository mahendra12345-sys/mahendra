from django.test import TestCase

# Create your tests here.

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class UserAuthTestCase(TestCase):

    def setUp(self):
        """Set up test user before running tests."""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='Test@123')

    def test_registration_success(self):
        """Test if user registration works successfully."""
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'Test@1234',
            'password2': 'Test@1234'
        })
        self.assertEqual(response.status_code, 200)  # Ensure page loads
        self.assertTrue(User.objects.filter(username='newuser').exists())  # Check if user exists

    def test_registration_password_mismatch(self):
        """Test if registration fails when passwords do not match."""
        response = self.client.post(reverse('register'), {
            'username': 'mismatchuser',
            'email': 'mismatch@example.com',
            'password1': 'Test@123',
            'password2': 'WrongPassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='mismatchuser').exists())  # User should not be created

    def test_login_success(self):
        """Test if user can log in successfully."""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'Test@123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login
        self.assertRedirects(response, reverse('dashboard'))  # Ensure it redirects to dashboard

    def test_login_invalid_credentials(self):
        """Test if login fails with incorrect credentials."""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'WrongPassword'
        })
        self.assertEqual(response.status_code, 200)  # Stay on login page
        self.assertContains(response, "Invalid credentials!")  # Check error message

    def test_logout(self):
        """Test if user can log out successfully."""
        self.client.login(username='testuser', password='Test@123')  # Log in first
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect after logout
        self.assertRedirects(response, reverse('login'))  # Ensure it redirects to login page

    def test_dashboard_access_without_login(self):
        """Test if dashboard is inaccessible without login."""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)  # Should redirect to login page
        self.assertRedirects(response, reverse('login') + '?next=/accounts/dashboard/')

    def test_dashboard_access_with_login(self):
        """Test if dashboard is accessible when logged in."""
        self.client.login(username='testuser', password='Test@123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)  # Should load dashboard page
        self.assertContains(response, "Welcome, testuser!")  # Check if username is displayed
