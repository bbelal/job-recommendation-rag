# Job Assistant App with Streamlit and Docker

This repository contains a **Job Assistant App** built with Streamlit. The app analyzes a user's CV (uploaded as a PDF) and provides:
1. A list of possible job positions the candidate can apply for (ordered by relevance).
2. Actionable tips to improve the candidate's profile for better job opportunities.

The app uses OpenAI's API via [OpenRouter.ai](https://openrouter.ai) to generate responses.

---

## Prerequisites

Before running the app, ensure you have the following:

1. **Docker**: Install Docker from [here](https://docs.docker.com/get-docker/).
2. **API Key**: Sign up for an API key from [OpenRouter.ai](https://openrouter.ai). This key is required to interact with the AI model.

---

## How to Run the App

### 1. Build the Docker Image

Navigate to the root directory of the project and build the Docker image using the following command:

`docker build -t job-assistant-app .`

### 2. Run the Docker Container

Run the container using the following command. Replace `your_api_key_here` with your actual OpenRouter.ai API key:

`docker run -p 8501:8501 -e API_KEY=your_api_key_here job-assistant-app`

- `-p 8501:8501`: Maps port 8501 on your local machine to port 8501 in the container (Streamlit's default port).
- `-e API_KEY=your_api_key_here`: Passes your OpenRouter.ai API key as an environment variable to the app.

### 3. Access the App

Open your web browser and navigate to: [http://localhost:8501](http://localhost:8501)

---

## App Features

1. **Upload Your CV**: Upload your CV as a PDF file.
2. **AI-Powered Analysis**: The app uses the **Google Gemini 2.0 Flash Lite** model (via OpenRouter.ai) to analyze your CV and provide:
   - A list of job positions you can apply for (ordered by relevance).
   - Actionable tips to improve your profile.
3. **Secure API Key Handling**: The app securely uses your OpenRouter.ai API key via environment variables.

---

## Example

Here’s an example of running the app with an API key:

`docker run -p 8501:8501 -e API_KEY=12345-abcdef-67890 job-assistant-app`

---

## Code Overview

The app is built using:
- **Streamlit**: For the web interface.
- **PyMuPDF**: For loading and extracting text from PDF files.
- **OpenRouter.ai**: For interacting with the AI model (Google Gemini 2.0 Flash Lite).

### Key Functions

- **`load_pdf(uploaded_file)`**: Loads and extracts text from the uploaded PDF file.
- **`main()`**: Handles the Streamlit interface, file upload, and API calls to OpenRouter.ai.

---

## Notes

- **API Key Security**: Never hardcode your API key in the app or commit it to version control. Use environment variables or a secrets manager for secure handling.
- **Docker Compose**: If you prefer using Docker Compose, check the `docker-compose.yml` file for additional configuration options.

---

## Troubleshooting

1. **No PDF Uploaded**: Ensure you upload a valid PDF file.
2. **API Key Not Set**: Make sure the `API_KEY` environment variable is correctly passed to the Docker container.
3. **Model Errors**: If the AI model fails to respond, check your OpenRouter.ai API key and ensure you have sufficient credits.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.