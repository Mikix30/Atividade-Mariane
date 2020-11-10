v = int(input("Qual o número desejado? "))


funct = [

    lambda x: x**2,

    lambda x: x**3,

]


for f in funct:
    print(f(v))
