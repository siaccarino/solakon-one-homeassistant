FROM ubuntu:24.04

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        git \
        python3 \
        python3-dev \
        python-is-python3 \
        python3-pip

# install the python packages system wide
# it is pointless to generate a python venv in a python devcontainer 
RUN pip install --no-input --break-system-packages \
    homeassistant \
    pymodbus \
    pytest \
    ruff

# map the host user to the container user
ARG UID=1000
ARG GID=1000
RUN if getent group $GID; then \
        groupmod -n developer $(getent group $GID | cut -d: -f1); \ 
    else \
        groupadd -g $GID developer; \ 
    fi && \
    if getent passwd $UID; then \ 
        OLD_USER=$(getent passwd $UID | cut -d: -f1); \ 
        usermod -l developer -g $GID $OLD_USER; \
    else \
        useradd -m -u $UID -g $GID developer; \ 
    fi

# allow sudo for the container user
RUN mkdir -p /etc/sudoers.d \
    && echo "developer ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/developer \
    && chmod 0440 /etc/sudoers.d/developer

# set up bash for the container user
COPY .bashrc /home/developer/.bashrc
RUN chsh -s /bin/bash developer

USER developer
