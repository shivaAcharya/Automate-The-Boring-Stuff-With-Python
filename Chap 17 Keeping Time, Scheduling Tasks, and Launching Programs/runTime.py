import time

def prodCalc():
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

startTime = time.time()
prod = prodCalc()
endTime = time.time()
print('The product of 1 through 100000 is %s digit long.' % (len(str(prod))))
print('The total run time is %s seconds.' % (endTime - startTime))