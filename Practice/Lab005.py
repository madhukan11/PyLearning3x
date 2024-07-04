def f1(a, b, c):
    return (a + b + c)


result = f1(30, 80, 120)
print(result)


def make_pizza(*toppings):
    return (toppings)


mk = make_pizza("onions", "mushroom", "corn")
print(mk)
rk = make_pizza("onions", "mushroom", "tamatoo")
print(rk)


def make_pizzas(*toppings, base):
    return (toppings, base)


mk = make_pizzas("onions", "mushroom", "corn", base="thin")
print(mk)
rk = make_pizzas("onions", "mushroom", "tamatoo", base="thick")
print(rk)
