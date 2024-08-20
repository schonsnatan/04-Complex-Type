lista = [64, 34, 25, 12, 22, 11, 90]

def order_num_lists(numeros: list) -> list:
    new_num_list = numeros.copy()
    tam = len(new_num_list)
    temp = new_num_list[0]
    for i in range(tam):
        for j in range(tam):
            if new_num_list[i] < new_num_list[j]:
                temp = new_num_list[i]
                new_num_list[i] = new_num_list[j]
                new_num_list[j] = temp
    return new_num_list

nova_lista = order_num_lists(lista)
print(nova_lista)

#using build-in sort function
list_second = [2,5,1,7,24,12,14,95,67]
list_second.sort()

print(list_second)

#name normalized function
def normalize_name(name: str) -> str:
    return name.strip().lower()

names = [' Alice ', "BOB", "Carlos"]
normalized_names = [normalize_name(name) for name in names]
print(normalized_names)