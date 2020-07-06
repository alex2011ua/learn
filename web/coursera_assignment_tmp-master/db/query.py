from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from db.models import User, Blog, Topic


def create():
    user1 = User(first_name='u1', last_name='u1')
    user1.save()
    user2 = User(first_name='u2', last_name='u2')
    user2.save()
    user3 = User(first_name='u3', last_name='u3')
    user3.save()
    blog1 = Blog(title='blog1', author='u1')
    blog1.save()
    blog2 = Blog(title='blog2', author='u1')
    blog2.save()
    blog1.subscribers = user1, user2
    blog1.save()
    blog2.subscribers = user2
    blog2.save()
    topic1 = Topic(title='topic1', blog=blog1, author=u1)
    topic1.save()
    topic2 = Topic(title='topic2_content', blog = blog1, author = user3, created = '2017-01-01')
    topic2.save()
    topic1.likes = user1, user2, user3
    topic1.save()

def edit_all():
    all_user = User.objects.all()
    for user in all_user:
        user.first_name = 'uu1'


def edit_u1_u2():
    pass


def delete_u1():
    pass


def unsubscribe_u2_from_blogs():
    pass


def get_topic_created_grated():
    pass


def get_topic_title_ended():
    pass


def get_user_with_limit():
    pass


def get_topic_count():
    pass


def get_avg_topic_count():
    pass


def get_blog_that_have_more_than_one_topic():
    pass


def get_topic_by_u1():
    pass


def get_user_that_dont_have_blog():
    pass


def get_topic_that_like_all_users():
    pass


def get_topic_that_dont_have_like():
    pass
