def BaseNtoDec(szam,base):
    """N-es szamrendszerbeli szamot valt at tizes szamrendszerbe
    (2 <= N <= 10)"""
    power = 1
    num = 0
    # str_szam = str(szam)
    rev_str_num = str(szam)[::-1]
    for i in map(str,rev_str_num):
        num += int(i) * power
        power = power * base
    str_num = str(num)
    return str_num

def Base10toN(num, base):
    """Tizes szamrendszerbeli szamot valt at N-es szamrendszerbe
    (2 <= N <= 10)"""
    converted_string = ""
    currentnum = int(num)
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    result = int(converted_string)
    return result

try:
    szamrendszer = int(input("Add meg a szamrendszert (2 <= szamrendszer <= 10) :"))
    if szamrendszer < 2 or szamrendszer > 10 :
        raise ValueError("A megadott szamrendszer nem felel meg a 2 <= szamrendszer <= 10 feltetelnek")

    else:
        szam1 = input("Add meg az 1. szamot :")
        szam2 = input("Add meg az 2. szamot :")
        reszosszeg1 = int(BaseNtoDec(szam1,szamrendszer))
        reszosszeg2 = int(BaseNtoDec(szam2,szamrendszer))
        sum_decimalis = reszosszeg1 + reszosszeg2
        vegeredmeny = Base10toN(sum_decimalis, szamrendszer)
        print("A(z) {a}-es szamrendszerben : {b} + {c} = {d}".format(a= szamrendszer , b= szam1, c=szam2, d=vegeredmeny))
except ValueError:
    print("A megadott szamrendszer nem felel meg a 2 <= szamrendszer <= 10 feltetelnek")