def FunWithFunctions():
    for count in range(1,2001):
        print count
        if count%2==0:
            print "^tis even"
        else:
            print "^tis a bit odd, this one"
FunWithFunctions()
aa = [666,6,6,6,2,666]
def MakingFunctionsIsFun(arrn,arr):
    for counter in arrn:
        counter *= arr
        print counter
MakingFunctionsIsFun(aa,5)
