from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_completion_tokens=10
)

result = llm.invoke("create  funny names of a person in india little abusive")
print(result.content)