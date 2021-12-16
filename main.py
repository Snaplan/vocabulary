# _*_ coding: utf-8 _*_

"""
input()
입력: 안내 문구
리턴 값: 읽은 줄

ex) name =  input('이름을 입력하세요')
->이름을 입력하세요라는 멘트가 나오고 옆에 값을 치고 엔터를 치는 값을 string의 형태로 name에 저장

"""
"""
split()
입력: 일단 안 씀
리턴 값: 여백을 제외한 각 원소의 리스트 

ex) names = '한재인 한재하', numbers = '1 3'
<->names = ['한재인','한재하']   # names[0], names[1]

new_names = names.split() 
new_names = ['한재인','한재하'] 
new_numbers = numbers.split()
new_numbers = ['1','3']
1을 가져오고 싶다-> new_numbers[0], 3을 가져오고 싶다. new_numbers[1]
A = int(new_numbers[0]) # 1을 정수화
B = int(new_numbers[1]) # 3을 정수화
"""


# name = input('이름을 입력하지마세유 ')
# print('안녕하세요 '+name+'님')


"""
문제
두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

출력
첫째 줄에 다음 세 가지 중 하나를 출력한다.

A가 B보다 큰 경우에는 '>'를 출력한다.
A가 B보다 작은 경우에는 '<'를 출력한다.
A와 B가 같은 경우에는 '=='를 출력한다.
"""


# if 뒷담:
#     if 사과:
#         용서()
#     if 발뺌:
#         손절()
# else:
#     if 맛있는거_사줌:
#         친하게_지냄()
#     친분_유지()

# A,B = map(int,input().split())
#
# # A,B = new_numbers[0],new_numbers[1]
# print(A)
# print(B)
#
# if a>5 or a < 10:
#
# A = input()
#
# B = int(A)
#
# if A > 90 and A < 100:
#     B

# a = input()
# new_list = a.split()
# A = int(new_list[0])
# B = int(new_list[1])
#
# while not (A == 0 and B == 0):
#     JANE = int(input())
#     print(A+B)
#     a = input()
#     new_list = a.split()
#     A = int(new_list[0])
#     B = int(new_list[1])
#
# while True:
#     a = input()
#     new_list = a.split()
#     A = int(new_list[0])
#     B = int(new_list[1])
#     if not (A == 0 and B == 0):
#         print(A+B)
#     else:
#         break

#
# cal = []
# for month in range(1,13):
#     m = []
#     for day in range(1,32):
#         m.append(day) #[1,2,3.....31]
#     cal.append(m)
#
# print(cal[0])
#
#
# t = int(input())
# new_list = []
# for i in range(t):
#     a = int(input())
#     new_list.append(a)
# new_list.sort()
# for i in new_list:
#     print(i)
#

# new_list = []
# old_list = [5,4,3,2,1]
#
# for i in old_list:
#     new_list.append(i*2)
#
# print(new_list)
#
# # old_list.pop(0)
# # old_list.remove(4)
# #
#
# A = input().split()
# X = input().split()
# P = []
# out = ""
#
# for i in range(len(A)):
#     A[i] = int(A[i])
#
# for i in range(len(X)):
#     X[i] = int(X[i])
#     if A[1] > X[i]:
#         P.append(X[i])
#
# for i in range(len(P)):
#     out = out + str(P[i]) + ' '
#
#
# print(f'{out}')

# l = [3,
# 29,
# 38,
# 12,
# 57,
# 74,
# 40,
# 85,
# 61
#
# best = 0
# best_location = 0
# for i,x in enumerate(l):
#     if best < x:
#         best = x
#         best_location = i
# print(f'최대위치는 {best_location+1} 최대값은 {best}')
#
# best = max(l)
# best_location = l.index(best)
# print(f'최대위치는 {best_location+1} 최대값은 {best}')
#
# min(l)

# pp = input()
# kk = input().split()
#
# kk.sort()
#
# print(kk[0] + kk[pp])

# #1 원소 하나일 때
# l = int(input())
# #원소 2개 일 때
# l = input().split()
# A = int(l[0])
# B = int(l[1])
#
# # N개 이상 일 때
# l = input().split()
# new_list = []
# for i in l:
#     new_list.append(int(i))
#

