FROM python:3.10

WORKDIR /app

# 🔥 Required system dependencies for tgcalls
RUN apt-get update && apt-get install -y \
    ffmpeg \
    build-essential \
    python3-dev \
    libffi-dev \
    libssl-dev

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
