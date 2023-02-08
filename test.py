# station = "사당"

# print(station + " 행 열차가 들어오고 있습니다.")
import random
#from math import * #math 모듈의 모든 기능을 가져옴
import math

d1 = random.randint(4, 29)
#print(d1)
#print("오프라인 스터디 모임 날짜는 매월",  d1  ,"일로 선정되었습니다.")
#print(random.randint(1, 10))

# print(math.floor(4.99))
# print(math.ceil(3.14))
# print(int(math.sqrt(16)))

# print(random.randint(1, 45))
# print(random.randint(1, 45))
# print(random.randint(1, 45))
# print(random.randint(1, 45))
# print(random.randint(1, 45))

# date = random.randint(4, 28)

# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")

# #슬라이싱
# jumin = "990120-1234567"
# print("성별 : " + jumin[7])
# print("연 : ", jumin[0:2])
# print("월 : ", jumin[2:4])
# print("일 : ", jumin[4:6])
# print(jumin[:6])
# print(jumin[7:])
# print(jumin[:])
# print(jumin[-7:])

python = "Python is Amazing"

# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python","Java"))

#"n" 의 index 확인
# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# find = python.find("n")
# print(find)
# find = python.find("n", find + 1)
# print(find)
# #print(python.index("Java")) #에러 출력 후 프로그램 실행 중지
# print(python.find("Java")) #-1 출력 후 종료

# print(python.count("n"))

#문자열에 변수 추가
# print("문자열 %d 문자열" %3)
# print("문자열 %c 문자열" % "B")
# print("문자열 %s 문자열" % "A")
# print("나는 %s 살입니다." %20)
# print("나는 %s색과 %s색을 좋아해요" % ("파랑", "빨강"))

# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨강"))

# #f-string 방법
# age = 20
# color = "빨강"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# print("""
#       백문이 불여일견
#       백견이 불여일타""")
# print("백문이 불여일견\n백견이 불여일타")
# # print("저는 \"나도코딩\"입니다")
# print("c:\\windows\\system32")
# print(r"c:\windows\system32")

# 사이트 별 암호 생성 하기
#url = "http://naver.com"
#url = "http://daum.net"
# url = "http://google.com"
# url1 = url[7:]
# url2 = url1[:-4]
# print(url2)
# print(url2[:3],len(url2[:]),url2.count("e"), '!')

# 리스트
# subway = [10, 20, 30]
# print(subway)
# subway1 = ["유재석", "조세호", "박명수"]
# print(subway1)
# # print(subway1.index("조세호") +1)
# subway1.insert(1, "정형돈")
# print(subway1.pop())
# print(subway1)
# print(subway1.pop())
# print(subway1)
# print(subway1.pop())
# print(subway1)

# num_list = [5, 4, 2, 1, 3]
# print(num_list)
# num_list.sort()
# num_list.reverse()
# print(num_list)

# dictionary (key:value 쌍으로 관리, 리스트는 목록)
# cabinet = {3: "유재석", 100: "김태호"}
# # print(cabinet[3])
# # print(cabinet[100])
# # cab1 = cabinet.get(3)
# print(cabinet)
# print(cabinet.get(5, "사용가능")) #값이 없는 경우 정의 한 결과를 출력 함
# print(3 in cabinet) #3번 캐비넷을 사용 중인지 확인
# print(5 in cabinet) #5번 캐비넷을 사용 중인지 확인
# del cabinet[3] # 3번 삭제
# cabinet[2] = "하하"  # 사전에 2번 추가
# print(cabinet.keys()) # 사용중인 키 확인
# print(cabinet.values()) # 값만 출력
# print(cabinet.items()) # 키와 값을 함께 출력
# cabinet[1] = "김서연"
# print(cabinet)
# cabinet[10] = "김다연"
# print(cabinet)
# print(cabinet.get(1))
# print(cabinet.get(10))

def open_account():
    print("계좌가 생성되었습니다.")
    
open_account()

def deposit(balance, money):
    print("입금이 완료 되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료 되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("잔액이 부족합니다. 잔액은 {0}원 입니다.".format(balance))
        return balance
        


balance = 0
balance = deposit(balance, 1000)
print(balance)

balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
print(balance)
