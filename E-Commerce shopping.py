class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class cart:
    def __init__(self):
        self.__products = [] #Products Encapsulated

    def add_product(self, product):
        self.__products.append(product)
        print(f"{product} Product has been added!")

    def remove_product(self, product_name):
        for product in self.__products:
            if product.name == product_name:
                self.__products.remove(product)
                print(f"{product_name} removed from the cart")
                return        
        print(f"{product_name} not found in cart.")

    def calculate_total(self):
        total = 0
        for product in self.__products:
            total += product.price
        return total
        print(f"calculated_total => {total}")


    def show_cart(self):
        if not self.__products:
            print("Cart is empty")
        else:
            print("Cart contains:")
            for product in self.__products:
                print(f" {product.name}=> $ {product.price}")


        total = self.calculate_total()
        print(f"Total =>  ${total}")

p1 = product("phone", 40000)
p2 = product("Redmi Note 5", 20000)
p3 = product("Back Cover", 500)
cart = cart()
cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)
cart.calculate_total()
cart.show_cart()


cart.remove_product("Back Cover")
cart.show_cart()
        


