# Базовый класс Пицца
class Pizza:
    def __init__(self, name, dough, sauce, toppings, price):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} руб."

    def prepare(self):
        print(f"Готовим {self.name}: замешиваем тесто ({self.dough}), добавляем соус ({self.sauce}) и начинку: {', '.join(self.toppings)}.")

    def bake(self):
        print(f"{self.name} выпекается в печи.")

    def cut(self):
        print(f"{self.name} нарезается на кусочки.")

    def pack(self):
        print(f"{self.name} упаковывается в коробку.")


# Конкретные виды пиццы
class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__("Пепперони", "тонкое", "томатный", ["пепперони", "сыр"], 20)

class BarbecuePizza(Pizza):
    def __init__(self):
        super().__init__("Барбекю", "толстое", "барбекю", ["курица", "лук", "соус барбекю"], 25)

class SeafoodPizza(Pizza):
    def __init__(self):
        super().__init__("ТУН ТУН ТУН САХУР", "тонкое", "сливочный", ["креветки", "кальмары", "сыр"], 35)


# Класс Заказ
class Order:
    order_counter = 0

    def __init__(self):
        Order.order_counter += 1
        self.pizzas = []

    def __str__(self):
        return f"Заказ №{Order.order_counter}: {len(self.pizzas)} пицц(ы)"

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def total_price(self):
        return sum(pizza.price for pizza in self.pizzas)

    def execute(self):
        print("\nНачинаем приготовление заказа...")
        for pizza in self.pizzas:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.pack()
        print("Заказ готов!\n")


# Класс Терминал
class Terminal:
    def __init__(self):
        self.menu = [PepperoniPizza(), BarbecuePizza(), SeafoodPizza()]
        self.order = Order()
        self.display_menu = True

    def __str__(self):
        return f"Терминал | Текущий заказ: {self.order}"

    def show_menu(self):
        print("\nМеню пицц:")
        for i, pizza in enumerate(self.menu, 1):
            print(f"{i}. {pizza}")

    def handle_selection(self, index):
        if 1 <= index <= len(self.menu):
            selected_pizza = self.menu[index - 1]
            self.order.add_pizza(selected_pizza)
            print(f"Пицца '{selected_pizza.name}' добавлена в заказ.")
        else:
            print("Неверный номер пиццы.")

    def accept_payment(self):
        total = self.order.total_price()
        print(f"\nСумма к оплате: {total} руб.")
        input("Нажмите Enter для оплаты... ")
        print("Оплата принята.")
        self.order.execute()


# Консольный интерфейс
def run_terminal():
    terminal = Terminal()
    terminal.show_menu()

    while True:
        print("\nКоманды:")
        print("1 - Добавить пиццу в заказ")
        print("2 - Подтвердить заказ и оплатить")
        print("0 - Отменить заказ и выйти")

        command = input("Введите команду: ")

        if command == "1":
            try:
                index = int(input("Введите номер пиццы из меню: "))
                terminal.handle_selection(index)
            except ValueError:
                print("Ошибка: введите числовое значение.")
        elif command == "2":
            if not terminal.order.pizzas:
                print("Сначала добавьте пиццу в заказ.")
            else:
                terminal.accept_payment()
                break
        elif command == "0":
            print("Заказ отменён. До свидания!")
            break
        else:
            print("Неизвестная команда. Повторите ввод.")

# Точка входа
if __name__ == "__main__":
    run_terminal()
    input()
