# LLM-Chatbot-with-FastAPI-and-Streamlit
This project empowers you to generate creative text content using the power of large language models (LLMs). It leverages the strengths of FastAPI for building a robust API server and Streamlit for crafting a user-friendly web interface.

**Key Technologies:**

* **FastAPI:** A high-performance, Python-based framework for building APIs with ease.
* **Langchain:** A library for simplifying work with LLMs and managing complex chatbot interactions.
* **Streamlit:** A framework that enables the creation of interactive web applications in a streamlined manner.
* **OpenAI API (Optional):** A powerful option for accessing advanced language models from OpenAI (requires a paid API key).
* **Groq Langchain Chat (Optional):** A convenient way to utilize Groq's cloud-based collection of open-source models for fast and efficient processing.
* **Ollama LLM (Locally Downloaded):** A free and open-source LLM (Llama 3 in this case) that can be run locally on your machine.
* **LangServe:** A library that simplifies deployment of LangChain runnables and chains as REST APIs.
* **Prompt Templates:** Two templates are defined for generating essays and poems.
* **Routes:** Routes for essay and poem generation are added to the FastAPI application.
* **Server Execution:** The FastAPI application is run using uvicorn.

**1. Environment Variables (.env):**

* Create a file named `.env` in your project's root directory.
* This file stores sensitive information like API keys that you don't want to commit to version control.
* Include the following lines, replacing placeholders with your actual values:

```
OPENAI_API_KEY=your_openai_api_key  # Optional for OpenAI access
GROQ_API_KEY=your_groq_api_key     # Optional for Groq cloud
```

* **Important:** Never share your API keys publicly.

**2. Running the Application:**

There are two main components to run: the FastAPI server and the Streamlit web interface.

**2.1. Running the FastAPI Server (app.py):**

1. Make sure you have Python and the required libraries installed (`pip install fastapi langchain langchain-openai langchain-groq langchain-community uvicorn dotenv`).
2. Load the environment variables:

   ```bash
   source .env  # Linux/macOS
   .env\Scripts\activate  # Windows (if using virtual environment)
   ```

3. Start the server:

   ```bash
   python app.py  # Replace port if needed
   ```

   This will run the FastAPI server, listening on port 8000 (or your chosen port) and ready to receive requests from the Streamlit application.

**2.2. Running the Streamlit Web Interface (client.py):**

1. In a separate terminal session, navigate to your project's directory.
2. Start the Streamlit app:

   ```bash
   streamlit run client.py
   ```

   This will launch the Streamlit interface in your web browser, typically at `http://localhost:8080` (the default port for Streamlit).

**Basic Workflow:**

1. **Run the FastAPI server:** Follow the steps in section 2.1 to start the server.
2. **Run the Streamlit web interface:** Follow the steps in section 2.2 to launch the Streamlit app in your browser.
3. **Interact with the Streamlit app:**
   - Select between generating an essay or a poem.
   - Enter a topic for the desired content.
   - Click the appropriate button to trigger the request to the FastAPI server.
   - The generated essay or poem will be displayed in the Streamlit interface.

**Additional Notes:**

* By default, the Streamlit application is configured to use the Groq API for essays and  Ollama LLM for poems.
* To leverage OpenAI, you'll need to uncomment the corresponding code sections in `app.py` and provide the necessary API keys in the `.env` file.
* Remember to replace placeholders with your actual API keys and adjust port numbers if needed.
* For detailed information about configuration options and advanced usage, refer to the documentation for FastAPI, Langchain, and Streamlit.

