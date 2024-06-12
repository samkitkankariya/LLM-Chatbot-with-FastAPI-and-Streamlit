import streamlit as st
import requests

def generate_essay(topic):
  """
  Sends a POST request to the FastAPI server at http://localhost:8000/essay/invoke 
  to generate an essay on the provided topic.

  Args:
      topic (str): The topic for the essay.

  Returns:
      str: The generated essay content or an error message if the request fails.
  """
  response = requests.post("http://localhost:8000/essay/invoke",
                             json={'input':{'topic':topic}})
  if response.status_code == 200:
    return response.json()['output']['content']
  else:
    return "Error: Unable to generate essay."

def generate_poem(topic):
  """
  Sends a POST request to the FastAPI server at http://localhost:8000/poem/invoke 
  to generate a poem on the provided topic.

  Args:
      topic (str): The topic for the poem.

  Returns:
      str: The generated poem content or an error message if the request fails.
  """
  response = requests.post("http://localhost:8000/poem/invoke",
                             json={'input':{'topic':topic}})
  if response.status_code == 200:
    return response.json()['output']
  else:
    return "Error: Unable to generate poem."

def main():
  """
  The main function that runs the Streamlit application.
  """
  st.title("Llama 3 Chatbot with FastAPI and Streamlit")

  st.write("This application allows you to generate essays and poems based on a given topic.")

  # Choose task
  task = st.selectbox("Choose a task", ("Generate Essay", "Generate Poem"))

  # Input topic
  topic = st.text_input("Enter the topic")

  if topic:
    if task == "Generate Essay":
      result = generate_essay(topic)
      st.subheader("Generated Essay")
    elif task == "Generate Poem":
      result = generate_poem(topic)
      st.subheader("Generated Poem")

    st.write(result)
  else:
    st.write("Please enter a topic.")

if __name__ == "__main__":
  main()
