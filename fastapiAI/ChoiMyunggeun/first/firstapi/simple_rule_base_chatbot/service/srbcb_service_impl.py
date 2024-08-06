from simple_rule_base_chatbot.repository.srbcb_repository_impl import SrbcbRepositoryImpl
from simple_rule_base_chatbot.service.srbcb_service import SrbcbService


class SrbcbServiceImpl(SrbcbService):
    def __init__(self):
        self.srbcbRepository = SrbcbRepositoryImpl()

    def ruleBaseResponse(self, userSendMessage):
        return self.srbcbRepository.generateBotMessage(userSendMessage)
