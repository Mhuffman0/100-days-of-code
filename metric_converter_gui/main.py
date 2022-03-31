def calculate(n, **kwargs):
    # return [{key: value} for (key, value) in kwargs.items()]
    return n + kwargs["add"], n * kwargs["multiply"]


print(calculate(2, add=5, multiply=7))