# new_list = []
#
# for i in range(9):
#     l = int(input())
#     new_list.append(l)


# for i in range(len(new_list)): #i 0~8
#     new_list[i] = new_list[i] * 2
#
# for i in new_list: # i가 그냥 각각의 원소
#     print(i)
# print(new_list)
# big_number = max(new_list)
# print(f'big number {big_number}')
# print(new_list.index(big_number)+1)

# max
# min
# sort() 그냥은 작은 것부터 reverse=True하면 큰 것부터
# index
# len()

#print(f'{small} {big}')

# A = input()
# B = input().split()
# new_list = []
#
# for i in B:
#     new_list.append(int(i))
#
# print(min(new_list))
# print(max(new_list))

# new_list = []
#
# for i in range(9):
#     l = input()
#     new_list.append(int(l))
#
# A = max(new_list)
#
# print(A)
# print(new_list.index(A) + 1)

# A = input().split()
# X = input().split()
# P = []
# out = ""
#
# for i in range(len(A)):
#     A[i] = int(A[i])
#
# for i in range(len(X)):
#     X[i] = int(X[i])
#     if A[1] > X[i]:
#         P.append(X[i])
#
# for i in range(len(P)):
#     out = out + str(P[i]) + " "
#
# print(f'{out}')

# A = int(input())
# B = input().split()
#
# for i in range(len(B)):
#     B[i] = int(B[i])
#
# total = sum(B)/A
#
# M = max(B)
#
# for i in range(len(B)):
#     B[i] = B[i]/M*100
#
# total = sum(B)/A
#
# print(total)
# new_list = []
# a_list = []
#
# for i in range(10):
#     A = int(input())
#     new_list.append(A)
#
# for i in new_list:
#     b = i%42
#     if b in a_list:
#         continue
#     else:
#         a_list.append(b)
#
# print(len(a_list))

'''
N번 반복:
	line = 읽고
	jumsoo = 0
	total = 0
	line에있는 원소  i 마다:
		i 가 'O'면:
			jumsoo = jumsoo +1
			total = total+ jumsoo
		i가 'X'면:
			jumsoo = 0
	print (total)
'''

# A = int(input())
#
# for i in range(A):
#     line = input()
#     jumsoo = 0
#     total = 0
#     for psadksal in line:
#         if psadksal == "O":
#             jumsoo = jumsoo + 1
# #             total = total + jumsoo
# #         elif psadksal == "X":
# #             jumsoo = 0
# #     print(total)
#
# new_list = []
# # append 추가하기 ex) new_list.append('황현승')
# # max 최댓 값
# # min 최솟 값
# # sum 합
# for i in range(5):
#     sdfghfsdf
#
#     print(f'{finalf}%') :.3
#
# input()
# split()
# len()

#
# for i in range(len(a)):
#     a [i]= a[i]+'님'
# print(a)


# a = ['1','2','3','4','999']

# for i in a:
#     print(i)
#
# for i in range(len(a)):
#     if i %2 ==0:
#         print(a[i])

# for i, v in enumerate(a):
#     a[i] = int(a[i])
# print(a)
#
# max()
# min()
# a.sort()
# len()
# sum()
# range()
# print()
# zip()


# a = int(input())
# new_list = []
#
# for i in range(a):
#     b = input()
#     new_list.append(b)
#
# new_list.sort()
# for x, v in enumerate(new_list):
#     new_list[x] = int(new_list[x])
#     print(new_list[x])
#
#
# a = int(input())
#
# for i in range(a):
#     b = input()


# a = int(input())
# new_list = []
#
# for i in range(a):
#     b = input()
#     new_list.append(b)
#
# new_list.sort()
# for x, v in enumerate(new_list):
#     new_list[x] = int(new_list[x])
#     print(new_list[x])
#
#
# a = int(input())
#
# for i in range(a):
#     b = input()
# a = ['황현승','허건','황현희','노유지','남궁민수','남궁민수','남궁민수']

