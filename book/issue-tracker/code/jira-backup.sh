#!/bin/bash

echo "[$(date)] Reading database configuration..."
USER=$(cat /opt/jira/home/dbconfig.xml |xmllint --xpath '//username/text()' -)
export PGPASSWORD=$(cat /opt/jira/home/dbconfig.xml |xmllint --xpath '//password/text()' -)
HOST=$(cat /opt/jira/home/dbconfig.xml |xmllint --xpath '//url/text()' - |awk -F'/' '{print $3}' |awk -F':' '{print $1}')
PORT=$(cat /opt/jira/home/dbconfig.xml |xmllint --xpath '//url/text()' - |awk -F'/' '{print $3}' |awk -F':' '{print $2}')
DATABASE=$(cat /opt/jira/home/dbconfig.xml |xmllint --xpath '//url/text()' - |awk -F'/' '{print $4}')

echo "[$(date)] Database connection settings..."
echo "User: $USER"
echo "Pass: **********" #$PGPASSWORD"
echo "Host: $HOST"
echo "Port: $PORT"
echo "Database: $DATABASE"

echo "[$(date)] Cleanup previous backups..."
rm -fr /opt/jira/backup/*

echo "[$(date)] Backup database..."
pg_dump -h $HOST -p $PORT -U $USER $DATABASE |gzip > /opt/jira/backup/jira-database_$(date +%F).tar.gz

echo "[$(date)] Backup home directory..."
tar -jcf /opt/jira/backup/jira-home_$(date +%F).tar.bz2 --exclude-caches-all /opt/jira/home

echo "[$(date)] All done."