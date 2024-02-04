FROM mariadb
WORKDIR /db1
COPY db1 ./db1
COPY ./nginx/my.conf /etc/nginx/conf.d/mysite.conf
RUN rm /etc/nginx/conf.d/default.conf
