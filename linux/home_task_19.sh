#!/bin/bash

DIR_CR_FILE=/opt/091224-ptm/shkarupa/create_files
DIR_SORT_FILE=/opt/091224-ptm/shkarupa/sorted_files


[ -d "$DIR_CR_FILE" ] || mkdir -p "$DIR_CR_FILE"
[ -d "$DIR_SORT_FILE" ] || mkdir -p "$DIR_SORT_FILE"


for i in {1..100}; do
    touch "$DIR_CR_FILE/$i"
done

for f in $DIR_CR_FILE/*; do
    if [ $(( $(basename "$f" ) % 2 )) -eq 0 ]
 then
     	mv $f $DIR_SORT_FILE/
    fi
done
