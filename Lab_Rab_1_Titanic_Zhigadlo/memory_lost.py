def memory_lost():
    try:
        # Создаем список, который будет расти до исчерпания доступной памяти
        memory_list = []
        while True:
            memory_list += [0] * 10**6  # Увеличиваем размер списка
    except MemoryError:
        print("Ошибка: Не хватает оперативной памяти")

memory_lost()
