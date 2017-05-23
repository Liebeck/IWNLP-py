import logging
import json


class IWNLPWrapper(object):
    def __init__(self, lemmatizer_path='IWNLP.Lemmatizer_20170501.json'):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug('Loading IWNLP lemmatizer')
        self.load(lemmatizer_path)
        self.logger.debug('IWNLP Lemmatizer loaded')

    def load(self, lemmatizer_path):
        """
        This methods load the IWNLP.Lemmatizer json file and creates a dictionary
         of lowercased forms which maps each form to its possible lemmas.
        """
        self.lemmatizer = {}
        with open(lemmatizer_path, encoding='utf-8') as data_file:
            raw = json.load(data_file)
            for entry in raw:
                self.lemmatizer[entry["Form"]] = entry["Lemmas"]

    def contains_entry(self, word, pos=None, ignore_case=False):
        key = word.lower().strip()
        if not pos:
            if ignore_case:
                return key in self.lemmatizer
            else:
                return key in self.lemmatizer and any(filter(lambda x: x["Form"] == word, self.lemmatizer[key]))
        elif not isinstance(pos, list):
            if ignore_case:
                return key in self.lemmatizer and any(filter(lambda x: x["POS"] == pos, self.lemmatizer[key]))
            else:
                return key in self.lemmatizer and any(
                    filter(lambda x: x["POS"] == pos and x["Form"] == word, self.lemmatizer[key]))
        else:
            for pos_entry in pos:
                if self.contains_entry(word, pos_entry, ignore_case):
                    return True
            return False

    def get_entries(self, word, pos=None, ignore_case=False):
        entries = []
        key = word.lower().strip()
        if not pos:
            if ignore_case:
                entries = self.lemmatizer[key]
            else:
                entries = list(filter(lambda x: x["Form"] == word, self.lemmatizer[key]))
        elif not isinstance(pos, list):
            if ignore_case:
                entries = list(filter(lambda x: x["POS"] == pos, self.lemmatizer[key]))
            else:
                entries = list(filter(lambda x: x["POS"] == pos and x["Form"] == word, self.lemmatizer[key]))
        else:
            for pos_entry in pos:
                entries.extend(self.get_lemmas(word, pos_entry, ignore_case))
        return entries

    def get_lemmas(self, word, pos=None, ignore_case=False):
        """
        Return all lemmas for a given word. This method assumes that the specified word is present in the dictionary
        :param word: Word that is present in the IWNLP lemmatizer
        """
        entries = self.get_entries(word, pos, ignore_case)
        lemmas = list(set([entry["Lemma"] for entry in entries]))
        return lemmas

    def lemmatize_plain(self, word, ignore_case=False):
        if self.contains_entry(word, ignore_case=ignore_case):
            return self.get_lemmas(word, ignore_case=ignore_case)
        else:
            return None

    def lemmatize(self, word, pos_universal_google):
        """
        Python port of the lemmatize method, see https://github.com/Liebeck/IWNLP.Lemmatizer/blob/master/IWNLP.Lemmatizer.Predictor/IWNLPSentenceProcessor.cs

        """
        if pos_universal_google == "NOUN":
            if self.contains_entry(word, "Noun"):
                return self.get_lemmas(word, "Noun")
            elif self.contains_entry(word, "X"):
                return self.get_lemmas(word, "X")
            elif self.contains_entry(word, "AdjectivalDeclension"):
                return self.get_lemmas(word, "AdjectivalDeclension")
            elif self.contains_entry(word, ["Noun", "X"], ignore_case=True):
                return self.get_lemmas(word, ["Noun", "X"], ignore_case=True)
            else:
                return None
        elif pos_universal_google == "ADJ":
            if self.contains_entry(word, "Adjective"):
                return self.get_lemmas(word, "Adjective")
            elif self.contains_entry(word, "Adjective", ignore_case=True):
                return self.get_lemmas(word, "Adjective", ignore_case=True)
            # Account for possible errors in the POS tagger. This order was fine-tuned in terms of accuracy
            elif self.contains_entry(word, "Noun", ignore_case=True):
                return self.get_lemmas(word, "Noun", ignore_case=True)
            elif self.contains_entry(word, "X", ignore_case=True):
                return self.get_lemmas(word, "X", ignore_case=True)
            elif self.contains_entry(word, "Verb", ignore_case=True):
                return self.get_lemmas(word, "Verb", ignore_case=True)
            else:
                return None
        elif pos_universal_google == "VERB":
            if self.contains_entry(word, "Verb", ignore_case=True):
                return self.get_lemmas(word, "Verb", ignore_case=True)
            else:
                return None
        else:
            return None
