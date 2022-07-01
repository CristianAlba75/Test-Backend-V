
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework.test import APITestCase

from .models import Post


class PostsTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()

    def test_add_post_successfully(self):
        """
        Tests add post.
        """
        url = reverse("add_post")
        data = {
            "name": "Post a",
            "content": "Content Post a",
            "email": "user_b@gmail.com"
        }
        response = self.client.post(url, data, format="json")
        post = Post.objects.get(name="Post a")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(post.name, "Post a")
        return post

    def test_add_post_with_missing_parameters(self):
        """
        Tests add post with missing parameters.
        Given: missing content post
        """
        url = reverse("add_post")
        data = {
            "name": "Post a",
            "email": "user_b@gmail.com"
        }
        response = self.client.post(url, data, format="json")
        aux = response.json()
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
        self.assertEqual(aux.get("error"), "Required parameters are missing")

    def test_add_post_with_name_already_exists(self):
        """
        Tests add post with name already exists.
        Given: Post with the same name.
        """
        self.test_add_post_successfully()
        url = reverse("add_post")
        data = {
            "name": "Post a",
            "content": "Content Post a",
            "email": "user_b@gmail.com",
        }
        response = self.client.post(url, data, format="json")
        aux = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(aux.get("error"), "Post already exists")

    def test_add_post_with_invalid_email(self):
        """
        Tests add post with invalid email.
        Given: Invalid email.
        """
        url = reverse("add_post")
        data = {
            "name": "Post a",
            "content": "Content Post a",
            "email": "user_c",
        }
        response = self.client.post(url, data, format="json")
        aux = response.json()
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
        self.assertEqual(aux.get("error"), "Invalid email")

    def test_get_tasks(self):
        """
        Tests get paginated posts.
        """
        self.test_add_post_successfully()
        url = reverse("get_posts",  kwargs={"last_id": 0})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_like_post(self):
        """
        Tests like post.
        """
        post = self.test_add_post_successfully()
        url = reverse("like_post", kwargs={"post_id": post.pk})
        response = self.client.put(url, format="json")
        post.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(post.likes, 1)

    def test_dislike_post(self):
        """
        Tests dislike post.
        """
        post = self.test_add_post_successfully()
        url = reverse("dislike_post", kwargs={"post_id": post.pk})
        response = self.client.put(url, format="json")
        post.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(post.dislikes, 1)
