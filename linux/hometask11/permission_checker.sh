#!/bin/sh


#Работаем на сервере linux.itcareerhub.de
#Создать скрипт permission_checker.sh
#Сделать его исполняемым.
#Создать Cкрипт , который получит список прав на файлы внутри директории /opt/ВАШАГРУППА, и если среди них есть файлы sh , то добавит им права на исполнение.
echo "Start script"
# Получаем из вне переменную для определения положения папки
echo "Первый аргумент: $1"
DIR_LOCATION=${1:-.}
FILE_LIST=$(ls -al $DIR_LOCATION | grep '.sh' | awk '{print $9}')

for line in $FILE_LIST ; do
    echo "$line"
    chmod +x "$DIR_LOCATION/$line"
    done
