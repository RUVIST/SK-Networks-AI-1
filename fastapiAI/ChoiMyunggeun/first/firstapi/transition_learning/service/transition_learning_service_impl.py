import torch

from transition_learning.repository.transition_learning_repository_impl import TransitionLearningRepositoryImpl
from transition_learning.service.transition_learning_service import TransitionLearningService


class TransitionLearningServiceImpl(TransitionLearningService):
    def __init__(self):
        self.__transitionLearningRepository = TransitionLearningRepositoryImpl()

    def predictText(self, transitionLearningPredictRequestForm):
        modelName, tokenizer, model = self.__transitionLearningRepository.prepareBertBaseUncasedLearningSet()
        model.eval()

        tokenizedUserInputText = tokenizer(
            transitionLearningPredictRequestForm.firstSentence,
            transitionLearningPredictRequestForm.secondSentence,
            return_tensors="pt",
            truncation=True,
        )

        with torch.no_grad():
            outputList = model(**tokenizedUserInputText)
            logitList = outputList.logits
            prediction = torch.argmax(logitList, dim=-1).item()

        if prediction == 1:
            result = "두 문장은 다르지만 의미는 같습니다."
        else:
            result = "두 문장의 의미는 다릅니다/"

        return result

    def transitionLearningWithsentimentAnalysis(self, sentimentAnalysisRequestForm):
        modelName, tokenizer, model = (
            self.__transitionLearningRepository.prepareBertBaseMultilingualUncasedSentimentLearningSet())
        model.eval()

        tokenizedUserInputText = tokenizer(
            sentimentAnalysisRequestForm.sentence,
            return_tensors="pt",
            truncation=True
        )

        with torch.no_grad():
            outputList = model(**tokenizedUserInputText)
            logitList = outputList.logits
            prediction = torch.argmax(logitList, dim=-1).item()

        sentimentList = ["매우 부정", "부정", "중립", "긍정", "매우 긍정"]
        sentiment = sentimentList[prediction]

        return sentiment

    def predictiTextWithGPT2(self, gpt2PretrainedPredictionRequestForm):
        modelName, tokenizer, model = (
            self.__transitionLearningRepository.prepareGPT2PretrainedLearningSet())
        model.eval()

        # tokenizedUserInputText = tokenizer(
        #     gpt2PretrainedPredictionRequestForm.text,
        #     return_tensors="pt"
        # )

        encodedInputList = tokenizer.encode(gpt2PretrainedPredictionRequestForm.text, return_tensors="pt")
        outputList = model.generate(encodedInputList, max_length=100, num_return_sequences=1)
        generatedText = tokenizer.decode(outputList[0], skip_special_tokens=True)

        return generatedText

