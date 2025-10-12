# fastapi-project

This is a simple FastAPI project that runs locally. 

## Project Structure

```
fastapi-project
├── src
│   ├── main.py          # Entry point of the FastAPI application
│   ├── models
│   │   └── __init__.py  # Data models used in the application
│   └── routes
│       └── __init__.py  # Application routes
├── templates
│   └── index.html       # HTML template for the home page
├── static
│   └── styles
│       └── main.css     # CSS styles for the application
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Requirements

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Running the Application

To run the FastAPI application, execute the following command:

```
uvicorn src.main:app --reload
```

You can access the application at `http://127.0.0.1:8000`. The home page can be found at `http://127.0.0.1:8000/`. 

## License

This project is licensed under the MIT License.