# Імпорт необхідних бібліотек
import asyncio  # Асинхронні операції
import requests  # HTTP запити
from bs4 import BeautifulSoup  # Парсинг HTML
from invoke import task, Context  # Функціональність командної оболонки

# Клас, що представляє товар
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Клас для парсингу сторінки з товаром
class ProductParser:
    def parse(self, url):
        # Виконати HTTP GET запит до вказаного URL
        response = requests.get(url)
        # Створити об'єкт BeautifulSoup для парсингу HTML відповіді
        soup = BeautifulSoup(response.content, 'html.parser')

        # Знайти елемент з назвою товару
        name_element = soup.find('h1', {'class': 'product-name'})
        if name_element is None:
            # Якщо елемент не знайдено, вивести повідомлення про помилку та завершити функцію
            print(f"Error: Could not find product name for URL {url}")
            return None

        # Отримати текст знайденого елементу та видалити зайві пробіли
        name = name_element.text.strip()

        # Знайти елемент з ціною товару
        price_element = soup.find('span', {'class': 'price'})
        if price_element is None:
            # Якщо елемент не знайдено, вивести повідомлення про помилку та завершити функцію
            print(f"Error: Could not find product price for URL {url}")
            return None

        # Отримати текст знайденого елементу, видалити зайві пробіли та конвертувати у дійсне число
        price = float(price_element.text.strip().replace('$', ''))

        # Створити об'єкт класу Product з отриманими даними та повернути його
        return Product(name, price)

# Функція для асинхронного отримання інформації про товари з двох URL
@task
async def fetch_product(ctx, url):
    # Створити екземпляр класу ProductParser
    parser = ProductParser()
    # Викликати метод parse для отримання даних про товар за вказаним URL
    product = parser.parse(url)
    if product is not None:
        # Якщо дані про товар отримано успішно, вивести назву та ціну товару
        print(f'Product name: {product.name}')
        print(f'Product price: ${product.price:.2f}\n')

# Асинхронна функція для паралельного виклику функції fetch_product для кожного URL
async def main():
    # Список URL сторінок з товарами
    urls = [
        'https://deep.in.ua/?fbclid=PAAaYJJnkioOPB17MrQAUS2SYqtOTKUv2m1fqxmaYDUJY_VosSD3NINWArBS4',
        'https://zoho.in.ua/catalog/product/b619f4a8-25bb-4ad6-a8d1-1036db2c6b9d?size=OVERSIZE'
    ]

    # Створення контексту Invoke
    ctx = Context()
    # Створення списку асинхронних задач для обробки кожного URL
    tasks = [fetch_product(ctx, url) for url in urls]
    # Очікування завершення всіх асинхронних задач
    await asyncio.gather(*tasks)

# Перевірка, чи цей файл викликається як скрипт, а не імпортується як модуль
if __name__ == '__main__':
    # Запуск асинхронної функції main
    asyncio.run(main())
