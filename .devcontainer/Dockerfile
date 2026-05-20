FROM buildpack-deps:trixie-curl

ENV TZ=UTC

ENV LANG=C.UTF-8
ENV LANGUAGE=C.UTF-8
ENV LC_ALL=C.UTF-8

RUN apt-get update -y && \
    apt-get install sudo-rs git starship vim locales locales-all bash-completion -y && \
    rm -rf /var/lib/apt/lists/* && \
    ln -s /usr/bin/sudo-rs /usr/bin/sudo

RUN groupadd -g 1000 dev && \
    useradd -m -u 1000 -s /bin/bash -g dev dev && \
    passwd -d dev

RUN echo "dev ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
