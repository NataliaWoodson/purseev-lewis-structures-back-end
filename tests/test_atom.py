from django.test import TestCase
from lewis_structures_app.models import Molecule
from lewis_structures_app.models import Atom
from lewis_structures_app.models import Electron

class AtomModelsTests(TestCase):
    # def test_initial_attributes(self):
    #     """
    #     initialization of Atom 
    #     """

    @classmethod
    def setUpTestData(cls):
        H2 = Molecule(moecular_formula="H2")

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)