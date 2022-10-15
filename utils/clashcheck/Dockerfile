FROM python:3

LABEL maintainer="yusteven@duck.com"

# init nginx procps/pkill
RUN apt update && \
    apt install -y --no-install-recommends nginx procps && \
    # remove apt cache
    rm -rf /var/lib/apt/lists/* 

WORKDIR /home/local

# port
EXPOSE 80

# config nginx
COPY default.conf /etc/nginx/conf.d/default.conf

# install requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -q

COPY . .

# clashcheck with while
CMD [ "./start.sh" ]
