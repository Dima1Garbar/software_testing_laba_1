class Formulas():
    def __init__(self, x):
        self.x = x

    def calculation(self):
        try:
            if self.x <= 1.783 or self.x >= 192.359:
                first_value = self.x ** 4 * 1.554 + self.x ** 3 * 3.859 - self.x ** 2 * 2.248 + self.x * 1.851
                second_value = self.x ** 3 * 2.498 - self.x ** 2 * 2.055 + self.x * 5.72
                third_value = self.x ** 2 * 1.948 + self.x * 3.572
                fourth_value = self.x * 4.314
                return first_value, second_value, third_value, fourth_value
        except TypeError:
            return "Error"
if __name__ == '__main__':
    F = Formulas("15")
    print(F.calculation())