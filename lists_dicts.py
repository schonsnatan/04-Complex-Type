import json

product_01 = {
    "nome": "Shoes",
    "price": 10.75,
    "quantity": 10,
    "available": False
}
product_02 = {
    "nome": "Shirt",
    "price": 5.50,
    "quantity": 15,
    "available": True
}

shop = []

shop.append(product_01)
shop.append(product_02)

carrinho_json = json.dumps(shop)
print(carrinho_json)