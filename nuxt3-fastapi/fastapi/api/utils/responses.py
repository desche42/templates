"""
Contains example responses for documenting the swagger page
"""
from fastapi import status

DEFAULT_RESPONSES = {
    # status.HTTP_204_NO_CONTENT: {"description": "No results found."},
    # status.HTTP_400_BAD_REQUEST: {"description": "Bad request."},
    status.HTTP_401_UNAUTHORIZED: {"description": "Not authenticated."},
    status.HTTP_403_FORBIDDEN: {"description": "Unauthorized to access."},
    # status.HTTP_502_BAD_GATEWAY: {"description": "Bad Gateway."}
}

def get_200_response(example):
    "Returns formatted successful response with an example"
    return {
        "description": "Successful response",
        "content": {
            "application/json": {
                "example": example
            }
        }
    }

