# Flask Chatbot Application

## Overview
This is a simple chatbot application built using Flask and DeepSeek AI. The application includes user authentication, a chat interface, and a deep learning model for generating chatbot responses.

## Features
- User registration and authentication
- Chat interface with AI-generated responses
- SQLite database for user management
- Dockerized for easy deployment

## Prerequisites
Make sure you have the following installed before running the application:
- Python 3.9+
- Docker
- pip

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/parvvaresh/deepspeek
   cd deepspeek
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Download the deep learning model:
   ```sh
   chmod +x dl_model.sh
   ./dl_model.sh
   ```

4. Initialize the database:
   ```sh
   python app.py
   ```

## Running the Application

### Using Python
```sh
python app.py
```

### Using Docker
1. Build the Docker image:
   ```sh
   docker build -t flask-chatbot .
   ```
2. Run the container:
   ```sh
   docker run -p 9090:9090 flask-chatbot
   ```

## API Endpoints
- `GET /` - Home page
- `GET /register` - Registration page
- `POST /register` - Handle user registration
- `GET /login` - Login page
- `POST /login` - Handle user login
- `GET /chat` - Chat interface
- `POST /chat` - Get AI-generated chatbot response

## Technologies Used
- Flask
- SQLite
- Bcrypt
- Ollama AI
- Docker

## License
This project is open-source and available under the MIT License.

