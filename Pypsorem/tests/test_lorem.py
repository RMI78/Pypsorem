import unittest
from lorem import Lorem

class TestLorem(unittest.TestCase):

    def test_paragraphs(self):
        lorem = Lorem("paras", 5, True)
        self.assertIsInstance(lorem.__str__(), str)
        self.assertGreater(len(lorem.__str__().split('\n')), 5)
        self.assertEqual(lorem.__str__().split(' ')[0], "Lorem")

    def test_words(self):
        lorem = Lorem("words", 100, False)
        self.assertIsInstance(lorem.__str__(), str)
        self.assertEqual(len(lorem.__str__().split(' ')), 100)

    def test_lists(self):
        lorem = Lorem("lists", 2, True)
        self.assertIsInstance(lorem.__str__(), str)
        self.assertEqual(len(lorem.__str__().split('\n')), 2)

    def test_bytes(self):
        lorem = Lorem("bytes", 500, False)
        self.assertIsInstance(lorem.__str__(), str)
        self.assertEqual(len(lorem.__str__()), 500)

if __name__ == '__main__':
    unittest.main()