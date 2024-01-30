![](https://www.jambopay.com/img/logo.png)

# JamboPay Customer Data API Project

> JamboPay Customer Data Project: Fetch and store data from customers and also provide the data upon request.

## Built With

- Django
- SQLite3(database), DRF(For Endpoints), Knox(Authentication and Authorization), Swagger(API Documentation)

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

A text editor eg VS Code, Python 3.7.6, Postman

### Setup

**Step 1: Clone this repo locally using git**

- Create a folder in your local machine
- Open your console in your folder and run this command: `git clone https://github.com/NduatiKagiri/JamboPay.git`
- Alternatively, you can just download the complete zip file and extract the folder in your directory

  **Step 2: Run in your project directory**

- Run `pip install -r requirements` to install all the modules required
- Run `py manage.py migrate` to make sure the database is well configured
- Run `py manage.py runserver` to start the project

**Step 3: Open the project documentation**

- Run `http://127.0.0.1:8000/swagger` on your browser to open the project documentation to view the endpoints

**Step 2: Make requests and check responses on Postman**

- Open Postman and send requests using the API endpoints from the documents
- First create a user using a POST request on the customers endpoint with username, email and password as form data
- Create an Auth Token by sending a POST request with the login endpoint and your email and password as form data
- Add the recieved token to the headers of all your future requests to the API

## Authors

:bust_in_silhouette: **NduatiKagiri**

GitHub: https://github.com/NduatiKagiri
Twitter: https://twitter.com/NduatiKagiri
LinkedIn: https://linkedin.com/in/nduati-kagiri/

## :handshake: Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the issues page.

## Show your support

Give a :star:️ if you like this project!

## :memo: License

This project is MIT licensed.
