#!/bin/sh

CMD=backend-sample-app.py
if [ ! -f "$CMD" ]; then
    echo "Please run '$0' from the same directory where '$CMD' file resides"
    exit 1
fi

CMD=$PWD/$CMD
PIDFILE=./backend-sample-app.pid
BACKEND_LOG_PATH=/var/log/nginx-ldap-auth/backend.log

. /etc/init.d/functions

start() {
    echo -n "Starting backend-sample-app: "
    if [ -s ${PIDFILE} ]; then
       RETVAL=1
       echo -n "Already running !" && warning
       echo
    else
       export BACKEND_LOG_PATH=$BACKEND_LOG_PATH
       nohup ${CMD} >/dev/null 2>&1 &
       RETVAL=$?
       PID=$!
       [ $RETVAL -eq 0 ] && success || failure
       echo
       echo $PID > ${PIDFILE}
    fi
}

case $1 in
    "start")
        start
    ;;
    "stop")
        echo -n "Stopping backend-sample-app: "
        killproc -p $PIDFILE $CMD
        unset BACKEND_LOG_PATH
        echo
    ;;
    *)
        echo "Usage: $0 <start|stop>"
    ;;
esac
