from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableSequence

# Define the model
llm = ChatOllama(model="qwen2.5-coder:7b", temperature=0.1)

# Define prompt template
animal_facts_template = ChatPromptTemplate.from_messages(
    [
        ("system","You like telling facts and you tell facts about {animal}."),
        ("human","Tell me {count} facts.")
    ]
)

# Defina a prompt template for translation to French

translation_template = ChatPromptTemplate.from_messages(
    [
        ("system","You are a translator and convert the provided text into {language}."),
        ("human", "Translate the following text to {language}:{text}"),
    ]
)

# Define additional processing steps using RunnableLambda
#count_words = RunnableLambda(lambda x: f"Word count: {len(x.split())}\n{x}")

prepare_for_translation = RunnableLambda(lambda output: {"text":output, "language":"french"})


# Create the combined chain using LangChain Expression Language(LCEL)
# First call the animal_fact_template then pass the result to llm, and then pass the result to StrOutputParser() function,
# then pass the result to prepare_for_translation, then pass the result to translation_template,
# and then pass the result to StrOutputParser() to get final result.
chain = animal_facts_template | llm | StrOutputParser() | prepare_for_translation| translation_template|llm| StrOutputParser()

# Run the chain
response = chain.invoke({"animal":"elephant", "count":2})

print(response)