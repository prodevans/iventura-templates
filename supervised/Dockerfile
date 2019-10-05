FROM python

EXPOSE  8050 8080

COPY . /app

WORKDIR /app

RUN python -m pip install --upgrade pip

RUN pip install -r /app/requirements.txt

RUN pip install --upgrade google-api-python-client 

RUN pip install requests

RUN pip install plotly --upgrade

# ENTRYPOINT ["python"]

# CMD ["app.py"]

CMD ["python", "/app/app.py"]

