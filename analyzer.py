from langchain.chat_models import ChatOpenAI
from prompts import SECURITY_PROMPT

llm = ChatOpenAI(model="gpt-4", temperature=0)

def analyze_log(log):
    prompt = SECURITY_PROMPT.format(log=log)
    response = llm.predict(prompt)
    return response
