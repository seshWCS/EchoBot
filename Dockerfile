FROM python:3.10

COPY . tgbot

RUN pip install -r tgbot/requirements.txt

CMD ["python", "tgbot/main.py"]
