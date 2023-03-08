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

# def open_account():
#     print("계좌가 생성되었습니다.")
    
# open_account()

# def deposit(balance, money):
#     print("입금이 완료 되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료 되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("잔액이 부족합니다. 잔액은 {0}원 입니다.".format(balance))
#         return balance

# balance = 0
# balance = deposit(balance, 1000)
# print(balance)

# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
# print(balance)

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0
# balance = deposit(balance, 1000)

# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석")
# profile("김태호", 20)
# profile("김태호", 20, "자바")

# def profile(name, age, main_lang): # 키워드 인자 : name, age, main_lang
#     print(name, age, main_lang)

# # profile("유재석", 20, "파이썬")
# # profile("김태호", 25, "자바")

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")
# profile(name="김종국", age=30, main_lang="자바")

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end="")
#     print(lang1, lang2, lang3, lang4, lang5)
    
# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    
#     for lang in language:
#         print(lang, end=" ")
#     print()    
    
# profile("유재석", 25, "Python", "Java", "C", "C++", "C#", "Kotlin")
# profile("김태호", 20, "Kotlin")

# gun = 10

# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
    
# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

# def std_weight(height, gender):
#     if gender == "남자":
#         std_weight = height * height * 22
#         return(std_weight)
#     elif gender == "여자":
#             return height * height *21
            

# height = 175
# gender = "여자"            
# weight = round(std_weight(height / 100, gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# print("Python","Java","JavaScript", sep=",", end="?")
# print(" 무엇이 더 재밌을까요?")

# scores = {"수학":0, "영어":50, "코딩":100}         

# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")
            
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))
    
# print("{0:>10}".format(500))
# print("{0:_<10}".format(500))

#파일쓰기
# score_file = open("score.txt","w",encoding="utf8")   
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()
    
#파일에 내용 추가
# score_file = open("score.txt","a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

#파일 읽기
# score_file = open("score.txt","r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("result_log.txt","r")

# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     fin = line.find('CC:')
#     print(fin)
#     # lst = line.split("CC:")
#     # print(lst)
    
# 50개 파일 생성 및 내용 추가하기
# for num in range(1,51):
#     lines = ['- '+ str(num) + '주차 주간보고 -', '\n부서 : ', '\n이름 : ', '\n업무 요약 :']
# #    print(str(num) + "주차.txt")
#     f = open(str(num) + '주차.txt', 'w')
#     f.writelines(lines)
# f.close()
       
# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 : ")
        
# name = "마린"
# hp = 40
# damage = 5

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {0}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# import requests
# from bs4 import BeautifulSoup

# # Set the headers to mimic a browser request
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# # Make a request to the webpage with headers
# url = "https://www.amazon.com/gp/bestsellers/electronics/3411001/ref=pd_zg_hrsr_electronics"
# response = requests.get(url, headers=headers)

# # Parse the HTML content using Beautiful Soup
# soup = BeautifulSoup(response.content, 'html.parser')

# # Find all the product items
# product_items = soup.find_all('div', {'class': 'a-section a-spacing-none p13n-asin'})

# # Loop through each product item and extract the product details
# for item in product_items:
#     # Extract the product name
#     product_name = item.find('span', {'class': 'a-size-small a-color-base'}).text.strip()
#     # Extract the star rating
#     star_rating = item.find('span', {'class': 'a-icon-alt'}).text.strip()
#     # Extract the price
#     price = item.find('span', {'class': 'p13n-sc-price'}).text.strip()
#     # Print the product details
#     print("Product Name: ", product_name)
#     print("Star Rating: ", star_rating)
#     print("Price: ", price)
#     print("-" * 50)

# import requests
# from bs4 import BeautifulSoup

# # Set the headers to mimic a browser request
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# # Make a request to the webpage with headers
# url = "https://www.amazon.com/gp/bestsellers/electronics/3411001/ref=pd_zg_hrsr_electronics"
# response = requests.get(url, headers=headers)

# # Parse the HTML content using Beautiful Soup
# soup = BeautifulSoup(response.content, 'html.parser')

# print(soup)

# # # Find all the product names using the provided class
# # product_names = soup.find_all('span', {'class': '_cDEzb_p13n-sc-css-line-clamp-3_g3dy1'})

# # # Loop through each product name and print it
# # # for name in product_names:
# # #     print(name.text.strip())

# # print(product_names)

# # /html/body/div[1]/div[3]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/a[2]/span/div
# # //*[@id="B07C2QHTTZ"]/a[2]/span/div

import requests
from bs4 import BeautifulSoup

# Set the headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Make a request to the webpage with headers
url = "https://www.amazon.com/gp/bestsellers/electronics/3411001/ref=pd_zg_hrsr_electronics"
response = requests.get(url, headers=headers)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

print(soup, 'w', file='error.txt')

# # Find all the product names using the provided class
# product_names = soup.find_all('div', {'class': 'p13n-sc-truncated'})

# print(product_names)

# # Loop through each product name and print it
# for name in product_names:
#     print(name.text.strip())
