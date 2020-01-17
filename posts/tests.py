from django.test import TestCase
from django.contrib.auth.models import User

from posts.models import Post


class BlogTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        #create user
        testuser1 = User.objects.create_user(
            username = 'testuser', password='abc123'
        ) 
        testuser1.save()

        test_post = Post.objects.create(
            author=testuser1, title='Blog Title', body='some post'
        )

        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(pk=1)
        expected_author = f'{post.author}'
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'
        self.assertEqual(expected_author, 'testuser')
        self.assertEqual(expected_title, 'Blog Title')
        self.assertEqual(expected_body, 'some post')
     
