import unittest


class MyTest(unittest.TestCase):
    def test_thing1(self):
        self.assert_(True)

    def test_thing2(self):
        a = None
        self.assertEqual(a, None)
        self.assertEqual(None, a)

    def test_thing2(self):
        a = None
        self.assertEqual(a, True)
        self.assertEqual(True, a)

    def test_thing3(self):
        a = None
        self.assertEqual(a, False)
        self.assertEqual(False, a)

    def test_thing4(self):
        a = 1
        self.assertTrue(a in [1, 2, 3])
        self.assertFalse(a not in [1, 2, 3])
        self.assertIs(a in [1, 2, 3], True)
        self.assertIsNot(a in [1, 2, 3], False)
        self.assertEqual(a in [1, 2, 3], True)

    def test_thing5(self):
        a = 1
        self.assertTrue(a == 1)
        self.assertFalse(a != 1)
        self.assertIs(a == 1, True)
        self.assertIsNot(a == 1, False)
        self.assertEqual(a == 1, True)
