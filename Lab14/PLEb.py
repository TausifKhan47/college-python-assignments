class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price:.2f}")
        print("\n")


    def apply_discount(self, discount_percent):
        discount_amount = (discount_percent / 100) * self.price
        self.price -= discount_amount


book1 = Book("Python Programming", "John Smith", 500)
book2 = Book("Data Science Essentials", "Alice Johnson", 750)

print("Book Details (Before Discount):")
book1.display_details()
book2.display_details()

book2.apply_discount(10)

print("Book Details (After Applying 10% Discount on Book 2):")
book1.display_details()
book2.display_details()