# a = int(input())
# for i in range(a):
#     l = input().split()
#     l.pop(0)
#     print(l)
#     # 퍼세트 = (선택된 수/전체 수) * 100
#     for x,v in enumerate(l):
#         l[x] = int(l[x])
#     ppap = sum(l)
#     score_up = []
#     score = ppap / len(l)
#     for o,p in enumerate(l):
#         if (l[o] > score):
#             score_up.append(l[o])
#     WaSans = len(score_up) / len(l) * 100
#     print(f'{WaSans :.3f}%')
# a = int(input())
# b = input()
# d = 0
# for i in range(a):
#     c = int((b[i]))
#     d = d + c
# print(d)
# a = int(input(0))
# for i in range(9):
#     print(f'{a} * {i+1} = {a*(i+1)}')

# word = input()

# class Product:
#     def __init__(self,j,p):
#         self.jaego = j
#         self.price = p
#     def more_jaego(self,m):
#         self.jaego = self.jaego + m
#
# # class Fruit(Product):
# #     def __init__(self):
# #         self.yoo_tong_gi_han =0
#
# apple = Product(50,100)
# apple.more_jaego(50)
# class Animal:
#     def anja(self):
#         print('sit')
# class Dog(Animal):
#     def bark(self):
#         print('bark')
# class Jindotgae(Dog):
#     def speak_korean(self):
#         print('안녕하세요')
#
# chorong = Jindotgae()
#
# chorong.anja()
# chorong.bark()
# chorong.speak_korean()
# ####
#
# import random
#
# def joosawee():
#     return random.randint(1,6)
#
# class User:
#     def __init__(self):
#         self.x= 0
#
# j1 = User()
# j2 = User()
# class yoot:
#     def __init__(self,p1,p2):
#         self.p1 = p1
#         self.p2 = p2
#         self.turn = True
#     def play(self):
#         if self.turn==True:
#             roll = joosawee()
#             if roll +self.p1.x >= 20:
#                 print('한재하 win game')
#                 return 2
#             self.p1.x = (self.p1.x + roll) % 20
#             print(f'재하 rolled {roll} on {self.p1.x}')
#             if self.p2.x == self.p1.x:
#                 self.p2.x = 0
#                 print('haha 재인 died')
#                 self.turn = not self.turn
#             self.turn = not self.turn
#             return 0
#         else:
#             roll = joosawee()
#             if roll +self.p2.x >= 20:
#                 print('한재인 win game')
#                 return 5
#             self.p2.x = (self.p2.x + roll) % 20
#             print(f'재인 rolled {roll} on {self.p2.x}')
#             if self.p2.x == self.p1.x:
#                 self.p1.x = 0
#                 print('haha 재하 died')
#                 self.turn = not self.turn
#             self.turn = not self.turn
#             return 0
#
# y = yoot(j1,j2)
# score_board = dict()
# score_board['한재인 점수'] = 0
# score_board['한재하 점수'] = 0
# for j in range(5):
#     for i in range(100):
#         result = y.play()
#         if result ==5:
#             score_board['한재인 점수'] += 1
#             break
#         if result ==2:
#             score_board['한재하 점수'] += 1
#             break
# print(score_board)



# class USER:
#     def __init__(self,a,b,c):
#         self.name = a
#         self.old = b
#         self.family = c
#
# def sinsangjongbo():
#     a = input("이름을 입력하세요 : ")
#     b = input("나이를 입력해주세요 : ")
#     c = input("가족 구성원을 입력해주세요(띄어쓰기 필요) :  ").split()
#     return
#
#
# a,b,c = sinsangjongbo()
# user1 = USER()
# print(user1.name)
# user2 = USER()
# print(user2.old)

# def factorial(x):
#     if x== 1:
#         return 1
#     return x * factorial(x-1)
#
# print(factorial(5))
#
# 5 4 7 2 423  78 76 234  867 34 5 78 79 90  2345  23
#
# def find_best(numbers):
#     a = numbers[0] + find_best(numbers[1:])
#     b = numbers[len(numbers)-1] + find_best(numbers[:len(numbers)-2])
#     return max(a,b)

