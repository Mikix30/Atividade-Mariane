numb1 = int(input("Qual o número desejado?"))

numb2 = int(input("Qual o outro número desejado? "))

numb3 = int(input("Qual o outro número desejado? "))

numb4 = int(input("Qual o outro número desejado? "))

numb5 = int(input("Qual o outro número desejado? "))


listt = [numb1,numb2,numb3,numb4,numb5]

numb = filter(lambda x: '>10' in x, [listt])


print(list(numb))
