from django.test import TestCase
from lewis_structures_app.models import Molecule
from lewis_structures_app.models import Atom


class AtomModelsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create two molecules
        Molecule.objects.create(molecular_formula="H2")
        Molecule.objects.create(molecular_formula="CH4")
        H2 = Molecule.objects.get(molecular_formula="H2")
        CH4 = Molecule.objects.get(molecular_formula="CH4")

        # create atom instances for H2 molecule
        Atom.objects.create(element_symbol="H", molecule=H2, name="H_1")  # H_1
        Atom.objects.create(element_symbol="H", molecule=H2, name="H_2")  # H_2
        # print(Atom.objects.all())

        # create atom instances for CH4 molecule
        Atom.objects.create(element_symbol="H", molecule=CH4, name="H_3")  # H_3
        Atom.objects.create(element_symbol="H", molecule=CH4, name="H_4")  # H_4
        Atom.objects.create(element_symbol="H", molecule=CH4, name="H_5")  # H_5
        Atom.objects.create(element_symbol="H", molecule=CH4, name="H_6")  # H_6
        Atom.objects.create(element_symbol="C", molecule=CH4, name="C_1")  # C_1
        print(Atom.objects.all())

    def setUp(self):
        H_1 = Atom.objects.all()[0]
        H_2 = Atom.objects.all()[1]
        H_1.create_electron_instances()
        H_2.create_electron_instances()

        H_3 = Atom.objects.all()[2]
        H_4 = Atom.objects.all()[3]
        H_5 = Atom.objects.all()[4]
        H_6 = Atom.objects.all()[5]
        C_1 = Atom.objects.all()[6]
        # create electron instances for CH4 molecule
        H_3.create_electron_instances()
        H_4.create_electron_instances()
        H_5.create_electron_instances()
        H_6.create_electron_instances()
        C_1.create_electron_instances()

        print("After resetting electrons or H_1 are: ", H_1.electrons)

    def test_initial_attributes(self):
        """
        initialization of Atom
        """
        
        H_1 = Atom.objects.all()[0]
        print("After resetting electrons or H_1 are: ", H_1.electrons)
        
        

        self.assertTrue(
            H_1.element_symbol
            # == H_2.element_symbol
            # == H_3.element_symbol
            # == H_4.element_symbol
            # == H_5.element_symbol
            # == H_6.element_symbol
            == "H"
        )
        self.assertTrue(len(H_1.electrons) == 1)
        # self.assertTrue(len(C_1.electrons) == 4)

    def test_false_is_false(self):
        H_1 = Atom.objects.all()[0]
        H_1.create_electron_instances()

        C_1 = Atom.objects.get(name="C_1")
        C_1.create_electron_instances()
        print("H_1 =", H_1.name, H_1.atom_id, H_1.electrons)
        print("C_1 =", C_1.name, C_1.atom_id, C_1.electrons)
        self.assertTrue(H_1.element_symbol == "H")
        self.assertTrue(len(H_1.electrons) == 1)
        print(Atom.objects.all()[0].atom_id)
        print(Atom.objects.all()[0].name)
        self.assertFalse(False)

    # def test_false_is_true(self):
    #     print("Method: test_false_is_true.")
    #     self.assertTrue(False)

    # def test_one_plus_one_equals_two(self):
    #     print("Method: test_one_plus_one_equals_two.")
    #     self.assertEqual(1 + 1, 2)
