import os
from runpod_llm import RunpodLlama2
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
# Load API key from environment variable
API_KEY = "rpa_Y72N3JGECJF0O6FWVY1K6VE1TJ4KJ7DR2J790UVMv3rmio"
if not API_KEY:
    raise ValueError("API key is missing. Please set the RUNPOD_API_KEY environment variable.")

# Define configuration parameters
config = {
    "max_tokens": 500,
    "n": 1,
    "best_of": 1,
    "presence_penalty": 0.2,
    "frequency_penalty": 0.5,
    "temperature": 0.3,
    "top_p": 1,
    "top_k": -1,
    "use_beam_search": False,
}

# Initialize the LLM
llm = RunpodLlama2(
    apikey=API_KEY,
    llm_type="7b",  # Specify the model type (e.g., "7b" or "13b").
    config=config,
    verbose=True,  # Enable verbose output for debugging.
)

# Define the prompt template
prompt_template = ChatPromptTemplate.from_template("How are you?")

# Convert the prompt template to a Runnable
prompt_runnable = RunnableLambda(lambda x: prompt_template.invoke({"input": x}))

# Create the output chain
output_chain = prompt_runnable | llm

# Invoke the model with the prompt
try:
    response = output_chain.invoke("Hello!")
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")