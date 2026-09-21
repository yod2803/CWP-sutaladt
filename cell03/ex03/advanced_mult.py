i = 0

while i <= 10:
    j = 0
    row = f"Table de: {i}:"
    while j <= 10:
        product = i * j
        row += f" {product}"
        j += 1
    print(row)
    i += 1