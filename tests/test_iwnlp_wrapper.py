import unittest
from iwnlp.iwnlp_wrapper import IWNLPWrapper


class IWNLPWrapperTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.iwnlp = IWNLPWrapper(lemmatizer_path='data/IWNLP.Lemmatizer_20170501.json')

    def test_lemmatize_plain_example1(self):
        predicted = self.iwnlp.lemmatize_plain('Hallo')
        self.assertEqual(predicted, ['Hallo'])

    def test_lemmatize_plain_example2(self):
        predicted = self.iwnlp.lemmatize_plain('Hallo', ignore_case=False)
        self.assertEqual(predicted, ['Hallo'])

    def test_lemmatize_plain_example3(self):
        predicted = self.iwnlp.lemmatize_plain('birne', ignore_case=False)
        self.assertEqual(predicted, None)

    def test_lemmatize_plain_example4(self):
        predicted = self.iwnlp.lemmatize_plain('birne', ignore_case=True)
        self.assertEqual(predicted, ['Birne'])

    def test_lemmatize_plain_example5(self):
        predicted = self.iwnlp.lemmatize_plain('gespielt')
        self.assertEqual(predicted, ['spielen'])

    def test_lemmatize_plain_example6(self):
        predicted = self.iwnlp.lemmatize_plain('schnell')
        self.assertCountEqual(predicted, ['schnellen', 'schnell'])

    def test_lemmatize_plain_example7(self):
        predicted = self.iwnlp.lemmatize_plain('Gartenhäuser')
        self.assertEqual(predicted, ['Gartenhaus'])

    def test_contains_entry_example1(self):
        self.assertEqual(self.iwnlp.contains_entry('Birne'), True)

    def test_contains_entry_example2(self):
        self.assertEqual(self.iwnlp.contains_entry('birne', ignore_case=False), False)

    def test_contains_entry_example3(self):
        self.assertEqual(self.iwnlp.contains_entry('birne', ignore_case=True), True)
