with open('pic.ppm', 'w') as f:
    f.write('P3\n256 256\n255\n')
    r = 64
    g = 0
    b = 210
    i = 0
    while i < 65536:
        f.write('{} {} {} '.format(r,g,b))
        g+=1
        g%=256
        i+=1
