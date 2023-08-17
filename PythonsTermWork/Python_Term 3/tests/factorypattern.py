class Pizza:
    def prepare(self):
        pass

class MargheritaPizza(Pizza):
    def prepare(self):
        print("Preparing Margherita Pizza")

class PepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing Pepperoni Pizza")

class VegetarianPizza(Pizza):
    def prepare(self):
        print("Preparing Vegetarian Pizza")

class PizzaFactory:
    def create_pizza(self, pizza_type):
        if pizza_type == "Margherita":
            return MargheritaPizza()
        elif pizza_type == "Pepperoni":
            return PepperoniPizza()
        elif pizza_type == "Vegetarian":
            return VegetarianPizza()

# Usage
factory = PizzaFactory()

pizza1 = factory.create_pizza("Margherita")
pizza2 = factory.create_pizza("Pepperoni")
pizza3 = factory.create_pizza("Vegetarian")

pizzas = [pizza1, pizza2, pizza3]

for pizza in pizzas:
    pizza.prepare()
