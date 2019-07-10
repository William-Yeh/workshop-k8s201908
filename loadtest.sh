#!/bin/bash
#
# Ping for specified HTTP(S) endpoint continuously and display the status code.
#

TARGET=${1:-http://localhost:30080/api/todo}
DELAY_SECONDS=${2:-0.1}
i=0

while :
do
    status=`curl -o /dev/null -sw '%{http_code}' $TARGET`
    if [ $status == "200" ]
    then
        echo "$i:" $status
    else
        echo "$i:      " $status
    fi

    sleep $DELAY_SECONDS
    let "i++"
done
