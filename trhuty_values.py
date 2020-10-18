if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
if name:
    print("Hello, " + name)                 # isim girilmezse name(False) olur,
                                            # Çünkü boş string, if False ise
                                            # else komutu çalışır
else:
    print("Are you the man with no name")
