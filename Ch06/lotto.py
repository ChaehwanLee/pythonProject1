import random

def inputnum(): #숫자 입력받는 함수
    while True:
        notNum = 0
        input1 = list(map(int,input('번호를 입력해주세요:').split())) # 공백 기준으로 입력받아 리스트로 만듦
        for i in range(0, 6):
            jungbokin = 0  # 중복 플래그 초기화
            for a in range(0, i + 1):  # 이전의 데이터들을 모두 판단
                if input1[i] == input1[a]:  # 중복시
                    if a == i:  # 자기자신이면
                        continue  # 넘어감
                    else:  # 자기자신이 아니면
                        jungbokin = 1  # 중복임
                        break
                else:  # 그냥중복아님
                    jungbokin = 0
            if jungbokin == 1: # 중복이면
                break #빠져나감
        for i in input1:
            if i > 45 or i < 1: # 1보다 작거나 45보다 큰 경우
                notNum = 1 # 조건 불만족
                break
            else:
                notNum = 0
        if jungbokin == 1:
            print('중복된 숫자가 있습니다. 다시 입력해주세요')
            continue

        if len(input1) != 6 or notNum == 1: # 입력된 숫자의 개수가 6 개가 아니거나 1~45 사이가 아닌 경우
            print('1~45 사이의 6개의 번호를 입력해주세요')
            continue # 반복
        else:
            break
    return input1




def number1(): #당첨번호 추첨
    number1 = [0, 0, 0, 0, 0, 0, 0]
    for i in range(0,7):
        jungbok = 0 # 중복 플래그 초기화
        while True:
            temp = random.randint(1, 45) # 1부터 45 사이 랜덤 수

            for a in range(0,i+1): # 이전의 데이터들을 모두 판단
                if temp == number1[a]: # 중복시
                    if a == i: # 자기자신이면
                        continue #넘어감
                    else: # 자기자신이 아니면
                        jungbok = 1 # 중복임
                        break
                else: # 그냥중복아님
                    jungbok = 0

            if jungbok ==0: #중복이 아닌 경우에만
                number1[i] = temp # 리스트에 저장
                break

    return number1



def lottoPrize(A, B): # 등수 추출
    deng = 0  # 등수
    count = 0 # 카운트
    bonus = B.pop()
    for b in range(0,6):
        if B.count(A[b]) == 1: # 숫자가 있으면(중복되는 숫자가 없으므로 1개로만 판단)
            count = count + 1 # 카운트 증가
    if count == 3:
        deng = 5
    elif count == 4:
        deng = 4
    elif count == 5: # 2,3등 판단
        if A.count(bonus) == 1: # 보너스 숫자가 입력에 있으면
            deng = 2
        else:
            deng = 3
    elif count == 6:
        deng = 1
    if deng == 0:  # 미당첨
        return print('일치하는 숫자 갯수: {} \n당첨되지 않으셨습니다.'.format(count))
    else:  # 당첨시
        return print('일치하는 숫자 갯수: {} \n{}등입니다.'.format(count, deng))

def lottoProgram():
    inNum = inputnum()
    print('입력번호 : {}'.format(inNum))
    outNum = number1()
    print('당첨번호 : {}'.format(outNum))
    lottoPrize(inNum, outNum)

lottoProgram()

if __lottoProgram()