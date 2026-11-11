FROM python:3.11-alpine

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV APP_PORT=5008
ENV PYTHONDONTWRITEBYTECODE=1
ENV MARKER=netlab
EXPOSE 5008

ARG VERSION=dev
RUN echo "$VERSION" > /app/VERSION

CMD ["python", "app.py"]
