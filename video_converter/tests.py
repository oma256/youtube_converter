from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):

    def setUp(self) -> None:
        self.video_url = 'https://www.youtube.com/watch?v=-sXw1HJ8SEI'
        self.email = 'oma.dulatov@gmail.com'

    def test_get_request(self):
        url = reverse('video_converter:index')

        r = self.client.get(url)

        self.assertEqual(r.status_code, 200)

    def test_post_request_invalid_data(self):
        url = reverse('video_converter:index')
        payload = {
            'email': self.email
        }

        r = self.client.post(url, payload, HTTP_HOST='0.0.0.0:8000')

        self.assertEqual(r.status_code, 200)

    def test_post_request_valid_data(self):
        url = reverse('video_converter:index')
        payload = {
            'url': self.video_url,
            'email': self.email
        }

        r = self.client.post(url, payload, HTTP_HOST='0.0.0.0:8000')

        self.assertEqual(r.status_code, 200)

