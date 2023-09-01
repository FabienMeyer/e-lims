FROM ubuntu:latest as elims-base

# Install linux dependencies
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        build-essential \
        curl \
        git \
        libbz2-dev \
        libffi-dev \
        liblzma-dev \
        libncurses5-dev \
        libncursesw5-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        llvm \
        make \
        tk-dev \
        wget \
        xz-utils \
        zlib1g-dev

# Install Pyenv
RUN curl https://pyenv.run | bash
ENV PATH="/root/.pyenv/bin:$PATH"
RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \
    exec $SHELL

# Install Python 3.11.4
ENV PYTHON_VERSION=3.11.4
RUN pyenv install ${PYTHON_VERSION} && \
    pyenv global ${PYTHON_VERSION} && \
    pyenv local ${PYTHON_VERSION} && \
    pyenv rehash

# Install Poetry
ENV POETRY_HOME="/root/.poetry/bin"
RUN curl -sSL https://install.python-poetry.org | python3 - 
ENV PATH="$POETRY_HOME/bin:$PATH"

# Set working directory
WORKDIR /app
COPY pyproject.toml /app/

# Project initialization:
RUN poetry config virtualenvs.in-project true && \
    poetry config virtualenvs.create true && \
    poetry env use /root/.pyenv/versions/${PYTHON_VERSION}/bin/python && \
    poetry install --no-dev --no-interaction --no-ansi
