def fake_divide(first, second):
    if second == 0:
        return "Ошибка"
    else:
        return first / second

print(fake_divide(69, 3))
print(fake_divide(3, 0))