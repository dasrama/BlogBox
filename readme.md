## Description 📝:
- This project aims to implement **JWT authentication** and **OAuth authorization** for secure API access. 
- It plans to enhance data validation by restructuring schemas and models and establish relationships between different data entities.
- Additionally, future goals include deploying on **Linux**, mastering the Linux terminal, **configuring Dockerfiles**, and setting up domain names for the application.



## 🛠️ Requirements

- Python 3.7+
- FastAPI
- SQLAlchemy
- psycopg2


## 📦 run the application locally :
### **Clone the repository**
```
git clone https://github.com/dasrama/BlogBox.git
``` 
### Create a virtual environment:
  - In the terminal, navigate to your project directory using the cd command. Once inside your project directory, run the following  command to create a virtual environment:

### Create a virtual environment:
```
    py -3 -m venv venv
```

### Activate the virtual environment:
```
.\venv\Scripts\activate
```

### Install dependencies :
```
pip install -r requirements.txt
```

### Configure Visual Studio Code to use the virtual environment:
- search for <Python: Select Interpreter>. Choose the interpreter located within your virtual environment (typically under the venv directory).

### **Set the environment variables in the .env file**:

### **run the application**
```
uvicorn app.main:app --reload
```

## 📋 Usage

- Access the Swagger documentation for detailed API usage instructions and test endpoints locally: `http://localhost:8000/docs`.
- Test the endpoints using tools like cURL, Postman, or any HTTP client of your choice.
 
