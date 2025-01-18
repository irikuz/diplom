# Визуализация с использованием Plotly
# КРУГОВАЯ ДИАГРАММА
import pandas as pd
import plotly.express as px


class Graph:
    """Класс для визуализации графиков.

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
        """Построение графика и его отображение.

        Использует Plotly для создания круговой диаграммы на основе
        переданных данных и отображает график.
        """
        fig = px.pie(self.y_data, names=self.x_data, values=self.y_data, title=self.title)
        fig.show()


# Запускаем код
if __name__ == "__main__":
    # Загружаем датасет Bitcoin в массив pandas
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