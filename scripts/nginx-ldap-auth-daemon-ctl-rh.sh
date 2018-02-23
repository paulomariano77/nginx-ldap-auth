#!/bin/sh

CMD=nginx-ldap-auth-daemon.py
if [ ! -f "$CMD" ]; then
    echo "Please run '$0' from the same directory where '$CMD' file resides"
    exit 1
fi

CMD=$PWD/$CMD
PIDFILE=./nginx-ldap-auth-daemon.pid
NGINX_AUTH_LOG_PATH=/var/log/nginx-ldap-auth/daemon.log

. /etc/init.d/functions

start() {
    echo -n "Starting ldap-auth-daemon: "
    if [ -s ${PIDFILE} ]; then
       RETVAL=1
       echo -n "Already running !" && warning
       echo
    else
       export NGINX_AUTH_LOG_PATH=$NGINX_AUTH_LOG_PATH
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
        echo -n "Stopping ldap-auth-daemon: "
        killproc -p $PIDFILE $CMD
        unset NGINX_AUTH_LOG_PATH
        echo
    ;;
    *)
        echo "Usage: $0 <start|stop>"
    ;;
esac
