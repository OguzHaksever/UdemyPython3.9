for i in range (1,13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i** 2, i**3))
    # İki noktadan sonraki sayı karakter boşluğu sayısı, okumayı kolaylaştırmak için


print()

print("Pi is approximately {0:12}".format(22/7))         # General format, 15 decimals
print("Pi is approximately {0:12f}".format(22/7))        # floating point value, 6 digit decimal
print("Pi is approximately {0:<52.50f}".format(22/7))    # floating point format with 50 decimal precision
print("Pi is approximately {0:<62.50f}".format(22/7))    #
print("Pi is approximately {0:<72.50f}".format(22/7))    # Maximum precision is between 51 - 53 decimals
