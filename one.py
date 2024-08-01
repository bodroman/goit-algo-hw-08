import heapq

def min_cost_to_connect_cables(cable_lengths):
    """
    Обчислює мінімальні витрати на з'єднання мережевих кабелів.

    Параметри:
    cable_lengths (list[int]): Список довжин кабелів, які потрібно об'єднати.

    Повертає:
    int: Мінімальні витрати на з'єднання всіх кабелів.
    """
    # Ініціалізуємо мін-купу з вхідним списком кабелів
    heapq.heapify(cable_lengths)
   
    total_cost = 0
   
    # Повторюємо, поки не залишиться один кабель
    while len(cable_lengths) > 1:
        # Витягуємо два найкоротші кабелі
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
       
        # Об'єднуємо їх
        combined_length = first + second
       
        # Додаємо витрати на об'єднання до загальних витрат
        total_cost += combined_length
        
        # Додаємо новий кабель назад у купу
        heapq.heappush(cable_lengths, combined_length)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print(f"Мінімальні витрати на з'єднання кабелів: {min_cost_to_connect_cables(cables)}")
