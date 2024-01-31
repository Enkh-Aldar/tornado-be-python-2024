from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from .models import Post, Actor, Category, Country, Language

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")
        
    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")
        
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test!")    
        
    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "This is a test!")
        

class ActorTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.actor = Actor.objects.create(text="This is a actor test!")
        
    def test_model_content(self):
        self.assertEqual(self.actor.text, "This is a actor test!")
        
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("actor"))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_correct(self):
        response = self.client.get(reverse("actor"))
        self.assertTemplateUsed(response, "actor.html")

    def test_template_content(self):
        response = self.client.get(reverse("actor"))
        self.assertContains(response, "This is a test!")    
        
    def test_actor(self):
        response = self.client.get(reverse("actor"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "actor.html")
        self.assertContains(response, "This is a test!")
        
class CategoryTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(text="This is a category test!")
        
    def test_model_content(self):
        self.assertEqual(self.category.text, "This is a category test!")
        
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("category"))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_correct(self):
        response = self.client.get(reverse("category"))
        self.assertTemplateUsed(response, "category.html")

    def test_template_content(self):
        response = self.client.get(reverse("category"))
        self.assertContains(response, "This is a test!")    
        
    def test_category(self):
        response = self.client.get(reverse("category"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "category.html")
        self.assertContains(response, "This is a test!")
        
class CountryTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.country = Country.objects.create(text="This is a country test!")
        
    def test_model_content(self):
        self.assertEqual(self.country.text, "This is a country test!")
        
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("country"))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_correct(self):
        response = self.client.get(reverse("country"))
        self.assertTemplateUsed(response, "country.html")

    def test_template_content(self):
        response = self.client.get(reverse("country"))
        self.assertContains(response, "This is a test!")    
        
    def test_country(self):
        response = self.client.get(reverse("country"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "country.html")
        self.assertContains(response, "This is a test!")
        
class LanguageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.language = Language.objects.create(text="This is a language test!")
        
    def test_model_content(self):
        self.assertEqual(self.language.text, "This is a language test!")
        
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("language"))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_correct(self):
        response = self.client.get(reverse("language"))
        self.assertTemplateUsed(response, "language.html")

    def test_template_content(self):
        response = self.client.get(reverse("language"))
        self.assertContains(response, "This is a test!")    
        
    def test_language(self):
        response = self.client.get(reverse("language"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "language.html")
        self.assertContains(response, "This is a test!")