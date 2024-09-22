from services.providers import AIProviderFactory, AIProviderType
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable.config import RunnableConfig

# Create a Groq chat model
groq_chat = AIProviderFactory.create_provider(AIProviderType.GROQ, "llama-3.1-8b-instant", stream=True)
gemini_chat = AIProviderFactory.create_provider(AIProviderType.GEMINI, "gemini-1.5-flash", stream=True)

# Define the prompt template
prompt = ChatPromptTemplate.from_template("You are a helpful assistant. {input}")

# Create the chain
chain = prompt | gemini_chat | StrOutputParser()

def run_chain(user_input: str, config: RunnableConfig = {}) -> None:
    for chunk in chain.stream({"input": user_input}, config):
        print(chunk, end="", flush=True)

if __name__ == "__main__":
    run_chain("Write a resume for a QA lead with 12 years of experience in automation and manual testing.")
