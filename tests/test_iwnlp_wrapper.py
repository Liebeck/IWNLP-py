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

    def test_contains_entry_example4(self):
        self.assertEqual(self.iwnlp.contains_entry('groko'), False)

    def test_contains_entry_example5(self):
        self.assertEqual(self.iwnlp.contains_entry('GroKo'), True)

    def test_contains_entry_example6(self):
        self.assertEqual(self.iwnlp.contains_entry('groko', ignore_case=True), True)

    def test_contains_entry_example7(self):
        self.assertEqual(self.iwnlp.contains_entry('groko', pos='Noun'), False)

    def test_contains_entry_example8(self):
        self.assertEqual(self.iwnlp.contains_entry('groko', pos='X'), False)

    def test_contains_entry_example9(self):
        self.assertEqual(self.iwnlp.contains_entry('groko', pos='AdjectivalDeclension'), False)

    def test_contains_entry_example10(self):
        self.assertEqual(self.iwnlp.contains_entry('groko', pos=["Noun", "X"], ignore_case=True), True)

    def test_lemmatize_example1(self):
        predicted = self.iwnlp.lemmatize('Lkws', pos_universal_google='NOUN')
        self.assertEqual(predicted, ['Lkw'])

    def test_lemmatize_example2(self):
        predicted = self.iwnlp.lemmatize('gespielt', pos_universal_google='VERB')
        self.assertEqual(predicted, ['spielen'])

    def test_get_lemmas_example1(self):
        predicted = self.iwnlp.get_lemmas('groko', pos=["Noun", "X"], ignore_case=True)
        self.assertEqual(predicted, ['GroKo'])
