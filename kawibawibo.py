import random
# 2016003718 ���Թ�
# ���������� �ڵ�

def main():
	com_finger = random.randrange(3) + 1
	for i in range(10):

		my_finger = int(input("����(1), ����(2), ��(3)�� ���ÿ�. : "))

		while not(my_finger == 1 or my_finger == 2 or my_finger ==3):
		    my_finger = int(input("����(1), ����(2), ��(3)�� ���ÿ�. : "))
		
		if(com_finger == 1):
			if(my_finger == 1):
				print("��ǻ�ʹ� ������ �½��ϴ�. => ���~ ")
			elif(my_finger == 2):
				print("��ǻ�ʹ� ������ �½��ϴ�. => �̱�~ ")
			elif(my_finger == 3):
				print("��ǻ�ʹ� ������ �½��ϴ�. => ��~ ")
		
		elif(com_finger == 2):
			if(my_finger == 1):
				print("��ǻ�ʹ� ������ �½��ϴ�. => ��~ ")
			elif(my_finger == 2):
				print("��ǻ�ʹ� ������ �½��ϴ�. => ���~ ")
			elif(my_finger == 3):
				print("��ǻ�ʹ� ������ �½��ϴ�. => �̱�~ ")
		
		elif(com_finger == 3):
			if(my_finger == 1):
				print("��ǻ�ʹ� ���� �½��ϴ�. => �̱�~ ")
			elif(my_finger == 2):
				print("��ǻ�ʹ� ���� �½��ϴ�. => ��~ ")
			elif(my_finger == 3):
				print("��ǻ�ʹ� ���� �½��ϴ�. => ���~ ")
main()