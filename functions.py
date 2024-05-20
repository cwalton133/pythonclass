#
## How to use Function in Python


## In this example we are multiplying the base number by the power number
## 3 ** 2
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num 
    return result
    
print(raise_to_power(3, 2)) 

