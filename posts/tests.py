from django.test import TestCase
from .models import Post

# check si ecriture/lecture fonctionne
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='juste un test')
    
    def test_text_content(self):
        post = Post.objects.get(id=1)
        result = 'juste un test'
        post_content = str(post.text)
        self.assertEqual(result, post_content)


# check si l'affichage templates + model fonctionne
class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is post number 1')
        Post.objects.create(text='this is post number 2 ')

    def test_status_ok(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)


# check si on affiche au moins un post
def test_read_one_post(self):
    resp = self.client.get('/')
    self.assertContains(resp, text='this is a post number')


# check si on affiche plusieurs posts
def test_display_list_post(self):
    resp = self.client.get('/')
    self.assertContains(resp, text='cest un post num', count = 2)



# Create your tests here.
