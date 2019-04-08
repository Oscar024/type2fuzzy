import unittest
import numpy as np
from type2fuzzy.membership.type1fuzzyset import Type1FuzzySet


class TestType1FuzzyTest(unittest.TestCase):

    def test_from_representation(self):

        set_representation = '0.1/1 + 0.2/2 + 0.3/3 + 0.4/4'
        t1fs = Type1FuzzySet.from_representation(set_representation)

        self.assertEqual(t1fs[1], 0.1)
        self.assertEqual(t1fs[2], 0.2)
        self.assertEqual(t1fs[3], 0.3)
        self.assertEqual(t1fs[4], 0.4)

    def test_to_representation(self):

        set_representation = '0.1/1.0 + 0.2/2.0 + 0.3/3.0 + 0.4/4.0'
        t1fs = Type1FuzzySet.from_representation(set_representation)

        rep_result = t1fs.__repr__()
        self.assertEqual(rep_result, set_representation)