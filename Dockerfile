FROM python:3-slim

RUN apt-get update && apt-get install -y \
    libhdf5-dev \
    libhdf5-serial-dev \
    hdf5-tools \
    libjpeg-dev \
    zlib1g-dev \
    gcc \
    g++ \
    pkg-config \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    cmake \
    && rm -rf /var/lib/apt/lists/*

    WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./main.py"]
