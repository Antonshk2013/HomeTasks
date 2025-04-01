#!/bin/bash
#Написать скрипт, который будет бесконечно пинговать указанный адрес (переменная или ввод пользователя)
#с интервалом 1 секунда между попытками.
#Если время пинга превышает 100 мс или не удается выполнить пинг в течение 3 последовательных отправок пакетов,
#скрипт просто выведет сообщения об этом.
if [ -z "$1" ]; then
    read -p "Укажите адрес рессурса " ADDRESS
else
    ADDRESS=$1
fi

# Счетчик неудачных пингов
fail_cnt=0

while true; do
    result=$(ping -c 1 "$ADDRESS" | grep 'time=')
    echo "$result"

    # Если пинг не удался, fail_cnt +=1
    if [ -z "$result" ]; then

        fail_cnt=$((fail_cnt + 1))
        echo "Нет Пинга #$fail_cnt."

        # Если 3 последовательных молчания, выводим сообщение
        if [ "$fail_cnt" -ge 3 ]; then
            echo "Нет соединения 3 попытки пройденгы $ADDRESS"
            fail_cnt=0

        fi
    else
        ping_time=$(echo "$result" | awk -F'time=' '{print $2}' | awk '{print $1}')
        if (( $(echo "$ping_time > 100" | bc -l) )); then
            echo "Время пинга выше установленного значения: $ping_time"
        fi
        fail_cnt=0
    fi

    sleep 1
done