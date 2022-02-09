# while True:
#     st = input('input number'); # 코드에 이상은 없으나, 실행중에 불가피하게 발생할 수 있는 문제
#
#     if st == 'q':
#         break;
#     try:
#         num = int(st); # 예외가 발생되면 아랫라인 실행 안되고 예외로가서 다시 실행
#         print(num * 100); # 우리는 이것을 예외상황이라고 이야기한다
#         # 실패횟수를 세어서
#
#     except ValueError as e:
#         # print(e);
#         print('retry...');
#
# print('Exit');

cnt = 0; # while 루프 밖에서 만들어야한다
while True:
    print('retry count:',cnt);
    st = input('input number'); # 코드에 이상은 없으나, 실행중에 불가피하게 발생할 수 있는 문제

    if st == 'q':
        break;
    try:
        num = int(st);
        print(num * 100);
    except: # 예외상황 처리하는 부분
        cnt += 1; #밖에서 선언해서 루프에 묶이지 않도록
        if cnt == 5:
            break;
        print('retry...');

print('Exit');