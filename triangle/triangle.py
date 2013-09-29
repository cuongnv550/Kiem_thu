def detect_triangle(a, b, c):
    if ( 'a' <= a <= 'z' or 'a' <= b <= 'z' or 'a' <= c <= 'z'):
        return -1
    if (  a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b ):
        var1 = 1
    else :
        var1 = 0
    if ( a == b or a == c or b == c ):
        var2 = 1
    else :
        var2 = 0
    # Du lieu khong hop le
    if( a<=0 or b<=0 or c<=0
        or a>2**32-1 or b>2**32-1 or c>2**32-1 
        or type(a) not in [float, long, int]
        or type(b) not in [float, long, int]
        or type(c) not in [float, long, int]):
        return -1
    # 3 canh khong tao thanh tam giac
    elif( a+b < c or b+c < a or a+c < b):
        return 0
    # tam giac deu
    elif( a==b and b==c):
        return 1
    # tam giac vuong can
    elif( var1 ==1 and var2==1):
        return 2
    # tam giac can
    elif(var1 == 0 and var2 == 1 ) :
        return 3
    # tam giac vuong
    elif ( var1 == 1 and var2 == 0):
        return 4
    # tam giac thuong
    else :
        return 5

               
