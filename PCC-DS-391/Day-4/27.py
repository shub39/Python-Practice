
number = input('Enter a number: ')
while True:
    try:
        number = int(number)
        break
    except:
        number = input('Please enter a number: ') 