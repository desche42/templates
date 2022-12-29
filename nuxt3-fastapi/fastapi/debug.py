"Debug the API"
import os

import uvicorn

# Must be set before importing main
os.environ["FASTAPI_ENV"] = "development"

"""
Run your FastAPI application in debug mode in VS Code.
"""

if __name__ == "__main__":
    # port 5000 causes errors in MacOS due to AirPlay port
    uvicorn.run("api.main:app", host="127.0.0.1", port=5001, reload=True)
