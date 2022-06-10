#!/bin/bash

LOG_FILE=$1

dir=$(dirname $0)
$dir/stop_bot.sh $LOG_FILE

if [ -n "$LOG_FILE" ]; then
    touch $LOG_FILE
    if [ ! -f "$LOG_FILE" ]; then
        echo "File $LOG_FILE does not exist"
    fi
fi

check_network() {
    inc=0
    until nc -z api.telegram.org 443; do 
        echo "api.telegram.org:443 unavailable. Waiting..."
        inc=$(($inc+1))
        if [ $inc -gt 120 ]; then
            echo "ERROR: api.telegram.org:443 unavailable"
        fi
        sleep 5
    done
}

if [ -z "$LOG_FILE" ] || [ ! -f "$LOG_FILE" ]; then
    check_network
    echo "Bot started"
    pushd $dir
    python3 -u $dir/mention_bot.py
    popd
else
    check_network 2>&1 | tee -a $LOG_FILE
    pushd $dir
    nohup python3 -u $dir/mention_bot.py >> $LOG_FILE 2>&1 &
    popd
    echo "Bot started" | tee -a $LOG_FILE
fi
