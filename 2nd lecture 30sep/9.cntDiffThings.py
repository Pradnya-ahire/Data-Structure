text = "Hellow World!!"


cons = 0
vow = 0
chars = 0
num =0

for ch in text:
    if ch.isalpha():
        if ch.lower() in 'aeiou':
            vow = vow+1

        else:
            cons =cons+1

    elif ch.isdigit():
        num = num +1

    else:
        chars = chars + 1

print(cons)
print(num)

print(vow)
print(chars)



    