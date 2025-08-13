from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatOllama(model="qwen2.5-coder:7b", temperature=0.1)

#result = llm.invoke("Hi")
#print(result.content)

message=[
    SystemMessage("You are a helpful assistant that translates English to Bangla. Translate the user sentence."),
    HumanMessage("I love programming.")
]

#result = llm.invoke(message)
#print(result.content)

messages = [
    ("system", "You are a helpful assistant that translates English to Bengali. Translate the user sentence."),
    ("human", "I love programming."),
]
#result = llm.invoke(messages)
#print(result.content)

print(llm.invoke([{"role":'user',"content":"Hello"}]).content)