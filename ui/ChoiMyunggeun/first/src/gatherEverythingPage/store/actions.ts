import { ActionContext } from "vuex"
import { AICommandState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"
import { REQUEST_AI_COMMAND_RESULT_TO_FASTAPI } from "./mutation-types"

export type AICommandActions = {
    requestAICommandToFastAPI(context: ActionContext<AICommandState, any>, aiCommandNumber: number): Promise<void>
    requestProcessedAICommandResultToFastAPI(context: ActionContext<AICommandState, any>): Promise<void>
}

const actions: AICommandActions = {
    async requestAICommandToFastAPI(context: ActionContext<AICommandState, any>, aiCommandNumber: number): Promise<void> {
        try {
            const res = await axiosInst.fastapiAxiosInst.post('request-ai-command', {
                command: aiCommandNumber
            });
            console.log('data:', res.data)
        } catch (error) {
            console.error('requestAICommandToFastAPI() 문제 발생:', error);
            throw error
        }
    },
    async requestProcessedAICommandResultToFastAPI(context: ActionContext<AICommandState, any>): Promise<void> {
        try {
            const res: AxiosResponse<any, any> = await axiosInst.fastapiAxiosInst.get('/dice-result/');
            console.log('data:', res)
            const data = res.data;
            console.log('data:', data)
            context.commit('REQUEST_AI_COMMAND_RESULT_TO_FASTAPI', data);
        } catch (error) {
            console.error('Error fetching AI Command Result:', error);
            // 에러를 처리할 수 있는 추가 로직
            throw error
        }
    },
    // async, Promise는 추후에 논의
    // 파라미터로 전달된 payload 외의 ActionContext 라는 것이 존재함
    // 현재 vue에서 구동하는 action의 상태값을 관리하기 위해 사용
    // 이 context 객체를 사용하여 mutations를 호출 할 수 있음
    // mutations를 호출하는 방식은 위의 list 케이스와 동일하게 context.commit()으로 호출함
    async requestCreateBoardToDjango(context: ActionContext<BoardState, unknown>, payload: {
        title: string, writer: string, content: string
    }): Promise<AxiosResponse> {

        console.log('requestCreateBoardToDjango()')

        const { title, writer, content } = payload
        console.log('전송할 데이터:', { title, writer, content })

        try {
            // HTTP 통신을 진행할 때 유의할 사항이 있음
            // GET 방식과 POST 방식이 존재하는데
            // GET 방식은 URL에 모든 정보들이 노출됨
            // POST 방식은 URL에 정보가 노출되지 않고 데이터가 숨겨져서 보내짐
            // 고로 개인 정보나 민감한 데이터의 경우 반드시 POST로 전송할 필요가 있음
            // 보낼 때 첫 번째 인자가 '요청할 경로', 두 번째 인자는 데이터 형태로 보냅니다.
            const res: AxiosResponse = await axiosInst.djangoAxiosInst.post(
                '/board/register', { title, writer, content})

            console.log('res:', res.data)
            return res.data
        } catch (error) {
            alert('requestCreateBoardToDjango() 문제 발생!')
            throw error
        }
    },
    async requestDeleteBoardToDjango(context: ActionContext<BoardState, unknown>, boardId: number): Promise<void> {
        try {
            console.log('requestDeleteBoardToDjango()')
            // HTTP 상으로 DELETE 요청을 전송함
            await axiosInst.djangoAxiosInst.delete(`/board/delete/${boardId}`)
        } catch (error) {
            console.log('requestDeleteBoardToDjango() 과정에서 문제 발생')
            throw error
        }
    },
    async requestModifyBoardToDjango(context: ActionContext<BoardState, any>, payload: {
        title: string, content: string, boardId: number
    }): Promise<void> {
        
        const { title, content, boardId } = payload

        try {
            // 수정을 요청 할 때는 PUT을 사용합니다.
            await axiosInst.djangoAxiosInst.put(`/board/modify/${boardId}`, { title, content })
            console.log('수정 성공!')
        } catch (error) {
            console.log('requestModifyBoardToDjango() 과정에서 문제 발생')
            throw error
        }
    }
};

export default actions;