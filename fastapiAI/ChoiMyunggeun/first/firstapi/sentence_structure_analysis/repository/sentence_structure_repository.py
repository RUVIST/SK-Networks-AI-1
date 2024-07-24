from abc import ABC, abstractmethod


class SentenceStructureAnalysisRepository(ABC):

    @abstractmethod
    def sentenceTokenize(self, sentenceRequest):
        pass