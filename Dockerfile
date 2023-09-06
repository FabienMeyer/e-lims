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
ENV DEFAULT_PYENV_PYTHON=3.11.4
RUN pyenv install ${DEFAULT_PYENV_PYTHON} && \
    pyenv install 3.12-dev && \
    pyenv install 3.13-dev && \
    pyenv global ${DEFAULT_PYENV_PYTHON} && \
    pyenv local ${DEFAULT_PYENV_PYTHON} && \
    pyenv rehash

# Install Poetry
ENV POETRY_HOME="/root/.poetry/bin"
RUN curl -sSL https://install.python-poetry.org | python3 - 
ENV PATH="$POETRY_HOME/bin:$PATH"