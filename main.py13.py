'''lesson13'''
import csv
class Product:
    def __init__(self, name, product_type, price):
        if product_type not in ["coffee", "tea", "additional"]:
            raise ValueError("Тип може бути тільки 'coffee', 'tea' або 'additional'.")

        self.name = name
        self.product_type = product_type
        self.price = price

    def __str__(self):
        return f"Кава: {self.name}, ціна: {self.price}грн."


class Store:
    def __init__(self):
        self.products = []

    def import_products(self, file_name, quantity=5):
        try:
            with open(file_name, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name = row["Найменування"]
                    product_type = row["Тип"]
                    price = float(row["Ціна"])
                    for _ in range(quantity):
                        self.products.append(Product(name, product_type, price))
        except FileNotFoundError:
            print(f"Файл '{file_name}' не знайдено.")
        except Exception as e:
            print(f"Сталася помилка: {e}")

    def get_products_by_type(self, product_type):
        return [product for product in self.products if product.product_type == product_type]

    def get_total_value(self):
        return sum(product.price for product in self.products)

    def sell_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return product
        return None

    def combine_products(self, product1, product2):
        if product1.product_type == "coffee" and product2.product_type == "additional":
            combined_name = f"{product1.name} з {product2.name}"
            combined_price = product1.price + product2.price
            return Product(combined_name, "coffee", combined_price)
        elif product1.product_type == "additional" and product2.product_type == "coffee":
            combined_name = f"{product2.name} з {product1.name}"
            combined_price = product1.price + product2.price
            return Product(combined_name, "coffee", combined_price)
        else:
            raise ValueError("Об'єднання доступно тільки для 'coffee' та 'additional' продуктів.")


if __name__ == "__main__":
    coffee_shop = Store()
    coffee_shop.import_products("inventory.csv")

    print("Усі продукти:")
    for product in coffee_shop.products:
        print(product)

    print("\nКава:")
    coffee_products = coffee_shop.get_products_by_type("coffee")
    for product in coffee_products:
        print(product)

    total_value = coffee_shop.get_total_value()
    print(f"\nЗагальна вартість: {total_value}грн.")

    product_to_sell = coffee_shop.sell_product("Еспресо")
    if product_to_sell:
        print(f"\nПродано продукт: {product_to_sell}")
    else:
        print("\nТакого продукту немає на складі.")

    coffee = Product("Еспресо", "coffee", 27)
    milk = Product("Молоко", "additional", 10)
    latte = coffee_shop.combine_products(coffee, milk)
    print(f"\nОб'єднано: {latte}")