with open('pic.ppm', 'w') as f:
    f.write('P3\n512 512\n512\n')
    r = 128
    g = 0
    b = 420
    i = 0
    while i < 262144:
        f.write('{} {} {} '.format(r,g,b))
        g+=1
        g%=512
        i+=1
