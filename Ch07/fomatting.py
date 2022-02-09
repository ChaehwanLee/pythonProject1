num1 = 10;
num2 = 2.34;
st = 'abc';

sql = 'INSERT INTO TB VALUES(%s, %d, %f)';
print(sql % (st,num1,num2));

st2 = 'jmlee@tonesol.com';
# 아이디를 출력하시오

id = st2[0:st2.find('@')];
print(id);

# 도메인을 출력하시오

domain = st2[st2.find('@') +1 : st2.find('.')];
print(domain);

# 3 개의 숫자를 입력 받는다.
# 3 개의 숫자를 리스트에 담는다.
nums = input('input 3 numbers ,,,');
lnums = nums.split();
print(nums)
lnums=[];

lnums2 = [];
for n in lnums:
    lnums2.append(int(n));
print(lnums2);