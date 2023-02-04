FROM python

RUN pip install telethon

COPY . .

CMD ["python", "tgdelete.py"]