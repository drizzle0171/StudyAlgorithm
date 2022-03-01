def finding_gcd(a,b):
    while(b!=0):
        result = b
        a, b = b, a%b
    return result 

def test_finding_gcd():
    num1 = 21
    num2 = 12
    assert(finding_gcd(num1, num2) == 3)
    print("테스트 통과")

if __name__=="__main__":
    test_finding_gcd()