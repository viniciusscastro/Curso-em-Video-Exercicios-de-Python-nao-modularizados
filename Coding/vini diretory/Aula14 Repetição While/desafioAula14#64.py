c = s = q = 0
while c != 999:
    c = int(input('digite o {} numero'.format(q+1)))
    if c != 999:
        s +=c
        q +=1
print('foram digitados {} e a soma entre eles é {}'.format(q, s))