import random

list = []
winners = []
while True:
    member = input("이름을 입력하세오[두 글자 이상!] : (업으면 댁둥 을 입력하세오)")
    if member == '댁둥':
        break
    if len(member) < 2:
        print("오타났어요, 페도 녀석아!!")
    for a in list:
        if a == member:
            print("중복되었어오")
        else: pass
    list.append(member)
i = 0
n  = int(input("뽑을 사람 수를 입력하세오 : "))
while i < n:
    winner = random.choice(list)
    for k in winners:
        if k == winner:
            pass
    winners.append(winner)
    i += 1

for u in winners:
    print("축하함니다",u)

