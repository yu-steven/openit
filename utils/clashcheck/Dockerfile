FROM python:3

LABEL maintainer="yusteven@duck.com"

# init TimeZone
ENV TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive

RUN ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/*

# init nginx procps/pkill
RUN apt update && \
    apt install -y --no-install-recommends nginx procps && \
    # remove apt cache
    rm -rf /var/lib/apt/lists/* 

WORKDIR /home/local

# port
EXPOSE 80

# config nginx
COPY /config/default.conf /etc/nginx/conf.d/default.conf

# install requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -q

COPY . .

# clashcheck with while
CMD ["./start.sh"]
