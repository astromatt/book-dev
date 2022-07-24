FROM ubuntu

RUN apt update && apt install -y postgresql-10.5 postgresql-client-10.5
USER postgres

RUN /etc/init.d/postgresql start \
    && psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" \
    && createdb -O docker docker

# Adjust PostgreSQL configuration so that remote connections to the database are possible.
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/10.5/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/10.5/main/postgresql.conf

# information only
EXPOSE 5432
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

CMD ["/usr/lib/postgresql/10.5/bin/postgres", "-D", "/var/lib/postgresql/10.5/main", "-c", "config_file=/etc/postgresql/10.5/main/postgresql.conf"]
