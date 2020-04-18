import random

r = random.randint(1, 100)

while True:
	rand = input ('請輸入數字: ')
	rand = int(rand)
	if rand == r :
		print('恭喜你猜對了')
		break
	else:
 		print('再來一次')