# from random import randrange
# numbers = []
# for i in range(100000000):
#     numbers.append(randrange(1 ,7))
# count = 0
# for n in numbers:
#     if n == 1:
#         count = count +1
# print(count/len(numbers))



# numbers = []
#
#
# k = int(input())
# for i in range(k):
#     a = input().split()
#     for x in range(a):
#
#     numbers.append((a,b))
#
# numbers.sort()


#
# print(numbers)

# line_count = int(input())
# c_list = []
# for i in range(line_count):
#     coordinate_list = input().split()
#     a = (int(coordinate_list[1]),int(coordinate_list[0]))
#     c_list.append(a)
# c_list.sort()
# for l in range(line_count):
#     print(f"{c_list[l][1]} {c_list[l][0]}")

# DT = input()
# RT = []
# for i in range(len(DT)):
#      RT.append(DT[i])
# # for z in range(len(RT)):
# #     RT[z] = int(RT[z])
# RT.sort(reverse=True)
#
# answer =''
# for r in RT:
#     answer = answer + r
# print(answer)

# a = []
#
#
# def jagophap(x):
#     for i in range(len(x)):
#         x[i] = x[i]**2
#     return sum(x)
# answer = jagophap(a)
# print(answer)
#
# honeyseed : -8222465627887252162

# def factorial(x):
#     if x== 1:
#         return 1
#     return x * factorial(x-1)
#
# print(factorial(1000))

# Python program to read
# json file

# import json
#
# with open('states.json','r', encoding="UTF-8") as f:
#
#
#     states = json.load(f)
#     a = states['states']
#     for i in a:
#         if i['name'] == '빵현승':
#             print(i["area_codes"])

# new_list = [[1,2,3,0],[4,5,6,0,0],[7,8,9,8,6,4]]
#
# for z in range(len(new_list)):
#     for i in range()
#         print(new_list[z][])
# sorrythisseaagroggalda = "오오늘마트각종물건5만원세일"
# for x,o in enumerate(sorrythisseaagroggalda):
#     wha_sans = sorrythisseaagroggalda[x:866]
#     print(wha_sans)
# for i in range(1,7,1):
#     print(" " * (7-i) + "*" * i + "*" * i + " 미안하다 이거 보여주려고 어그로끌었다.. 나루토 사스케 싸움수준 ㄹㅇ실화냐? 진짜 세계관최강자들의 싸움이다.. 그찐따같던 나루토가 맞나? 진짜 나루토는 전설이다..진짜옛날에 맨날나루토봘는데 왕같은존재인 호카게 되서 세계최강 전설적인 영웅이된나루토보면 진짜내가다 감격스럽고 나루토 노래부터 명장면까지 가슴울리는장면들이 뇌리에 스치면서 가슴이 웅장해진다.. 그리고 극장판 에 카카시앞에 운석날라오는 거대한 걸 사스케가 갑자기 순식간에 나타나서 부숴버리곤 개간지나게 나루토가 없다면 마을을 지킬 자는 나밖에 없다 라며 바람처럼 사라진장면은 진짜 나루토처음부터 본사람이면 안울수가없더라 진짜 너무 감격스럽고 보루토를 최근에 알았는데 미안하다.. 지금20화보는데 진짜 나루토세대나와서 너무 감격스럽고 모두어엿하게 큰거보니 내가 다 뭔가 알수없는 추억이라해야되나 그런감정이 이상하게 얽혀있다.. 시노는 말이많아진거같다 좋은선생이고..그리고 보루토왜욕하냐 귀여운데 나루토를보는것같다 성격도 닮았어 그리고버루토에 나루토사스케 둘이싸워도 이기는 신같은존재 나온다는게 사실임?? 그리고인터닛에 쳐봣는디 이거 ㄹㅇㄹㅇ 진짜팩트냐?? 저적이 보루토에 나오는 신급괴물임?ㅡ 나루토사스케 합체한거봐라 진짜 ㅆㅂ 이거보고 개충격먹어가지고 와 소리 저절로 나오더라 ;; 진짜 저건 개오지는데.. 저게 ㄹㅇ이면 진짜 꼭봐야돼 진짜 세계도 파괴시키는거아니야 .. 와 진짜 나루토사스케가 저렇게 되다니 진짜 눈물나려고했다.. 버루토그라서 계속보는중인데 저거 ㄹㅇ이냐..? 하.. ㅆㅂ 사스케 보고싶다..  진짜언제 이렇게 신급 최강들이 되었을까 옛날생각나고 나 중딩때생각나고 뭔가 슬프기도하고 좋기도하고 감격도하고 여러가지감정이 복잡하네.. 아무튼 나루토는 진짜 애니중최거명작임..")
# c = [105,110,102,105,116,101,115,116,97,105,114,115]
# for i,v in enumerate(c):
#     print(chr(c[i]))

