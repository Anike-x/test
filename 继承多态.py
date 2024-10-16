class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_describe(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def __str__(self):
        return self.get_describe()

    def fill_gas(self):
        print("加满油了")


# 重写方法实现多态
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def fill_gas(self):
        print("没有油箱")


my_new_car = Car('audi', 'a4', 2016)
my_new_car.fill_gas()
new_car = ElectricCar('tesla', 'model s', 2016)
new_car.fill_gas()
print(my_new_car.get_describe())
print(new_car.get_describe())
