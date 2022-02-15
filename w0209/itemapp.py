# app.py code 만 업로드
# app.py
import itemdb

def start():
    print('Start App');
    while True:
        cmd = input('Input CMD(q,i,s,so,u,d)');
        if cmd == 'q':
            break;
        elif cmd == 'i':
            print('Insert Item');
            id = int(input('ID'));
            name = input('NAME:');
            price = int(input('PRICE:'));
            rate = float(input('FLOAT'));
            try:
                itemdb.insert(id,name,price,rate);
                print('Inserted OK');
            except:
                print('Insert Error');

        elif cmd == 's':
            print('Item Select');
            try:
                datas = itemdb.select();
                for data in datas:
                    print('%d %s %d %f' % data);
            except:
                print('Select Error');

        elif cmd == 'so':
            print('Insert Select One');
            try:
                id = int(input('id: '))
                results = itemdb.selectone(id);
                print(results)
            except:
                print('Error');

        elif cmd == 'u':
            print('Insert Update');
            try:
                id = int(input('Id'));
                name = input('Name');
                price = int(input('Price'));
                rate = int(input('Rate'));
                itemdb.update(id, name, price, rate)
            except:
                print('Update Error')

        elif cmd == 'd':
            print('Insert Delete');
            try:
                id=int(input('ID'));
                itemdb.delete(id)
            except:
                print('Delete Error')

    print('End App');


if __name__ == '__main__':
    start();