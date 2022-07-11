
def meta_dec(arg):

    def dec_example(func):

        def inner(list_of_numbers):
            if isinstance(list_of_numbers, int):
                return list_of_numbers ** list_of_numbers
            return [func(num) for num in list_of_numbers]
        return inner
    if callable(arg):
        return dec_example(arg)
    else:
        def dec(func):
            def inner_(list_of_numbers, a=arg):
                return[num ** a for num in list_of_numbers]
            return inner_
        return dec


@meta_dec
def power(a):
    return a ** a


nums = [1, 2, 3, 4, 5, 6]

print(power(nums))