# import os
# import os.path
# print("===============Démarrage du programme===============")
# current_path = "C:/Users/user/OneDrive/문서"
#
# for a,b,c in os.walk(current_path):
#     print(a)
#     print(b)
#     print(c)
#
# class a:
#
# class queue:
#     def __init__(self):
#         self.queue_storage = []
#     def enqueue(self, num):
#         for i in num:
#             self.queue_storage.append(i)
#     def deqeue(self):
#         size = len(self.queue_storage)
#         a = self.queue_storage.pop(0)
#         return(a)
#
# class stack:
#     def __init__(self):
#         self.stack_storage = []
#     def push(self, num):
#         for i in num:
#             self.stack_storage.append(i)
#     def pop(self):
#         size = len(self.stack_storage)
#         a = self.stack_storage.pop(size-1)
#         return(a)
#
# komq = queue()
# komq.enqueue([1,2,3,4])
# for i in range(2):
#     print(komq.deqeue())
# print(komq.queue_storage)
#
# gabbq = stack()
# gabbq.push([1,2,3,4])
# for i in range(2):
#     print(gabbq.pop())
# print(gabbq.stack_storage)

# a = input()
# eol = []
# wasans = []
# for i in range(int(a)):
#    eol.append(int(input()))
# for x,y in enumerate(eol):
#     if y == 0:
#         wasans.pop(len(wasans)-1)
#     else:
#         wasans.append(y)
# print(sum(wasans))

# class queue:
#     def __init__(self):
#         self.queue_storage = []
#     def enqueue(self, num):
#         self.queue_storage.append(num)
#     def dequeue(self):
#         Ja = self.queue_storage.pop(0)
#         return Ja
#
# p = int(input())
# a = queue()
#
# for v in range(1,p+1):
#     a.enqueue(v)
#
# while not len(a.queue_storage) == 1:
#     a.dequeue()
#     n = a.dequeue()
#     a.enqueue(n)
# print(a.queue_storage[0])

import json
class vocabularyclass:
        def __init__(self): # 이거 태초에서 하는거임
            with open("vocabulary.json","r",encoding="UTF8") as vocajson:
                self.voca = json.load(vocajson)
        def save(self):
            with open("vocabulary.json", "w", encoding="UTF8") as jvocajson:
                json.dump(self.voca,jvocajson,ensure_ascii=False,indent=4)

        def add(self,word,mean): # 이거 단어 넣는거임
            self.jvoca = self.voca["jvocabulary"]
            self.jvoca[word]=mean
            self.save()

        def modify(self,word,mean): # 이거 단어 수정하는 거임
            self.mjvoca = self.voca["jvocabulary"]
            if word in self.mjvoca:
                self.mjvoca[word]=mean # 수정하는 곳임
                self.save()
            else:
                print(f"해당 \'{word}\' 단어가 단어장에 등록되어 있지 않습니다. 그래서 수정하지 못했습니다")

        def delete(self,word): # 이거 단어 삭제하는 거임
            self.djvoca = self.voca["jvocabulary"]
            if word in self.djvoca:
                del self.djvoca[word] # 여기가 삭제하는 거임
                self.save()
            else:
                print(f"해당 \'{word}\' 단어가 단어장에 등록되어 있지 않습니다. 그래서 삭제하지 못했습니다")


a = vocabularyclass()
a.add('golf','골프')
a.add('hi','ㅎㅇ')
print(a.voca)


