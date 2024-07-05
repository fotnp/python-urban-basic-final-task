import csv


def read_file(filename: str) -> list[dict]:
    """
    Читает данные из CSV файла и преобразует их в список словарей.

    :param filename: Название файла, содержащего данные.
    :return: Список словарей с данными о домах.
    """
    with open(filename) as f:
        data = list(csv.DictReader(f))

    for d in data:
        d["floor_count"] = int(d["floor_count"])
        d["heating_value"] = float(d["heating_value"])
        d["area_residential"] = float(d["area_residential"])
        d["population"] = int(d["population"])

    return data


def classify_house(floor_count: int) -> str:
    """
    Классифицирует дом на основе количества этажей.

    Проверяет, является ли количество этажей целым числом и положительным значением.
    Возвращает категорию дома в зависимости от количества этажей.

    :param floor_count: Количество этажей в доме.
    :return: Категория дома в виде строки: "Малоэтажный", "Среднеэтажный" или "Многоэтажный".
    """
    if not isinstance(floor_count, int):
        msg = "Количество этажей должно быть целочисленным значением"
        raise TypeError(msg)

    if floor_count <= 0:
        msg = "Количество этажей должно быть положительным числом."
        raise ValueError(msg)

    if floor_count <= 5:
        return "Малоэтажный"
    elif 5 < floor_count <= 16:
        return "Среднеэтажный"
    else:
        return "Многоэтажный"


def get_classify_houses(houses: list[dict]) -> list[str]:
    """
    Классифицирует дома на основе количества этажей.

    :param houses: Список словарей с данными о домах.
    :return: Список категорий домов.
    """
    return [classify_house(house["floor_count"]) for house in houses]


def get_count_house_categories(categories: list[str]) -> dict[str, int]:
    """
    Подсчитывает количество домов в каждой категории.

    :param categories: Список категорий домов.
    :return: Словарь с количеством домов в каждой категории.
    """
    count_house_categories = {}
    for category in categories:
        if category not in count_house_categories:
            count_house_categories[category] = 1
        else:
            count_house_categories[category] += 1

    return count_house_categories


def min_area_residential(houses: list[dict]) -> str:
    """
    Находит адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.

    :param houses: Список словарей с данными о домах.
    :return: Адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.
    """
    min_avg_area = float("+inf")
    address = None
    for house in houses:
        current_avg_area = house["area_residential"] / house["population"]
        if current_avg_area < min_avg_area:
            min_avg_area = current_avg_area
            address = house["house_address"]

    return address


if __name__ == "__main__":
    houses_filename = "housing_data.csv"
    houses_data = read_file(houses_filename)

    house_categories = get_classify_houses(houses_data)
    count_categories = get_count_house_categories(house_categories)
    print(count_categories)

    house_address = min_area_residential(houses_data)
    print(house_address)
