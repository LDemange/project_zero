# $DEL_BEGIN
FROM python:3.9.7-buster
WORKDIR /prod
COPY project_zero project_zero
COPY requirements.txt requirements.txt
COPY setup.py setup.py
RUN pip install .
CMD uvicorn project_zero.api.fast:app --host 0.0.0.0 --port $PORT
# $DEL_END
