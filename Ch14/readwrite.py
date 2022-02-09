def filewrite(name, content):
    try:
        f = open(name, 'wt');
        f.write(content);
    except:
        print('Error');
    finally:
        f.close();

# def fileread(name):
#     try:
#         f = open(name, 'rt');
#         text = f.read();
#     except FileNotFoundError as fe:
#         raise fe;
#     except IOError as ie:
#         raise ie;
#     finally:
#         f.close();
#     return text;

def filerea(name):
    f = None;
    try:
        f = open(name, 'rt');
        text = f.read();
    except FileNotFoundError as fe:
        raise fe; # 예외 상황에서 raise를 던진다
    finally:
        if f is not None:
            f.close();
    return text;

# 기능을 분리해서 사용
# 하나 이상의 상황을 만들 수 있다
# function