"""
    This script attempts to register user.
    It then logs in with that user to parse header response holding JWT token. 
    It then writes this token to .env file. 
    These tokens expire every 7 days.
    Currently You can run this if getting 403's to refresh token. 
    In further version we will automate this with springboot scheduling. 
"""

import requests

BASE = "http://127.0.0.1:8080/api"

try:

    payload =  {
                  "username": "stephenfreed",
                  "password": "Password01!",
                  "role": "admin",
                  "firstName": "stephen",
                  "lastName": "Freed",
                  "email": "stephen@gmail.com",
                  "phone": "123-123-1234"}
           

    # posts data to registration endpoint
    response = requests.post(BASE + "/users/registration", json=payload)
    response_code = response.status_code

except Exception as e:
    pass
    # print(e)

finally:

    payload =  {
                  "username": "stephenfreed",
                  "password": "Password01!"}

    # posts data to login
    response = requests.post(BASE + "/login", json=payload)

    # parses bearer token from headers
    response_headers = response.headers
    bearer_token = response_headers["Authorization"][7:]

    # writes to .env file
    with open("./.env", "w") as my_file:
        my_file.write(f"BEARER_TOKEN={bearer_token}")
