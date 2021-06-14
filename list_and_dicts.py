def run():
    my_list = [1,"hello",True,4,5]# definicion de lista
    my_dict = {"firtsName":"Facundo","lasName":"Garcia"} #definicion Diccionario

    super_list = [
        {"firtsName":"Facundo","lasName":"Garcia"},
        {"firtsName":"Maria","lasName":"Silva"},
        {"firtsName":"Carlos","lasName":"Bautista"},
        {"firtsName":"Jimena","lasName":"Melano"}
    ]

    super_dict = {
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,3],
        "floating_nums":[ 1.1,2.4,5.0]
    }
    for key, value in super_dict.items():
        print(f' {key} = {value}')
        

if __name__ == '__main__':
    run()