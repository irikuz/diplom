# Визуализация с использованием Plotly
# ЛИНЕЙНЫЙ ГРАФИК
import pandas as pd
import plotly.graph_objects as go


class Graph:
    """Класс для визуализации линейных графиков.

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
        """Построение линейного графика и его отображение.

        Использует Plotly для создания линейного графика на основе
        переданных данных и отображает график с заданными заголовком и подписями осей.
        """
        # Рисуем график согласно переданным переменным x и y
        fig = go.Figure(data=go.Scatter(x=self.x_data, y=self.y_data, mode='lines+markers'))
        # Передаем название графика и наименование осей x и y
        fig.update_layout(title=self.title, xaxis_title=self.x_label, yaxis_title=self.y_label)
        # Рисуем график
        fig.show()


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