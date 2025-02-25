# Сравнение различных библиотек для визуализации данных: Matplotlib, Seaborn и Plotly

## Описание проекта

Этот проект предназначен для сравнения трех популярных библиотек для визуализации данных в Python: Matplotlib, Seaborn и Plotly. Мы анализируем их ключевые характеристики, чтобы помочь пользователям выбрать наиболее подходящую библиотеку для своих нужд в визуализации данных.

Цель исследования: Создать набор визуализаций с использованием Matplotlib, Seaborn и Plotly, сравнить их функциональность и удобство использования.

Задачи исследования:

Изучить основные функции и возможности библиотек Matplotlib, Seaborn и Plotly.

Создать набор визуализаций с использованием каждой из библиотек.

Сравнить функциональность библиотек, включая поддержку различных типов графиков, возможность настройки стилей и параметров, интеграцию с другими инструментами и т.д.

Оценить удобство использования каждой библиотеки, учитывая такие факторы, как простота установки, наличие документации и примеров, поддержка сообщества и т.п.

Проанализировать результаты сравнения и сделать выводы о том, какая библиотека наиболее подходит для решения конкретных задач визуализации данных.
## Демонстрация работы кода

Примеры работы кода на основе использования трех популярные библиотек для визуализации данных в Python: Matplotlib, Seaborn и Plotly. 

Столбчатая диаграмма (Column Chart) Цель: Сравнение категорий. Применение: Подходит для визуализации категорийных данных, когда их количество превышает пять. 

![Визуализация с использованием Matplotlib СТОЛБЧАТАЯ ДИАГРАММА](https://github.com/user-attachments/assets/c7f3f1a3-bd45-4e8d-b20b-ea32415984ea)
Визуализация с использованием Matplotlib
![Визуализация с использованием Seaborn  СТОЛБЧАТАЯ ДИАГРАММА](https://github.com/user-attachments/assets/7ce6fc0b-e47a-427a-ba3f-b7e637f6670c)
Визуализация с использованием Seaborn
![Plotly СТОЛБЧАТАЯ ДИАГРАММА](https://github.com/user-attachments/assets/bfc377cd-2dca-4927-9d32-77b45dd9b4f7)
Визуализация с использованием Plotly

Линейная диаграмма (Line Chart) Цель: Отображение динамики изменений. Применение: Полезна для представления данных во времени

![Визуализация с использованием Matplotlib  ЛИНЕЙНЫЙ ГРАФИК](https://github.com/user-attachments/assets/efbe0ce2-5637-4574-a273-56aa50bfbe44)
Визуализация с использованием Matplotlib
![Визуализация с использованием Seaborn ЛИНЕЙНЫЙ ГРАФИК](https://github.com/user-attachments/assets/cc313c33-a3c3-49de-9cc1-eec72bd81a27)
Визуализация с использованием Seaborn
![Plotly ЛИНЕЙНЫЙ ГРАФИК](https://github.com/user-attachments/assets/cbda1213-ee1b-49c5-89fa-c41d18b13c45)
Визуализация с использованием Plotly

Круговая диаграмма (Pie Chart) Цель: Показать доли в целом. Применение: Эффективна для представления небольшого количества категорий (обычно до пяти)

![Визуализация с использованием Matplotlib  КРУГОВАЯ ДИАГРАММА](https://github.com/user-attachments/assets/16b082a6-0e13-4d07-835e-7a1985583aef)
Визуализация с использованием Matplotlib

![Plotly КРУГОВАЯ ДИАГРАММА](https://github.com/user-attachments/assets/e07354e0-508c-4fe6-8521-43ce01cbc489)
Визуализация с использованием Plotly

Гистограмма (Histograms) Цель: Сравнение частот и распределений. Применение: Идеальна для визуализации данных с частыми колебаниями, например, изменения курсов валют, где важно видеть колебания.
![Визуализация с использованием Seaborn ГИСТОГРАММА](https://github.com/user-attachments/assets/aadac106-a559-4287-85a9-a677b120599c)
Визуализация с использованием Seaborn

## Установка проекта

Следуйте этим шагам для установки проекта:

1. **Клонируйте проект с GitHub:**

   ```bash
   git clone https://github.com/irikuz/diplom.git
   ```

2. **Создайте виртуальное окружение:**

   ```bash
   python -m venv venv
   ```

3. **Активируйте виртуальное окружение:**

   - Для macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - Для Windows:

     ```bash
     venv\Scripts\activate
     ```

4. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Установите необходимые библиотеки:**

   - **Библиотека Matplotlib:**

     ```bash
     pip install matplotlib
     ```

   - **Библиотека Seaborn:**

     ```bash
     pip install seaborn
     ```

   - **Библиотека Plotly:**

     ```bash
     pip install plotly
     ```

   - **Библиотека Pandas:**

     ```bash
     pip install pandas
     ```

## Таблица, объединяющая основные характеристики библиотек Matplotlib, Seaborn и Plotly:

| **Особенность**                          | **Matplotlib**                                   | **Seaborn**                                   | **Plotly**                                      |
|------------------------------------------|-------------------------------------------------|------------------------------------------------|-------------------------------------------------|
| **Простота использования**               | Средняя, требует параметры для кастомизации     | Высокая, очень удобно для работы с минимумом кода | Очень высокая, простой синтаксис, поддержка интерактивности |
| **Поддержка интерактивности (web разработки)** | Нет, нужны дополнительные библиотеки             | Нет                                            | Да                                              |
| **Типы графиков**                       | Все стандартные типы графиков                    | Статистические графики                         | Интерактивные (web) и 3D графики               |
| **Анимация**                            | Нет                                             | Нет                                            | Да, поддержка через динамические данные         |
| **Сложность графиков**                  | Высокая (много настроек)                        | Низкая (готовые стили, функции и цветовые шаблоны) | Средняя (для базовых графиков)                  |
| **Использование с Pandas**              | Хорошо                                          | Отлично                                       | Хорошо                                          |
| **Настройка графиков**                  | Очень высокая                                   | Средняя                                       | Средняя                                        |
| **Производительность**                   | Хорошо для малых и средних объемов данных      | Хорошо для статистических графиков            | Хорошая, но может снижаться при работе с большими объемами данных |
| **Визуальное оформление**                | Базовое                                        | Очень красивое по умолчанию                   | Высококачественное, но требует больше ресурсов  |
| **Подходит для**                        | Простейших и сложных графиков                   | Статистических данных                          | Интерактивных (web) и динамичных графиков, поддержка JavaScript |
| **Масштабируемость**                    | Высокая                                        | Средняя                                       | Высокая                                        |
| **Удобство использования**               | Средняя                                        | Высокая                                       | Очень высокая                                   |

Данная таблица представляет собой сравнительный анализ трех популярных библиотек для визуализации данных в Python: Matplotlib, Seaborn и Plotly. Она охватывает ключевые характеристики каждой библиотеки, что позволяет пользователям быстро оценить их возможности и выбрать наиболее подходящую для своих нужд. 
