import spacy
from nltk import sent_tokenize, word_tokenize

from sentence_structure_analysis.repository.sentence_structure_repository import SentenceStructureAnalysisRepository


class SentenceStructureAnalysisRepositoryImpl(SentenceStructureAnalysisRepository):

    def sentenceTokenize(self, text):
        print(f'repository -> sentenceTokenize(): {text}')
        return sent_tokenize(text)