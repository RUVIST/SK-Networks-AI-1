from abc import ABC, abstractmethod


class TransitionLearningRepository(ABC):
    @abstractmethod
    def prepareBertBaseUncasedLearningSet(self):
        pass

    @abstractmethod
    def prepareBertBaseMultilingualUncasedSentimentLearningSet(self):
        pass
