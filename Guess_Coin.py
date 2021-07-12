# Random Coin
import random
# x = coin ; o is head 1 is tail
x = random.randint(0, 1)

# guess
y = int(input('Head (Type 0) or Tail (Type 1) : '))

if x == y :
    print('True')
elif y != 0 and y != 1 :
    print('Only 0 and 1')
else :
    print(('False'))
