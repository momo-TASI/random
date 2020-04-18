import random

r = random.randint(1, 100)
i = 5
while True:
	i = i - 1
	rand = input ('請輸入數字: ')
	rand = int(rand)
	if rand == r :
		print('恭喜你猜對了')
		break
	elif rand > r:
		print('比答案大')
	elif rand < r:
		print('比答案小')