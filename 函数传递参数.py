def add(a: int, b: int, c: int = 0):
    return a + b + c


def make_pizza(*toppings: str):  # 传递任意量实参
    print(toppings)


def make_dinner(size: int, *toppings: str):  # 先匹配位置实参和关键词实参，因此要放到*toppings前面，剩余的参数收集到最后形参
    print(size, toppings)


add(1, 2)
add(1, 2, 3)
make_pizza("pepperoni")
make_pizza("mushroom", "green peppers", "extra cheese")
make_dinner(10, "mushroom", "green peppers", "extra cheese")
