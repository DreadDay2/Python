import random
import time

number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)

while True:
    question = input('Czy chcesz wylosować numerek do odpytania ? (Tak/Nie) ')
    print(question)
    if question == 'Tak':
        los = random.choice(number)
        print(f'Wylosowany numerek to: {los}')
    elif question == 'Nie':
        print('Dobrze. Nie będę losował numerku do odpowiedzi.')
        time.sleep(2)
        break