# IWNLP-py
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/Liebeck/IWNLP-py/master/LICENSE.md)
[![Build Status](https://api.travis-ci.org/Liebeck/IWNLP-py.svg?branch=master)](https://travis-ci.com/Liebeck/IWNLP-py)

IWNLP-py is a Python port of [IWNLP.Lemmatizer](https://github.com/Liebeck/IWNLP.Lemmatizer). IWNLP-py offers a lemmatization of German words based on the [German Wiktionary](https://de.wiktionary.org/wiki) which is processed by [IWNLP](https://github.com/Liebeck/IWNLP).

# How to setup IWNLP-py
1. Use pip to install iwnlp
``` bash
pip install iwnlp
```
2. Download the latest processed IWNLP dump from http://lager.cs.uni-duesseldorf.de/NLP/IWNLP/IWNLP.Lemmatizer_20170501.zip and unzip it.


# How to use IWNLP-py
The Python package consists of the *IWNLPWrapper* class. Keep in mind that the lemmatizer will return *None* for unknown words rather than guessing a lemma. If more than one lemma is found, all lemmas are returned. In order to lemmatize single words, you can choose between two functions:
1. *lemmatize*: If you have access to POS tags of your words, you should use this function. The POS tagset is [Google's universal POS tagset](http://universaldependencies.org/u/pos/). The lemmatization performance is tuned to be as high as possible, as listed [here](http://www.iwnlp.com/iwnlp_results.html). [Our paper](http://www.aclweb.org/anthology/P15-2068) describes our approach in more detail. Keep in mind, that our results have much improved over the last two years.
``` python
def lemmatize(self, word, pos_universal_google)
```
Usage:
``` python
from iwnlp.iwnlp_wrapper import IWNLPWrapper
lemmatizer = IWNLPWrapper(lemmatizer_path='data/IWNLP.Lemmatizer_20170501.json')
lemmatizer.lemmatize('Lkws', pos_universal_google='NOUN')
# ['Lkw']
lemmatizer.lemmatize('Onlineauftritten', pos_universal_google='NOUN')
# ['Onlineauftritt']
lemmatizer.lemmatize('gespielt', pos_universal_google='VERB')
# ['spielen']
```

2. *lemmatize*: If you don't have access to POS tags or don't want to use them you can simply pass the word without any POS tag and retrieve any lemma that is present in IWNLP. You may also specify if you want the lookup to be **case sensitive**, which it is by default.
``` python
def lemmatize_plain(self, word, ignore_case=False):
```

Usage:
``` python
from iwnlp.iwnlp_wrapper import IWNLPWrapper
lemmatizer = IWNLPWrapper(lemmatizer_path='data/IWNLP.Lemmatizer_20170501.json')
lemmatizer.lemmatize_plain('birne')
# no result since the noun is lowercased
lemmatizer.lemmatize_plain('birne', ignore_case=True)
# ['Birne']
lemmatizer.lemmatize_plain('zerstreut', ignore_case=True)
# ['zerstreut', 'zerstreuen']
```

# Citation
Please include the following BibTeX if you use IWNLP in your work:
``` bash
@InProceedings{liebeck-conrad:2015:ACL-IJCNLP,
  author    = {Liebeck, Matthias  and  Conrad, Stefan},
  title     = {{IWNLP: Inverse Wiktionary for Natural Language Processing}},
  booktitle = {Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 2: Short Papers)},
  year      = {2015},
  publisher = {Association for Computational Linguistics},
  pages     = {414--418},
  url       = {http://www.aclweb.org/anthology/P15-2068}
}
```