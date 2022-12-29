# Backend <!-- omit in toc -->

**UNDER CONSTRUCTION**

- [Authentication/Authorization](#authenticationauthorization)



## Logging <!-- omit in toc -->

By setting a `LOG_LEVEL` env variable you can enable more/ less detailed logging of your FastAPI container (default is `INFO`).
Add your own log statements using the `logger` object from `loguru` instead of `print`:

```py
from loguru import logger
logger.info("Writing logs with INFO level")
```


## Authentication/Authorization

Authentication is implemented in the backend via <____>.
A HTTP request to the backend can hence be authenticated via either

1. A browser cookie containing your token
2. or an `Authorization` header containing a Bearer token
3. or your browser session (after a first initial authentication in step 1)

See here a **non-restricted endpoint** (no authentication required):

```python
@router.get("/test_endpoint")
def test():
    # logic of the endpoint here
    pass
```

Here is how to **require authentication**:


```python
# TODO

from ....

auth = AuthModule()

@router.get("/test_endpoint")
def test(user: str = Depends(auth.dependency)):
    # logic of the endpoint here
    pass
```

In order to additionally **require authorization**, add a call to the `authorization` function:

```python
@router.get("/test_endpoint")
def test(user: str = Depends(auth_whitelisted.dependency)):
    # logic of the endpoint here
    pass
```
