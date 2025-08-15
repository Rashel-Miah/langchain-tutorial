from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

# Define the model
llm = ChatOllama(model="qwen2.5-coder:7b", temperature=0.1)

# Define prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","You are a facts expert who knows the facts about {animal}."),
        ("human","Tell me {fact_count} facts.")
    ]
)

# Create the combined chain using LangChain Expression Language(LCEL)
# First call the prompt_template then pass the result to llm, and then pass the result to StrOutputParser() function to get final result.
chain = prompt_template | llm | StrOutputParser()

result = chain.invoke({"animal":"cat", "fact_count":2})

print(result)