from typing import Dict, Any

print("\nExercicio 1:\n")

list_num: list = list(range(1,11))

for i in list_num:
    print(i)


print("\nExercicio 2:\n")

list_code = ["Python", "Java", "C++", "JavaScript"]
list_code.remove("C++")
list_code.append("Ruby")
print(list_code)

print("\nExercicio 3:\n")

book: Dict[str, Any] = {
    "title": "Bible",
    "year": 1,
    "author": "Jesus"
}
book_2: Dict[str, Any] = {
    "title": "GOT",
    "year": 2012,
    "author": "Author"
}

list_dicts: dict = {
    "book_01": {"title": "GOT",
    "year": 2012,
    "author": "Author",},

    "book_02": {"title": "GOT",
    "year": 2012,
    "author": "Author"}
}

lista_elements = book.items() #transform dict in list and print each element
for i in lista_elements:
    print(i)

print("\n")
print(list_dicts["book_01"])

print("\nExercicio 4:\n")

def count_char(statement):
    count_word: dict = {}
    for word in statement:
        if word in count_word:
            count_word[word] += 1
        else:
            count_word[word] = 1
    return count_word

print(count_char("Thats a test to count number of characters"))

print("\nExercicio 5:\n")

list_fruits = ["maça","banana","cereja"]
dict_fruits: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = sum(dict_fruits.values())
print(total)

print("\nExercicio 6:\n")

emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails = list(set(emails))
print(emails)

print("\nExercicio 7:\n")

idades = [22, 15, 30, 17, 18]

for i in idades:
    if i >= 18:
        print(i)

print("\nExercicio 8:\n")

pessoas = [
    {"nome": "carol", "idade": 30},
    {"nome": "alice", "idade": 25},
    {"nome": "bob", "idade": 20}
]

pessoas_sorted = sorted(pessoas,key=lambda x: x['nome'])
print(pessoas_sorted)

# pessoas.sort(key=lambda pessoas: pessoa['nome'])

print("\nExercicio 9:\n")

numeros = [10, 20, 30, 40, 50]

media = sum(numeros)/len(numeros)
print("Mean:", media)

print("\nExercicio 10:\n")

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [i for i in valores if i%2==0]
impar = [i for i in valores if i%2!=0]

print(pares)
print(impar)

print("\nExercicio 11:\n")

produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]
print(produtos)
for i in produtos:
    if i["id"]==2:
        i["preço"]=90
print(produtos)

print("\nExercicio 12:\n")

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dict_oficial = {**dicionario1, **dicionario2}

#dict_oficial.update(dicionario1)
#dict_oficial.update(dicionario2)

print(dict_oficial)

print("\nExercicio 13:\n")

estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

estoque_bigger = {}

for i in estoque:
    if estoque[i]>0:
        estoque_bigger[i] = estoque[i]    

print(estoque_bigger)

print("\nExercicio 14:\n")

dicionario = {"a": 1, "b": 2, "c": 3}
list_key = dicionario.keys()
list_values = dicionario.values()
print(list_key)
print(list_values)

print("\nExercicio 15:\n")

texto = "engenharia de dados"
count_word = {}

for i in texto:
    if i in count_word:
        count_word[i] += 1
    else:
        count_word[i] = 1
print(count_word)

#Functions
print("\nExercicio 16:\n")

def sum_list_numbers(numbers: list) -> list:
    return sum(numbers)

test_list = sum_list_numbers([1,2,3,4,5,6,7,8,9,10])
print(test_list)

print("\nExercicio 17:\n")

def check_if_primo(num: int) -> bool:
    if num <= 1:
        return False
    if num <=3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

primo = check_if_primo(11)
print(primo)

print("\nExercicio 18:\n")

#full algorithm
def revert_string(text: str) -> str:
    tam = len(text)
    list1 = list(text)
    i = 0
    for i in range(tam//2):
        temp = list1[tam-i-1]
        list1[tam-i-1] = list1[i]
        list1[i] = temp
    return ''.join(list1)

print(revert_string("lapis"))

#easy version:
def revert_string_easy(text: str) -> str:
    return text[::-1]

print(revert_string_easy("Testando a versao facil de reverter string."))

print("\nExercicio 19:\n")

def combinations(target_sum: int, numbers: list) -> list:
    # Lista para armazenar os pares de números que somam ao target_sum
    result = []
    # Dicionário para armazenar índices dos números já vistos
    seen = {}
    
    for number in numbers:
        # Calcula o complemento necessário para formar o target_sum com o número atual
        complement = target_sum - number
        if complement in seen:
            # Se o complemento estiver no dicionário, adiciona o par à lista de resultados
            result.append((complement, number))
        # Adiciona o número ao dicionário
        seen[number] = True
    
    return result

# Testando a função
print(combinations(5, [1, 2, 3, 4, 5]))  # Saída esperada: [(2, 3), (1, 4)]

print("\nExercicio 20:\n")

def order_dict_keys(dicionario: dict) -> list:
    myKeys = list(dicionario.keys())
    myKeys.sort()
    return myKeys

print(order_dict_keys({'ravi': 10, 'rajnish': 9,'sanjeev': 15, 'yash': 2, 'suraj': 32}))
