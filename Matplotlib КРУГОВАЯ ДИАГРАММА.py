# Визуализация с использованием Matplotlib
# КРУГОВАЯ ДИАГРАММА
import pandas as pd
from matplotlib import pyplot as plt


class Graph:
    """Класс для визуализации круговых диаграмм.

    Атрибуты:
        title (str): Заголовок графика.
        x_label (str): Название оси X (не используется в круговой диаграмме, но оставлено для совместимости).
        y_label (str): Название оси Y (не используется в круговой диаграмме, но оставлено для совместимости).
        x_data (list): Данные для меток (отображаются на диаграмме).
        y_data (list): Данные для значений (размеры секторов диаграммы).
    """

    def __init__(self, title, x_label, y_label, x_data, y_data):
        """Инициализация класса Graph.

        Args:
            title (str): Заголовок графика.
            x_label (str): Название оси X.
            y_label (str): Название оси Y.
            x_data (list): Данные для меток.
            y_data (list): Данные для значений.
        """
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.x_data = x_data
        self.y_data = y_data

    def plot(self):
        """Создание и отображение круговой диаграммы.

        Использует Matplotlib для построения круговой диаграммы на основе
        переданных данных и отображает график с заданным заголовком.
        """
        # Создание круговой диаграммы
        plt.figure(figsize=(8, 6))
        # Рисуем график согласно переданным переменным y и x
        plt.pie(self.y_data, labels=self.x_data, autopct='%1.1f%%', startangle=140)
        # Название графика
        plt.title(self.title)
        # Рисуем график
        plt.show()


# Пример использования класса
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