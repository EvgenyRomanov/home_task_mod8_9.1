import numpy as np


def random_predict(number: int = 1) -> int:
    """Угадываем число.

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: количество попыток.
    """
    
    count = 0
    # Начальное значение диапазона.
    start_num = 1
    # Конечное значение диапазона.
    end_num = 100
    
    while True:
        count += 1
        # С каждой итерацией будет сокращать дипазон поиска в 2 раза.   
        mean = (start_num + end_num) // 2  
        
        if end_num - start_num > 3 :
            # Предполагаемое число.
            predict_number = mean 
                                      
            if predict_number < number:
                start_num = predict_number
            elif predict_number > number:
                end_num = predict_number
            elif number == predict_number:
                break  
        else:
            # Когда максимально сократили диапазон до 3 чисел,
            # у нас остается всего два варианта.
            predict_number = mean
            
            if predict_number > number:
                predict_number -= 1
            elif predict_number < number:
                predict_number += 1
            if number == predict_number:
                # Выходим из цикла, если угадали.
                break
            
    return count


def score_game(random_predict) -> int:
    """Среднее кол-во попыток угадать число при 1000 повторений. 

    Args:
        random_predict (function): функция, которая угадывает число.

    Returns:
        int: среднее количество попыток.
    """
    
    count_ls = []
    # Фиксируем сид для воспроизводимости.
    # np.random.seed(1)  
    
    # Загадали список чисел.
    random_array = np.random.randint(1, 101, size=(1000))  

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток.")
    
    return score


if __name__ == "__main__":
    score_game(random_predict)
