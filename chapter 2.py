#Day--1  if, elif, else 
my_lover=input('请输入她的名字')
birthday=float(input('请输入她的生日'))        # birthday=input('请输入她的生日')
if len(my_lover)==4 and my_lover=='zcyn':
    print('不忘初心')
elif birthday==6.8:      #.elif birthday=='6.8':(注意，input默认我输入的为字符串,赋值等于也要是字符串)
    print('不断努力')
else:
    print('继续沉淀')


