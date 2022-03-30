import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    left_border = 1 # Левая граница области предсказания
    right_border = 101 # Правая граница области предсказания

    while True:
        count += 1
        predict_number = np.random.randint(left_border, right_border) # Предполагаемое число
        # Корректировка границ отгадывания
        if predict_number < number:
            left_border = predict_number 
        elif predict_number > number:
            right_border = predict_number
        if number == predict_number: # Условие выхода из цикла
            break 
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = []
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # Список загадываемых чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # Находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)