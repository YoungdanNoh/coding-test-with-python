a = int(input())

dict = {"winter":[12, 1, 2],
        "spring":[3,4,5],
        "summer":[6,7,8],
        "fall":[9,10,11]}

for k, v in dict.items():
    if a in v:
        print(k)