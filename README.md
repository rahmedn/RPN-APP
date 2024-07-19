# FastAPI RPN Calculator

This project is an RPN (Reverse Polish Notation) calculator implemented in a client/server mode using FastAPI for the backend and Swagger for the user interface.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)


## Introduction

This project implements an RPN calculator with the following features:

- Add an element to a stack
- Retrieve the stack
- Clear the stack
- Arithmetic operations: addition, subtraction, multiplication, division

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. Clone the repository:
    
    ```bash
    git clone https://github.com/rahmedn/RPN-APP.git
    cd RPN-APP

2. Install the dependencies
    
    ```bash
    pip install -r requirements.txt

3. Start Application 

    ```bash
    uvicorn app.main:app --reload --port 8080

## Usage

1. Swagger Interface
Go to http://127.0.0.1:8000/docs to use the Swagger interface to test the different API endpoints.

## Testing

run the test with pytest command
