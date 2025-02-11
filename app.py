import streamlit as st
import logging
from langchain_community.document_loaders import PyMuPDFLoader
from openai import OpenAI
import os


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.environ.get("API_KEY"),
)

# Configure logging
logging.basicConfig(level=logging.INFO)

def load_pdf(uploaded_file):
    """Load PDF file with PyMuPDF"""
    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        loader = PyMuPDFLoader(file_path="temp.pdf")
        data = loader.load()
        logging.info("PDF loaded.")
        return data
    else:
        logging.error("No PDF file uploaded.")
        st.error("Please upload a PDF file.")
        return None



def main():
    st.title("Welcome to your Job Assistant")
    uploaded_file = st.file_uploader("Please upload your CV as a PDF file to start", type="pdf")

    if uploaded_file:
        logging.info("PDF file uploaded")
        with st.spinner("Generating response..."):
                try:
                    # Load pdf file 
                    cv_text = load_pdf(uploaded_file)

                    # Make the API call with the conversation history
                    completion = client.chat.completions.create(
                        extra_headers={
                            "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
                            "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
                        },
                        extra_body={},
                        model="google/gemini-2.0-flash-lite-preview-02-05:free",
                        messages=[
    {
      "role": "system",
      "content": "You are a professional job assistant. Your role is to analyze a curriculum vitae (CV) and provide the following: 1. A list of possible job positions the candidate can apply for, ordered from most relevant to least relevant. 2. Tips on how the candidate can improve their profile to increase their chances of landing a job. Be specific and actionable in your advice."
    },
    {
      "role": "user",
      "content": f"Here is my CV:\n{cv_text}\n\nPlease analyze it and provide the requested output."
    }
  ]
                    )
                    st.markdown("**Assistant:**")
                    st.write(completion.choices[0].message.content)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

    else:
        st.info("No PDF documents uploaded")


if __name__ == "__main__":
    main()

