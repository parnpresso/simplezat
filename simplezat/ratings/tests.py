from django.urls import reverse
from django.test import TestCase


class RatingViewTest(TestCase):
    def setUp(self):
        self.url = reverse('ratings')

    def test_rating_view_should_be_accessible(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_rating_view_should_have_question_text(self):    
        response = self.client.get(self.url)

        expected = '<h1>How do we do?</h1>'
        self.assertContains(response, expected, status_code=200)

