import random

r = random.randint(1, 100)
i = 0
while True:
	i += 1 # i = i + 1
	rand = input ('請輸入數字: ')
	rand = int(rand)
	if rand == r :
		print('恭喜你猜對了')
		print('這是你猜的第' , i , '次')
		break
	elif rand > r:
		print('比答案大')
	elif rand < r:
		print('比答案小')
	print('這是你猜的第' , i , '次')