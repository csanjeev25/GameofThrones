from django.test import TestCase
from django.core.urlresolvers import reverse
from django.urls import reverse
from .views import index,house,character
from .models import Character,House,Battle

# Create your tests here.
class IndexTests(TestCase):
	def test_index_view_status_code(self):
		url = reverse('index')
		response = self.client.get(url)
		self.assertEquals(response.status_code,200)

	def test_index_url_resolves_index_view(self):
		view = resolve('/')
		self.assertEquals(view.func,index)

class CharacterTests(TestCase):
	def setUp(self):
		Character.objects.create(name="Lord Eddard Stark",image='''https://vignette.wikia.nocookie.net/gameofthrones/images/3/37/Eddard_Stark_infob
ox_new.jpg/revision/latest?cb=20160730050722''')

	def test_character_view_success_status_code(self):
		url = reverse('character',kwargs={'pk':1})
		response = self.client.get(url)
		self.assertEquals(response.status_code,200)

	def test_character_not_found_status_code(self):
		url = reverse('character',kwargs={'pk':99})
		response = self.client.get(url)
		self.assertEquals(response.status_code,404)

	def test_character_url_resolves_character_view(self):
		view = resolve('/character/1/')
		self.assertEquals(view.func,character)