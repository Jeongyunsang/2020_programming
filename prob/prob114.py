#사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라. 단 255를 초과하는 경우 255를 출력해야 한다.
user = input("입력값: ")
num = 20 + int(user)
if num > 255:
    print(255)
else:
    print(num)