# Закаблукова Анастасия Эдуардовна ИВТ-1.1
## Лабораторная работа №1. Реализация удаленного импорта.

Первый шаг.  
Создать файл *myremotemodule.py*, который будет импортироваться и разместить его в каталоге *rootserver*.  
![](image_report/pic1.png)

Второй шаг.  
Разместить в этом файле код.  
![](image_report/pic2.png)

Третий шаг.  
Создать файл *activation_script.py*, который будет содержать функцию url_hook и классы URLLoader и URLFinder.  
![](image_report/pic3.png)

Четвертый шаг.  
Запускаем сервер.  
![](image_report/pic4.png)

Пятый шаг.  
Запускаем файл *activation_script.py*.  
![](image_report/pic5.png)

Импортируем модуль.  
![](image_report/pic9.jpg)

Шестой шаг.  
Добавляем путь, где располагается модуль в *sys.path*.  
![](image_report/pic6.png)  
![](image_report/pic7.png)

Седьмой шаг.  
Импортируем файл *myremotemodule.py*, в котором размещена функция *myfoo*.  
![](image_report/pic8.png)

Восьмой шаг.  
Используя в качестве источника модуля github pages.  
![](image_report/pic10.png)  
![](image_report/pic11.png)  

Девятый шаг.  
![](image_report/pic12.png) 
