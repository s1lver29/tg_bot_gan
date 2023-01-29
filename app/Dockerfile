FROM python:3.9.16

WORKDIR .

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY . /app

CMD ["python3", "app/bot.py"]