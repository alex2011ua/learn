def calculate(data, findall):
    matches = findall(r"([abc])([-+]?)=([abc]?)([+-]?\d*)")  # Если придумать хорошую регулярку, будет просто
    for v1, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        # Если бы могло быть только =, вообще одной строкой все считалось бы, вот так:
        if s == '+':
            x = data.get(v2, 0) + int(n or 0)
            data[v1] = data[v1] + x
        elif s == '-':
            x = data.get(v2, 0) + int(n or 0)
            data[v1] = data[v1] - x
        else:
            data[v1] = data.get(v2, 0) + int(n or 0)
    return data
