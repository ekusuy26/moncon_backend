FROM mysql:8.0

ARG MYSQL_DATABASE \
    MYSQL_USER \
    MYSQL_PASSWORD \
    MYSQL_ROOT_PASSWORD

ENV MYSQL_DATABASE=/${MYSQL_DATABASE} \
    MYSQL_USER=/${MYSQL_USER} \
    MYSQL_PASSWORD=/${MYSQL_PASSWORD} \
    MYSQL_ROOT_PASSWORD=/${MYSQL_ROOT_PASSWORD} \
    TZ=Asia/Tokyo

COPY ./db_setting/my.cnf /etc/mysql/conf.d/my.cnf
RUN chmod 644 /etc/mysql/conf.d/my.cnf