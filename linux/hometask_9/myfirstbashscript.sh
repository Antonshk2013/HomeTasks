#!/bin/sh
USER=ANTON
date
echo "hello $USER"
echo "$PWD"
ps -ef | grep bioset | grep -v bioset| wc -l
ls -la /etc/passwd | awk '{print $1}'
