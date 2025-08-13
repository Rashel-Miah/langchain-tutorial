from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from datetime import datetime, timedelta
from langchain.agents import tool

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """

    current_time = datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time
    

@tool
def time_difference(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the time difference between Bangladesh and London in the specified format.
        Bangladesh is 5 hours ahead of London, UK.
        So, subtract 5 hours from Bangladesh time.
       """
    hours_to_subtract = 5
    new_time = datetime.now() - timedelta(hours=hours_to_subtract)
    formatted_time = new_time.strftime(format)
    return formatted_time


# Define the model
llm = ChatOllama(model="codellama:13b", temperature=0.1)

query = "What is the current time in London? (You are in Bangladesh). Just show the current time and not the date."

prompt_template = hub.pull("hwchase17/react")

tools = [get_system_time, time_difference]

agent = create_react_agent(llm, tools, prompt_template)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_executor.invoke({"input": query})