FROM ubuntu:16.04
MAINTAINER Weilong Hu <huweilong@whu.edu.cn>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y software-properties-common \
    #&& add-apt-repository ppa:nginx/stable
    && add-apt-repository ppa:nginx/development

RUN apt-get install -y \
    python3 python3-pip uwsgi-plugin-python3 \
    nginx supervisor \
    && apt-get clean
COPY nginx/flask.conf /etc/nginx/sites-available/
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY website/requirements.txt /var/www/app/requirements.txt

RUN mkdir -p /var/log/nginx/app /var/log/uwsgi/app /var/log/supervisor \
    && rm /etc/nginx/sites-enabled/default \
    && ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf \
    && echo "daemon off;" >> /etc/nginx/nginx.conf \
    && pip3 install -r /var/www/app/requirements.txt \
    && chown -R www-data:www-data /var/www/app \
    && chown -R www-data:www-data /var/log

RUN apt-get remove python3-pip -y && apt-get autoremove -y

CMD ["/usr/bin/supervisord"]
