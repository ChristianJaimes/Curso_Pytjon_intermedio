def run():
    #Filter
    my_list = [1,4,5,6,9,11,13]
    odd = [i for i in my_list if i%2 != 0] #Usando list comprehensions
    print(odd)
    odd2 =list(filter(lambda x : x%2 != 0,my_list)) #usando Filter
    print(odd2,"\n")

    #MAP
    my_list2 = [1,2,3,4,5]
    squares = [i**2 for i in my_list2] #Usando list comprehensions
    print(squares)
    squares2 = list(map(lambda x:x**2, my_list2))#Usando MAP
    print(squares2,"\n")

    #Reduce
    my_list3 = [2,2,2,2,2]
    all_multiplicated = 1
    for i in my_list3:
        all_multiplicated *= i
    print(all_multiplicated)
    from functools import reduce
    all_multiplicated2 = reduce(lambda a,b :a*b,my_list3)
    print(all_multiplicated2)

if __name__ == '__main__':
    run()
    