driving = input('請問你有沒有開過車?')
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗')
	else:
		print('奇怪 你怎麼會開過車')
elif driving == '沒有':
	if age >= 18:
		print('你可以去考駕照,怎不去考')
	else:
		print('再過幾年就可以考啦!')	
else:
	print('只能輸入有/沒有')		