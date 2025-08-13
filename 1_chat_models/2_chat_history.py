from langchain_ollama import ChatOllama
from langchain.schema import HumanMessage,SystemMessage, AIMessage

llm = ChatOllama(model="qwen2.5-coder:7b", temperature=0.1)

chat_history = [] # Create a list to store message

# Initial system message
system_message = SystemMessage(content="You are a helpful AI assistant")
chat_history.append(system_message) # add system message to the chat history

# Loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query)) # Add user message

    # Get AI response using history
    print(chat_history)
    result = llm.invoke(chat_history)
    response = result.content
    print("response: ",response)
    chat_history.append(AIMessage(content=response)) # Add AI 
    
    print(f"AI: {response}")