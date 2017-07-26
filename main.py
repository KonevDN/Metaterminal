# coding=utf-8

# coding=utf-8
import os
import time, datetime
import serial.tools.list_ports

'''
mass = [1,2,3,4,5,6]
for element in mass:
    print(element)
    if element == 3:
        mass.remove(element)
mass
print(mass)
'''

''' Проверка и создание папки для логов'''
if not os.path.exists('logs'):
    os.makedirs('logs')

''' Создание имени файла и самого файла  '''
time.sleep(1)      # дополнительная простая защита от создания одинаковых имен файла, тк имя содержит "секунду"
now = datetime.datetime.now()
str_current_time = now.strftime("%Y-%m-%d__%Hh%Mm%Ss____")
str_new_log_file_name = str_current_time +'FM3'+'.log'
str_complete_new_log_dir_and_file_name = os.path.join('logs',str_new_log_file_name)
objLogFile = open(str_complete_new_log_dir_and_file_name,'w')

''' Вывод спика имеющихся COM-портов '''
ports = serial.tools.list_ports.comports()
for port in ports:
    print(str(port))
    objLogFile.write(str(port)+'\r\n')  # .encode()
    objLogFile.flush()

''' Подключение к COM-порту и его настройка '''
ser = serial.Serial()
ser.port = 'COM4'
ser.baudrate = 57600
ser.bytesize = 8
ser.parity = 'N'
ser.stopbits = 1
ser.timeout = 60
ser.xonxoff = 0
ser.rtscts = 0
res = ser.open()

int_number_of_line = 0
while 1:
    int_number_of_line += 1
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d\t%Hh%Mm%Ss")
    # current_time = str(now.date()) + '\t' + str(now.hour) + 'h' + str(now.minute) + 'm' + str(now.second)+'s'
    # line = str(int_number_of_line) +'\t'+ current_time +'\t\t'+ str(ser.readline().decode('utf-8').strip())
    port_data:bytes = ser.readline()
    # port_data = ser.readline()
    # print("Bytes - `{0}`, string - `{1}`".format(repr(port_data), port_data.decode('utf-8')))
    #port_data = port_data.decode()
    port_data = str(port_data,'utf-8','ignore')
    line = str(int_number_of_line).ljust(6,' ') + '\t\t' + current_time + '\t\t' + str(port_data) #+ '\r\n'  # .decode('utf-8').strip()
    #print(line,end='')  # .encode('utf8')
    #line=line.strip()
    print(line)
    objLogFile.write(line)
    objLogFile.flush()

print(ser.is_open)
ser.close()
print(ser.is_open)
objLogFile.close()

