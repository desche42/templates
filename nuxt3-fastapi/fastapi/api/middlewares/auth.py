"""
Authentication and authorization methods used in the app
"""
import os
import uuid
import hashlib

auth_schemes = []

# list of authorised users
auth_usernames = (os.getenv("AUTH_USER_NAMES") or "").split(",")
debug_user = os.getenv("DEBUG_USER")

if debug_user:
    # add here methods for local debug user
    auth_schemes.append({})
    auth_usernames.append(debug_user)


def make_session_params():
    """Creates session parameters for FastAPI application"""
    secret_key = uuid.uuid4()
    secret_hash = hashlib.sha1()
    secret_hash.update(str(secret_key).encode("utf-8"))
    return {
        "secret_key": secret_key,
        "session_cookie": "fastapi_session_" + secret_hash.hexdigest()[:8]
    }


# auth = YourNewAuthModule()
