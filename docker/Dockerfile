FROM selenium/standalone-chrome:114.0-chromedriver-114.0
USER root

# Install Python 3.13 from source
RUN apt-get update && apt-get install -y \
    wget build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev \
    libssl-dev libreadline-dev libffi-dev curl libbz2-dev \
    && wget https://www.python.org/ftp/python/3.13.0/Python-3.13.0.tgz \
    && tar -xf Python-3.13.0.tgz \
    && cd Python-3.13.0 && ./configure --enable-optimizations \
    && make -j"$(nproc)" && make altinstall \
    && cd .. && rm -rf Python-3.13.0 Python-3.13.0.tgz \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Make python3.13 the default
RUN ln -s /usr/local/bin/python3.13 /usr/bin/python && \
    ln -s /usr/local/bin/pip3.13 /usr/bin/pip

ENV DISPLAY=:99
WORKDIR /app

# Install Poetry and dependencies
COPY pyproject.toml poetry.lock* ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root

COPY . .

CMD ["python", "cli.py"]