from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="qwen2.5-coder:7b", temperature=0.1)

system_message = "Translate the following from English into {language}"

promt_template = ChatPromptTemplate.from_messages(
    [("system",system_message),("user","{text}")]
)

prompt = promt_template.invoke({"language":"Italian", "text":"How are you?"})

#print(prompt.to_messages)

response = llm.invoke(prompt)
print(response.content)