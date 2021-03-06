# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](https://github.com/EvgenyRomanov/home_task_mod8_9.1/blob/main/README.md#описание-проекта)  
[2. Какой кейс решаем?](https://github.com/EvgenyRomanov/home_task_mod8_9.1/blob/main/README.md#какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/EvgenyRomanov/home_task_mod8_9.1/blob/main/README.md#краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/EvgenyRomanov/home_task_mod8_9.1/blob/main/README.md#этапы-работы-над-проектом)  
[5. Результат](https://github.com/EvgenyRomanov/home_task_mod8_9.1/blob/main/README.md#результаты)    
[6. Выводы](https://github.com/EvgenyRomanov/home_task_mod8_9.1/blob/main/README.md#выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](https://github.com/EvgenyRomanov/home_task_mod8_9.1/blob/main/README.md#оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за количество попыток < 20.

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений.

**Что практикуем**     
Учимся писать хороший код на python.


### Краткая информация о данных
В ходе решения задачи используем целые цисла в диапазоне от 1 до 1000.
  
:arrow_up:[к оглавлению](https://github.com/EvgenyRomanov/home_task_mod8_9.1/blob/main/README.md#оглавление)


### Этапы работы над проектом  
- Создание функции, которая ищет переданное в нее число и возвращает кол-во попыток.
- Создание функции, которая принимает в качестве аргумента вышеуказанную функцию, применяет ее к каждому элементу списка из 1000 рандомных чисел
и возвращает среднее среднее кол-во попыток.

:arrow_up:[к оглавлению](https://github.com/EvgenyRomanov/home_task_mod8_9.1/blob/main/README.md#оглавление)


### Результаты:  
[Jupyter Notebook](https://github.com/EvgenyRomanov/home_task_mod8_9.1/blob/main/game_book.ipynb)

:arrow_up:[к оглавлению](https://github.com/EvgenyRomanov/home_task_mod8_9.1/blob/main/README.md#оглавление)


### Выводы:  
Сокращаяя диапазон поиска числа в два раза с каждой итерацией, можно значительно сократить время поиска или кол-во попыток найти число.

:arrow_up:[к оглавлению](https://github.com/EvgenyRomanov/home_task_mod8_9.1/blob/main/README.md#оглавление)
