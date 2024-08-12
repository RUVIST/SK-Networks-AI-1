from transition_learning.repository.transition_learning_repository import TransitionLearningRepository
from transformers import BertTokenizer, BertForSequenceClassification, GPT2Tokenizer, GPT2LMHeadModel


class TransitionLearningRepositoryImpl(TransitionLearningRepository):
    MODEL_NAME_GPT2 = "gpt2"
    MODEL_NAME_BERT_BASE_UNCASED = "bert-base-uncased"
    MODEL_NAME_BERT_BASE_MULTILINGUAL_UNCASED_SENTIMENT = "nlptown/bert-base-multilingual-uncased-sentiment"

    def prepareBertBaseUncasedLearningSet(self):
        tokenizer = BertTokenizer.from_pretrained(self.MODEL_NAME_BERT_BASE_UNCASED)
        model = BertForSequenceClassification.from_pretrained(self.MODEL_NAME_BERT_BASE_UNCASED, num_labels=2)

        return self.MODEL_NAME_BERT_BASE_UNCASED, tokenizer, model

    def prepareBertBaseMultilingualUncasedSentimentLearningSet(self):
        # transformer 에 의해 사전 학습된
        tokenizer = BertTokenizer.from_pretrained(self.MODEL_NAME_BERT_BASE_MULTILINGUAL_UNCASED_SENTIMENT)
        model = BertForSequenceClassification.from_pretrained(self.MODEL_NAME_BERT_BASE_MULTILINGUAL_UNCASED_SENTIMENT)

        return self.MODEL_NAME_BERT_BASE_MULTILINGUAL_UNCASED_SENTIMENT, tokenizer, model

    def prepareGPT2PretrainedLearningSet(self):
        tokenizer = GPT2Tokenizer.from_pretrained(self.MODEL_NAME_GPT2)
        model = GPT2LMHeadModel.from_pretrained(self.MODEL_NAME_GPT2)

        return self.MODEL_NAME_GPT2, tokenizer, model
