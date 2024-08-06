from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from fastapi.responses import JSONResponse

from simple_rule_base_chatbot.controller.request_form.SrbcbRequestForm import SrbcbRequestForm
from simple_rule_base_chatbot.service.srbcb_service_impl import SrbcbServiceImpl

simpleRuleBaseChatbotRouter = APIRouter()

async def injectSrbcbService() -> SrbcbServiceImpl:
    return SrbcbServiceImpl()

@simpleRuleBaseChatbotRouter.post("/srbcb-response")
async def srbcbTrain(srbcbRequestForm: SrbcbRequestForm,
                     srbcbService: SrbcbServiceImpl = Depends(injectSrbcbService)):

    print(f"controller -> srbcbTrain(): srbcbRequestForm: {srbcbRequestForm}")

    generatedText = srbcbService.ruleBaseResponse(srbcbRequestForm.userSendMessage)
    return JSONResponse(content={"generatedText": generatedText}, status_code=status.HTTP_200_OK)