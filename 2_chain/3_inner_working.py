from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableSequence

# Define the model
llm = ChatOllama(model="qwen2.5-coder:7b", temperature=0.1)

# Define prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","You love facts and you tell facts about {animal}."),
        ("human","Tell me {count} facts.")
    ]
)

# Create individual runnables(Steps in the chain)
format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model =  RunnableLambda(lambda x: llm.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x.content)

# Create the runnable sequence(equivalent to the LCEL chain)
chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

# Run the chain
response = chain.invoke({"animal":"elephant", "count":2})

print(response)


# Create the combined chain using LangChain Expression Language(LCEL)
# First call the prompt_template then pass the result to llm, and then pass the result to StrOutputParser() function to get final result.
#chain = prompt_template | llm | StrOutputParser()

#result = chain.invoke({"animal":"cat", "count":2})

#print(result)