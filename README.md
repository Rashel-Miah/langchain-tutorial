# langchain-tutorial
This tutorial is designed for langchain basic tutorial.

## 🧩 It contains the modules below.
1 ✅ Chat model Tutorial
  - Starter
  - History
  - Prompt Template
    
2 ✅ Chain Tutorial
  - Sequential Chain
  - Basic Chain
  - Building manual chain (How the chain works internally)
  - Parallel Chain
  - Conditional Chain

3 ✅ RAG Chain Tutorial
  - Basic Part 1
  - Basic Part 2
  - Basic Metadata Part 1
  - Basic Metadata Part 2
  - RAG with LLM

4 ✅ Agents
  - Basic Agent

## 🚀 Brief description of Chat Model

- ✅ Basic chat model: How to invoke a llm with system and user message
- ✅ History: Add history technique to keep track of conversations
- ✅ Prompt Template: Prompt templates are a concept in LangChain designed to assist for transformation. They take in raw user input and transforms it into a list of messages ready to pass to the language model.

## 🚀 Brief description of Chain Tutorial

- ✅ This section describes the different types of chains and illustrates the manual process of how the chain works internally.
- ✅ Basic Chain: Define the multiple tasks and wrap them to execute in a defined order. That allows a single call instead of multiple calls for multiple tasks. Example: Chain = Task1 | Task2 | Task3
- ✅ Manual Chain: It tells, how to create a chain manually without pipe(|) operator using the help of RunnableLambda and RunnableSequence
- ✅ Sequential Chain: It is a Chain where the outputs of one chain feed directly into next chain.
      Example: Final Chain = Chain-1(Task1|Task2|Task3) | Chain-2 (Task1|Task2|Task3): Out put of Chain-1 is the input of Chain-2.
- ✅ Parallel Chain: It enables the simultaneous execution of multiple independent sub-chains or components. This allows for parallel processing of different tasks or branches within a larger workflow, significantly reducing overall execution time and improving efficiency, especially when dealing with tasks that do not depend on each other's output.
- ✅ Conditional Chain: The primary mechanism for building conditional chains in LangChain is the RunnableBranch. This component acts like an "if-else" statement, allowing you to define a series of conditions and corresponding runnables. When the RunnableBranch is invoked, it evaluates each condition in order, and the runnable associated with the first condition that evaluates to True is executed. If no conditions are met, a default runnable can be specified to handle the unconditioned flow.

## 🚀 Brief description of RAG
- ✅ Retrieval Augmented Generation (RAG) is a powerful technique that enhances language models by combining them with external knowledge bases. RAG addresses a key limitation of models: models rely on fixed training datasets, which can lead to outdated or incomplete information. When given a query, RAG systems first search a knowledge base for relevant information. The system then incorporates this retrieved information into the model's prompt. The model uses the provided context to generate a response to the query. By bridging the gap between vast language models and dynamic, targeted information retrieval, RAG is a powerful technique for building more capable and reliable AI systems.
   - Key Concepts:
    (1) Retrieval system: Retrieve relevant information from a knowledge base. Here, You can use a vector database to store external knowledge.
    (2) Adding external knowledge: Pass retrieved information to a model.

## 🚀 Brief description of AGENT
- ✅ By themselves, language models can't take actions - they just output text. Agents are systems that take a high-level task and use an LLM as a reasoning engine to decide what actions to take and execute those actions.
Many LLM applications implement a particular control flow of steps before and / or after LLM calls. As an example, RAG performs retrieval of documents relevant to a user question, and passes those documents to an LLM in order to ground the model's response in the provided document context.

Instead of hard-coding a fixed control flow, we sometimes want LLM systems that can pick their own control flow to solve more complex problems! This is one definition of an agent: an agent is a system that uses an LLM to decide the control flow of an application. There are many ways that an LLM can control application:

  - An LLM can route between two potential paths
  - An LLM can decide which of many tools to call
  - An LLM can decide whether the generated answer is sufficient or more work is needed

## 🤖 Model Info

This app uses:
- **LLM:** `qwen2.5-coder` via Ollama


Built by [Rashel Sarker].  
Feel free to fork and customize. PRs welcome!
