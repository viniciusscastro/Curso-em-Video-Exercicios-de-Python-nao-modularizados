s = qn = 0
while True:
    n = int(input('digite um numero interiro(exceto 999)\n'))
    if n == 999:
        break
    s += n
    qn += 1
print(f'foram digitados {qn} numeros e a soma entre eles é {s}')