# Визуализация с использованием Seaborn
# СТОЛБЧАТАЯ ДИАГРАММА
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


class Graph:
    """Класс для визуализации столбчатых диаграмм.

    Атрибуты:
        title (str): Заголовок графика.
        x_label (str): Название оси X.
        y_label (str): Название оси Y.
        x_data (list): Данные для оси X.
        y_data (list): Данные для оси Y.
    """

    def __init__(self, title, x_label, y_label, x_data, y_data):
        """Инициализация класса Graph.

        Args:
            title (str): Заголовок графика.
            x_label (str): Название оси X.
            y_label (str): Название оси Y.
            x_data (list): Данные для оси X.
            y_data (list): Данные для оси Y.
        """
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.x_data = x_data
        self.y_data = y_data

    def plot(self):
        """Создание и отображение столбчатой диаграммы.

        Использует Seaborn для построения столбчатой диаграммы на основе
        переданных данных и отображает график с заданными заголовком и подписями осей.
        """
        # Создаем график
        plt.figure(figsize=(15, 6))
        # Рисуем график согласно переданным переменным x и y
        sns.barplot(x=self.x_data, y=self.y_data)
        # Название графика
        plt.title(self.title)
        # Наименование оси X
        plt.xlabel(self.x_label)
        # Наименование оси Y
        plt.ylabel(self.y_label)
        # Добавляем сетку
        plt.grid(True)
        # Рисуем график
        plt.show()


# Запускаем код
if __name__ == "__main__":
    # Загружаем датасет Bitcoin в массив pandas
    # Ссылка на файл
    url = "/Users/Shared/Previously Relocated Items/Security/Рабочая/Pyton/pythonProject17/Bitcoin.csv"
    # Описание столбцов
    columns = [
        'Currency',
        'Date',
        'Closing Price (USD)',
        '24h Open (USD)',
        '24h High (USD)',
        '24h Low (USD)',
        'Change%'
    ]
    # Загрузка массива данных
    rates = pd.read_csv(url, header=1, names=columns, encoding='utf-8')

    # Фильтруем данные, отбираем только данные с коэффициентом 0.19
    subset = rates[rates['Change%'] >= 0.19]

    # Строим график, передаем необходимые переменные
    graph = Graph(
        title="Самые выгодные дни для продажи валюты",
        x_label="Дата",
        y_label="Коэффициент в %",
        x_data=subset['Date'],
        y_data=subset['Change%']
    )

    # Выводим график
    graph.plot()