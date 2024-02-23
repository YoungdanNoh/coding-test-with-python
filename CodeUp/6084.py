h, b, c, s = map(int, input().split(' '))

storage = h*b*c*s
storage = storage/8/1024/1024

print("{0:.1f} MB".format(storage))