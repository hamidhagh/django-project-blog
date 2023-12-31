import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestPostSingle:
    def test_single_post_url(self, client, post_factory):
        post = post_factory()
        url = reverse("single-post", kwargs={"post": post.slug})
        response = client.get(url)
        assert response.status_code == 200
