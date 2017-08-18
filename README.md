# ENG Metaterminal is console terminal app for read data from COM-port
designed on python3 for Windows
# RU Metaterminal это консольное приложение для чтения логов из COM-порта
разработано на языке python3 для Windows

# ENG A short guide 
To use the application simply 
1) download the entire folder Metaterminal, 
2) install Windows interpreter Python 3, and then... 
3) double click the main file main.py data from the port will be read continuously, displayed on screen and written to a text file. 
4) If you need to configure the com port, it is at this stage still want to edit the file main.py.

# RU Короткое руководство 
Для использования приложения достаточно 
1) скачать всю папку Metaterminal, 
2) установить в систему Windows интерпретатор Питон 3 и затем...
3) запустить двойным щелчком главный файл main.py, данные из порта будут читаться постоянно, выводиться на экран и записываться в текстовый файл. 
4) Если нужно настроить com порт, то на данном этапе все еще следует редактировать файл main.py. 

# ENG default settings of COM-port
# RU настройки COM-порта по умолчанию 
- str_name_of_device:str = 'FindMe3'
- str_number_of_COM_port:str = 'COM4'
- str_name_of_folder_for_logs:str = 'logs'
- int_baudrate = 57600  # baudrate (int) – Baud rate such as 9600 or 115200 etc.
- int_bytesize = 8  # bytesize – Number of data bits. Possible values: FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS
- str_parity = 'N'  # parity – Enable parity checking. Possible values: PARITY_NONE, PARITY_EVEN, PARITY_ODD PARITY_MARK, PARITY_SPACE
- int_stopbits = 1  # stopbits – Number of stop bits. Possible values: STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO
- int_timeout = 5   # timeout (float) – Set a read timeout value.
- int_xonxoff = 0   # xonxoff (bool) – Enable software flow control.
- int_rtscts = 0    # rtscts (bool) – Enable hardware (RTS/CTS) flow control.

# Autor/Автор
- KonevDN@ya.ru
- https://vk.com/KonevDN