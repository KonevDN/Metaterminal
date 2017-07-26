# coding=utf-8

import os
import time, datetime
import serial.tools.list_ports

''' Проверка и создание папки для логов'''
if not os.path.exists('logs'):
    os.makedirs('logs')

''' Создание имени лога файла '''
time.sleep(1)      # дополнительная простая защита от создания одинаковых имен файла, тк имя содержит "секунду"
obj_current_time = datetime.datetime.now()
str_current_time = obj_current_time.strftime("%Y-%m-%d__%Hh%Mm%Ss____")
str_new_log_file_name = str_current_time +'FM3'+'.log'
str_complete_log_file_name = os.path.join('logs', str_new_log_file_name)
''' Создание самого лог файла '''
obj_log_file = open(str_complete_log_file_name, 'w')

''' Вывод спика имеющихся COM-портов '''
list_of_ports = serial.tools.list_ports.comports()
for str_port_name in list_of_ports:
    print(str_port_name)
    obj_log_file.write(str(str_port_name) + '\r\n')
    obj_log_file.flush()

''' Подключение к COM-порту и его настройка '''
obj_com_port = serial.Serial()
obj_com_port.port = 'COM4'
obj_com_port.baudrate = 57600
obj_com_port.bytesize = 8
obj_com_port.parity = 'N'
obj_com_port.stopbits = 1
obj_com_port.timeout = 60
obj_com_port.xonxoff = 0
obj_com_port.rtscts = 0

try:
    tmp = obj_com_port.open()
except:
    print('could not open port')
    obj_log_file.close()
    print('fuck')
    exit(0)

int_number_of_line = 0
while True:
    int_number_of_line += 1
    obj_current_time = datetime.datetime.now()
    str_current_time = obj_current_time.strftime("%Y-%m-%d\t%Hh%Mm%Ss")
    bytes_port_data:bytes = obj_com_port.readline()
    str_port_data = str(bytes_port_data, 'utf-8', 'ignore')
    list_of_clear_strings_of_port_data = str_port_data.splitlines()
    for str_one_clear_string_from_port in list_of_clear_strings_of_port_data:
        str_complete_line = str(int_number_of_line).ljust(6, ' ') + '\t\t' + str_current_time + '\t\t' + str_one_clear_string_from_port
        print(str_complete_line)
        obj_log_file.write(str_complete_line+'\r\n')
        obj_log_file.flush()

print(obj_com_port.is_open)
obj_com_port.close()
print(obj_com_port.is_open)
obj_log_file.close()

