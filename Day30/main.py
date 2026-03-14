try:
    file = open("config.txt", "r")
except FileNotFoundError:
    file = open("config.txt", "w")
else:
    print(file.read())
finally:
    file.close()
    raise KeyError("haha")