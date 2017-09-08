#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

cd  digest
# run Celery worker for our project digest with Celery configuration stored in Celeryconf
su -m myuser -c "celery worker -A digest.celeryconf --beat -Q  default -n default@%h"