import random
# 2016003718 윤규민
# 가위바위보 코드

def main():
	com_finger = random.randrange(3) + 1
	for i in range(10):

		my_finger = int(input("가위(1), 바위(2), 보(3)를 내시오. : "))

		while not(my_finger == 1 or my_finger == 2 or my_finger ==3):
		    my_finger = int(input("가위(1), 바위(2), 보(3)를 내시오. : "))
		
		if(com_finger == 1):
			if(my_finger == 1):
				print("컴퓨터는 가위를 냈습니다. => 비김~ ")
			elif(my_finger == 2):
				print("컴퓨터는 가위를 냈습니다. => 이김~ ")
			elif(my_finger == 3):
				print("컴퓨터는 가위를 냈습니다. => 짐~ ")
		
		elif(com_finger == 2):
			if(my_finger == 1):
				print("컴퓨터는 바위를 냈습니다. => 짐~ ")
			elif(my_finger == 2):
				print("컴퓨터는 바위를 냈습니다. => 비김~ ")
			elif(my_finger == 3):
				print("컴퓨터는 바위를 냈습니다. => 이김~ ")
		
		elif(com_finger == 3):
			if(my_finger == 1):
				print("컴퓨터는 보를 냈습니다. => 이김~ ")
			elif(my_finger == 2):
				print("컴퓨터는 보를 냈습니다. => 짐~ ")
			elif(my_finger == 3):
				print("컴퓨터는 보를 냈습니다. => 비김~ ")
main()