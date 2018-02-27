#!/bin/bash
NAME=$1
if [ -z "${NAME}" ]; then
  echo "Include name of project."
  exit 1
fi
virtualenv --python $(which python) ~/.virtualenvs/$NAME
# source ~/.virtualenvs/chalice-demo/bin/activate
source ~/.virtualenvs/$NAME/bin/activate
pip install chalice
chalice new-project $NAME
