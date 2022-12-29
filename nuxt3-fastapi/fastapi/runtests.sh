# !/bin/bash
# Launch from /fastapi


if [ "$1" = "-coverage" ] || [ "$1" = "-c" ]
then
    pytest --cov-report html:tests/coverage --cov=api tests/
else
    pytest tests/
fi

