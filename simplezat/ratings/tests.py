from django.urls import reverse
from django.test import TestCase


class RatingViewTest(TestCase):
    def setUp(self):
        self.url = reverse('ratings')

    def test_rating_view_should_have_question_text(self):    
        response = self.client.get(self.url)

        expected = '<h1>How do we do?</h1>'
        self.assertContains(response, expected, status_code=200)

    def test_rating_view_should_show_three_ratings(self): 
        response = self.client.get(self.url)

        expected = '<a href="positive/">' \
            '<img width="200px" src="/static/images/positive.png" alt="Positive"></a>'
        self.assertContains(response, expected, status_code=200)

        expected = '<a href="neutral/">' \
            '<img width="200px" src="/static/images/neutral.png" alt="Neutral"></a>'
        self.assertContains(response, expected, status_code=200)

        expected = '<a href="negative/">' \
            '<img width="200px" src="/static/images/negative.png" alt="Negative"></a>'
        self.assertContains(response, expected, status_code=200)
