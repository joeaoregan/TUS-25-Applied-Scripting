message = "Hello world"

# Pythonic
for char in message:
    print(char)

# Not Pythonic
i = 0
while i < len(message):
    print(message[i])
    i += 1


# Pythonic
for i in range(10):
    pass

# Not Pythonic
i = 0
while i < 10:
    i += 1



playing = True

# Pythonic
while playing:
    pass

# Not Pythonic
while playing == True:
    pass



finished = False

# Pythonic
while not finished:
    pass

# Not Pythonic
while finished == False:
    pass



# Not Pyhonic
temperature = 85
pressure = 120
error_code = "E02"
shutdown_signal = False

while (temperature > 80 and pressure > 100 and error_code != "OK" and not shutdown_signal and len(error_code) > 1):
    print("System running despite multiple checks....")

    # Simulate system changes
    temperature -= 2
    pressure -= 5
    if temperature < 75:
        error_code = "OK"
    if pressure < 90:
        shutdown_signal = True


# Pythonic
while True:
    print("System running...")

    temperature -= 2
    pressure -= 5

    if temperature < 75 or pressure < 90:
        shutdown_signal = True

    if error_code == "OK" or shutdown_signal:
        break




# Pythonic
for i,char in enumerate(message):
    print(f"{i} {char}")

# Not Pythonic
for i in range(len(message)):
    print(f"{i} {message[i]}")