def bellman_ford(edges, num_vertices, start):
    """
    Алгоритм Беллмана-Форда для поиска кратчайших путей.

    :param edges: Список рёбер (u, v, w), где u - начальная вершина, v - конечная вершина, w - вес.
    :param num_vertices: Количество вершин в графе.
    :param start: Начальная вершина.
    :return: Кортеж (массив расстояний, флаг наличия отрицательного цикла).
    """
    # Инициализация
    distances = [float('inf')] * num_vertices
    distances[start] = 0

    # Релаксация рёбер num_vertices - 1 раз
    for _ in range(num_vertices - 1):
        for u, v, w in edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    # Проверка на отрицательные циклы
    for u, v, w in edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            return distances, True  # Обнаружен отрицательный цикл

    return distances, False  # Расстояния и отсутствие отрицательных циклов


# Примеры использования
if __name__ == "__main__":
    # Граф 1: Разреженный граф
    sparse_graph_edges = [
        (0, 1, 6),  # A -> B
        (0, 2, 7),  # A -> C
        (1, 2, 8),  # B -> C
        (1, 3, 5),  # B -> D
        (2, 3, -3),  # C -> D
        (3, 4, 9),  # D -> E
    ]
    print("Разреженный граф:")
    distances, has_negative_cycle = bellman_ford(sparse_graph_edges, 5, 0)
    print(f"Минимальные расстояния: {distances}, Отрицательный цикл: {has_negative_cycle}")

    # Граф 2: Граф с отрицательными весамиS
    negative_weights_edges = [
        (0, 1, 4),  # A -> B
        (0, 2, 5),  # A -> C
        (1, 3, -2),  # B -> D
        (2, 1, -6),  # C -> B
        (3, 4, 2),  # D -> E
    ]
    print("\nГраф с отрицательными весами:")
    distances, has_negative_cycle = bellman_ford(negative_weights_edges, 5, 0)
    print(f"Минимальные расстояния: {distances}, Отрицательный цикл: {has_negative_cycle}")

    # Граф 3: Граф с отрицательным циклом
    negative_cycle_edges = [
        (0, 1, 1),  # A -> B
        (1, 2, -1),  # B -> C
        (2, 3, -1),  # C -> D
        (3, 1, -1),  # D -> B (отрицательный цикл)
    ]
    print("\nГраф с отрицательным циклом:")
    distances, has_negative_cycle = bellman_ford(negative_cycle_edges, 4, 0)
    print(f"Минимальные расстояния: {distances}, Отрицательный цикл: {has_negative_cycle}")
