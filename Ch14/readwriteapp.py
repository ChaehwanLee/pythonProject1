import readwrite;

def start():
    # name = input('Input File Name...?');
    # content = input('Write Contents..:');
    # readwrite.filewrite(name,content);

    # rname = input('Input read File Name...?');
    # try:
    #     rcontent = readwrite.fileread(rname);
    #     print(rcontent);
    # except:
    #     print('File Not Found...');

    rname = input('Input read File Name...?');
    try:
        rcontent = readwrite.fileread(rname);
        print(rcontent);
    except FileNotFoundError:
        print('File Not Found...');
    except IOError:
        print('IO Error');

# 마우스로 아이콘을 클릭했을 때, 휴대폰으로 앱을 눌렀을 때
# UI 를 분리해서 사용
# User
if __name__ == '__main__':
    start();
