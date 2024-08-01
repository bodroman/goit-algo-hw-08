import heapq

def merge_k_lists(lists):
    """
    Зливає k відсортованих списків в один відсортований список за допомогою мін-купу.

    Параметри:
    lists (list[list[int]]): Список відсортованих списків.

    Повертає:
    list[int]: Відсортований список, що містить всі елементи з вхідних списків.
    """
    min_heap = []
    
    # Ініціалізуємо мін-купу першими елементами кожного списку
    for i, lst in enumerate(lists):
        if lst:  # Перевірка, чи список не порожній
            heapq.heappush(min_heap, (lst[0], i, 0))
    
    result = []
    
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)
        
        # Якщо є наступний елемент у тому ж списку, додаємо його до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))
    
    return result

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
