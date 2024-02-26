import pytest
from core.fixtures.user import user
from core.fixtures.post import post
from core.comment.models import Comment


@pytest.mark.django_db
def test_create_comment(user_param, post_param):
    comment = Comment.objects.create(
        author=user_param, post=post_param, body="Test Comment Body"
    )
    assert comment.author == user
    assert comment.post == post
    assert comment.body == "Test Comment Body"
