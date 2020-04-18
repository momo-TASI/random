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
	else:
 		print('猜錯囉')
 		if i > 0 :
 			print('還有' , i , '次機會')
 		if i == 0 :
 			break