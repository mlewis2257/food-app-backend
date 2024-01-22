from django.test import TestCase
from .models import Food


# Create your tests here.

class FoodModelTest(TestCase): 
    def setUp(self): 
        Food.objects.create(title='risotto', description='italian', completed=False)
        Food.objects.create(title='pho', description='vietnamese', completed=True)

    def test_food_content(self):
        risotto = Food.objects.get(title='risotto')
        pho = Food.objects.get(title='pho')
        self.assertEqual(risotto.description, 'italian')
        self.assertEqual(pho.completed, True)