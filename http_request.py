import requests


# get
def get():
    response = requests.get('http://localhost:8080/')
    # check the response status code
    if response.status_code == 200:
        # if the response was successful, print the response text
        print(response.text)
    else:
        # if the response was not successful, print an error message
        print('An error occurred:', response.status_code)


# put
def put():
    response = requests.put(url='http://localhost:8080/', data="hello put")
    # check the response status code
    if response.status_code == 200:
        # if the response was successful, print the response text
        print(response.text)
    else:
        # if the response was not successful, print an error message
        print('An error occurred:', response.status_code)


# put
def post():
    response = requests.put(url='http://localhost:8080/', data="hello post")
    # check the response status code
    if response.status_code == 200:
        # if the response was successful, print the response text
        print(response.text)
    else:
        # if the response was not successful, print an error message
        print('An error occurred:', response.status_code)


get()
put()
post()
