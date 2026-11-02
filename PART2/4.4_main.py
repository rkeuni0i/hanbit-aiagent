# ==============================================================================
# [4.4절 실습] 첫 번째 AI 모델(LLM) 호출하기
# ==============================================================================
# 이 코드는 Google의 인공지능 모델(gemini-3.5-flash-lite)에게 "역할(System)"을 부여하고,
# 사용자의 말(Human)을 건네어 번역된 답변을 받아보는 가장 기초적인 예제입니다.

# 1. 필요한 도구(라이브러리) 가져오기
# - ChatGoogleGenerativeAI: Google의 채팅형 AI 모델(Gemini 등)을 파이썬에서 쉽게 쓸 수 있게 해주는 도구입니다.
# - load_dotenv: 환경 변수('.env' 파일)를 읽어와서 컴퓨터 환경에 등록해주는 도구입니다.
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# 2. 환경 변수(.env 파일) 불러오기
# .env 파일이 있는 경우 환경 변수(GOOGLE_CLOUD_PROJECT, GOOGLE_GENAI_USE_VERTEXAI 등)를 불러옵니다.
load_dotenv()

# 3. 사용할 인공지능(LLM) 모델 준비하기 (ADC 방식 인증)
# - API 키 대신 Google Cloud ADC(Application Default Credentials)를 사용하여 Vertex AI를 통해 호출합니다.
# - vertexai=True 설정 시 로컬에 저장된 gcloud 인증 정보(gcloud auth application-default login)를 자동으로 활용합니다.
project_id = os.getenv("GOOGLE_CLOUD_PROJECT", "iceu-songpa04")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    vertexai=True,
    project=project_id,
)

# 4. AI에게 전달할 대화 목록(메시지 리스트) 만들기
# 파이썬의 리스트([ ]) 안에 튜플((역할, 내용)) 형태로 대화 시나리오를 작성합니다.
# - "system": AI에게 역할, 성격, 규칙을 지시하는 '무대 뒤 감독님의 지시사항'입니다.
# - "human": 실제 사용자가 AI에게 건네는 질문이나 요청입니다.
messages = [
    (
        "system",
        "당신은 사용자가 한 말을 영어로 번역하는 유능한 번역가입니다.",
    ),
    ("human", "안녕하세요."),
]

# 5. AI 모델 실행하기 (invoke = '호출하다/작동시키다')
# 준비한 메시지 목록(messages)을 AI(llm)에게 전달하고, AI가 생성한 응답을 'ai_msg' 변수에 저장합니다.
ai_msg = llm.invoke(messages)

# 6. 결과 화면에 출력하기
# AI가 답변한 내용(번역 결과인 "Hello."와 부가 정보)을 화면에 보여줍니다.
# (참고: 답변 텍스트만 깔끔하게 보고 싶다면 print(ai_msg.content) 라고 쓸 수도 있습니다.)
print(ai_msg)
