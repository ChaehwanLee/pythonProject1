while True:
    st = input('input number'); # 코드에 이상은 없으나, 실행중에 불가피하게 발생할 수 있는 문제

    if st == 'q':
        break;
    # if st.isalpha():
    #     print('retry...');
    #     continue;
    # else:
    num = int(st);
    print(num * 100); # 우리는 이것을 예외상황이라고 이야기한다

print('Exit');