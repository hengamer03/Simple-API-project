# Simple API

This is a simple API that provides two endpoints: one that returns a static message and another that runs a Python script inside a virtual environment and returns its output.

## Endpoints

### `/test`
- **Method:** GET
- **Description:** Returns a static message "it works".
- **Response:**
  ```json
  {
    "message": "it works"
  }
  ```

### `/run-script`
- **Method:** GET
- **Description:** Executes a Python script inside a virtual environment and returns its output.
- **Response:**
  ```json
  {
    "output": "Python script output",
    "error": ""
  }
  ```

## Setup

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd swagger-api
   ```

2. **Create a virtual environment:**
   ```sh
   python3 -m venv env
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```sh
     .\env\Scripts\activate
     ```
   - On Unix or MacOS:
     ```sh
     source env/bin/activate
     ```

4. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```sh
   python main.py
   ```

## Swagger Documentation

The API documentation is available at `/swagger`. You can view it by navigating to `http://localhost:5000/swagger` in your web browser.

## Project Structure

```
swagger-api/
├── env/                    # Virtual environment
├── swagger/                # Swagger configuration
│   ├── swagger.yaml        # Swagger API definition
│   └── swagger_setup.py    # Swagger setup script
├── test.py                 # Python script to be executed
├── main.py                 # Main application script
└── README.md               # Project documentation
```
