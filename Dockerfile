FROM python:3.12

WORKDIR /src

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY FreelanceMarket .

RUN chmod +x .