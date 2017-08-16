# coding=utf-8

import os
import time, datetime
import serial.tools.list_ports

''' Глобальные переменные '''
# имена
str_name_of_device:str = 'FindMe3_delete'
str_number_of_COM_port:str = 'COM4'
str_name_of_folder_for_logs:str = 'logs'
# настройка COM-порта
int_baudrate = 57600  # baudrate (int) – Baud rate such as 9600 or 115200 etc.
int_bytesize = 8  # bytesize – Number of data bits. Possible values: FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS
str_parity = 'N'  # parity – Enable parity checking. Possible values: PARITY_NONE, PARITY_EVEN, PARITY_ODD PARITY_MARK, PARITY_SPACE
int_stopbits = 1  # stopbits – Number of stop bits. Possible values: STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO
int_timeout = 5   # timeout (float) – Set a read timeout value.
int_xonxoff = 0   # xonxoff (bool) – Enable software flow control.
int_rtscts = 0    # rtscts (bool) – Enable hardware (RTS/CTS) flow control.

''' Создание имени для лог-файла '''
time.sleep(1)      # дополнительная простая защита от создания одинаковых имен файла, тк имя содержит "секунду"
obj_current_time = datetime.datetime.now()
str_current_time = obj_current_time.strftime("%Y-%m-%d__%Hh%Mm%Ss____")
str_name_of_new_log_file = str_current_time + str_name_of_device + '.log'
str_complete_log_file_name = os.path.join(str_name_of_folder_for_logs, str_name_of_new_log_file)

''' Создание лог файла '''
obj_log_file = open(str_complete_log_file_name, mode='w', encoding='utf8', newline='\r\n')

''' Вывод спика имеющихся COM-портов '''
print("Список существующих COM-портов:")
list_of_ports = serial.tools.list_ports.comports()
for str_port_name in list_of_ports:
    print(str_port_name)
    obj_log_file.write(str(str_port_name) + '\r\n')
    obj_log_file.flush()
print(end='\r\n')

''' Настройка COM-порта '''
obj_com_port = serial.Serial()
obj_com_port.port = str_number_of_COM_port
obj_com_port.baudrate = int_baudrate
obj_com_port.bytesize = int_bytesize
obj_com_port.parity = str_parity
obj_com_port.stopbits = int_stopbits
obj_com_port.timeout = int_timeout
obj_com_port.xonxoff = int_xonxoff
obj_com_port.rtscts = int_rtscts

'''' Подключение к COM-порту  '''
try:
    # попытка открытия порта
    obj_com_port.open()
    # выдача сообщения об успешно  результате открытия и запись в файл
    str_message = "Успешное открытие порта %s;" % (str_number_of_COM_port)
    print(str_message)
    obj_log_file.write(str_message + '\r\n')
    obj_log_file.flush()
    str_message = "Логируемое устройство %s;" % (str_name_of_device)
    print(str_message+'\r\n')
    obj_log_file.write(str_message + '\r\n')
    obj_log_file.flush()

except:
    print(obj_com_port.is_open)
    str_message = "Не получилось подключиться к порту %s, возможно, он занят." % str_number_of_COM_port
    print(str_message)
    obj_log_file.write(str(str_message) + '\r\n')
    obj_log_file.flush()
    obj_com_port.close()
    obj_log_file.close()
    input()
    exit()

''' Проверка и создание папки для логов'''
if not os.path.exists('logs'):
    os.makedirs('logs')



''' Хитрое чтение из порта и формирование вспомогательных данных для прочитанных строк '''
int_number_of_line:int = 1
while True:
    obj_current_time = datetime.datetime.now()
    str_current_time = obj_current_time.strftime("%Y-%m-%d    %Hh%Mm%Ss")
    bytes_port_data:bytes = obj_com_port.readline()
    #str_port_data = str(bytes_port_data, 'utf-8', 'ignore')
    str_port_data = bytes_port_data.decode('cp1251','ignore')
    list_of_clear_strings_of_port_data = str_port_data.splitlines()
    for str_one_clear_string_from_port in list_of_clear_strings_of_port_data:
        str_complete_line = str(int_number_of_line).ljust(6, ' ') + ' '*8 + str_current_time + ' '*8 + str_one_clear_string_from_port
        print(str_complete_line, end='\r\n')
        obj_log_file.write(str_complete_line+'\r\n')
        obj_log_file.flush()
        int_number_of_line += 1
    time.sleep(1/30) # seconds для регулировки скорости вывода логов


obj_com_port.close()
obj_log_file.close()

