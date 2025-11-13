FROM python:3.10-slim AS base

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

COPY app/ .

FROM base AS final

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]