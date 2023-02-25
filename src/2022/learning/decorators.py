def new_div(fun):
    def test(a, b):
        if (a < b):
            a, b = b, a
        return fun(a, b)

    return test


@new_div
def div(a, b):
    return a / b


# div = new_div(div)

value = div(2, 4)

print(value)
