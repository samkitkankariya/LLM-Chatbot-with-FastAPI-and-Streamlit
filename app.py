from fastapi import FastAPI  # For building the API
from langchain.prompts import ChatPromptTemplate  # For creating chat prompts
from langchain_openai import ChatOpenAI  # For OpenAI chat functionality
from langchain_groq import ChatGroq  # For Groq chat functionality
from langchain_community.llms import Ollama  # For Ollama LLM
from langserve import add_routes  # For adding routes to the API
import uvicorn  # For running the API
import os  # For loading environment variables
from dotenv import load_dotenv  # For loading environment variables

load_dotenv()

#Set environment variables
os.environ['OPEN_API_KEY'] = os.getenv("OPENAI_API_KEY")

#Initialize Groq Langchain chat object 
groq_chat = ChatGroq(
    groq_api_key=os.environ.get("GROQ_API_KEY"),
    model_name="mixtral-8x7b-32768",
)

#Initialize FastAPI 
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

model_openai=ChatOpenAI() #model 1 (paid)

#Initialize LLMs
llm_groq=groq_chat #model 2 (groq cloud - collection of different open source model known for its speed)
llm=Ollama(model="llama3") #model 2 (locally downloaded on pc: open source)

# Define chat prompts
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words")

# Add route for generating an essay using the Groq LLM
add_routes(
    app,
    prompt1 | llm_groq, #replace with model_openai if you want to use OpenAI API 
    path = "/essay"
) 

# Add route for generating a poem using the Ollama LLM
add_routes(
    app,
    prompt2 | llm, # Route for generating a poem using the Ollama LLM
    path = "/poem" # API endpoint for generating a poem
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

'''
If you close the terminal without exiting the server, you will get the following error:
[Errno 10048] error while attempting to bind on address ('127.0.0.1', 8000):
 only one usage of each socket address (protocol/network address/port) is normally permitted

 Solution - To check if there is a process using port 8000, you can run the following 
 command in your terminal:
    netstat -ano | findstr :8000

Once you have identified the PID of the process using port 8000, you can stop the process
 using the following command:
    taskkill /F /PID <PID>
    Replace <PID> with the actual process ID.
'''