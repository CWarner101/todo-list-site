# Name: Connor Warner
# Class: CIS 218
# Date: 2/7/24

from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoTests(TestCase):
    """Todo Tests"""

    @classmethod
    def setUpTestData(cls):
        """Set up the data needed for each test"""
        cls.todo = Todo.objects.create(name="Thing Todo",
                                       complete_by="2024-02-07")
        
    def test_model_content(self):
        """Test the model content"""
        self.assertEqual(self.todo.name, "Thing Todo")
        self.assertEqual(self.todo.complete_by, "2024-02-07")

    def test_url_exists_at_correct_location(self):
        """Test url exists at correct location"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        """Test the home page"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Thing Todo")
        self.assertContains(response, "Feb. 7, 2024")