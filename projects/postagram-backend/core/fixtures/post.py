import pytest
from core.fixtures.user import User
from core.post.models import Post


@pytest.fixture
def post(db, user_param):
    return Post.objects.create(author=User, body="Test Post Body")
