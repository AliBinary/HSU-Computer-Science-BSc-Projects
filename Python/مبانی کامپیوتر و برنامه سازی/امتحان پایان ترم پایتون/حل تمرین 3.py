x = 16
y = 39.216
S1 = "x = %4d, y = %7.2f" % (x, y)
print(S1)

S2 = "x = %d, y = %6.5f" % (x, y)
print(S2)

S3 = "x = {0:d}, y = {1:6.3f}".format(x, y)
print(S3)
