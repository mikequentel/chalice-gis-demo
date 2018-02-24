#!/bin/bash
# WKDIR="$(dirname "$0")"
# eg: ./generate_routes.sh localhost postgres businesses restaurants
HOST=$1
USR=$2
DB=$3
TABLE=$4

if [ -z "${HOST}" ]; then
  echo "Specify host name."
  exit 1
fi

if [ -z "${USR}" ]; then
  echo "Specify user name."
  exit 1
fi

if [ -z "${DB}" ]; then
  echo "Specify database name."
  exit 1
fi

if [ -z "${TABLE}" ]; then 
  echo "Specify table name."
  exit 1
fi

SQL="select column_name from information_schema.columns where table_name='${TABLE}' order by column_name;"

echo $SQL | psql -h ${HOST} -U ${USR} --set ON_ERROR_STOP=on ${DB} --tuples-only
