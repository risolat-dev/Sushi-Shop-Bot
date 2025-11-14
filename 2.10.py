import json


def all_data():
    try:
        with open("products.json", "r") as f:
            data = json.load(f)
            return dict(data)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}

def add_data(d: dict):
    data = all_data()
    data.update(d)
    with open("products.json", 'w') as f:
        json.dump(data, f, indent=4)


def add_phone():
    id = input("Id: ")
    title = input("Nomini kiriting>> ")
    price = int(input("Narxini kiriting>> "))
    storage = int(input("Xotirasi>> "))
    camera = int(input("Kamera (px)>> "))

    phone = {
        id: {
            "title": title,
            "price": price,
            "storage": storage,
            "camera": camera,
            "type": "phone"
        }
    }
    add_data(phone)

def add_tv():
    id = input("Id: ")
    title = input("Nomini kiriting>> ")
    price = int(input("Narxini kiriting>> "))
    size = int(input("Size>> "))
    dyum = int(input("Dyum >> "))

    tv = {
        id: {
            "title": title,
            "price": price,
            "size": size,
            "dyum": dyum,
            "type": "tv"
        }
    }
    add_data(tv)

def add_pc():
    id = input("Id: ")
    title = input("Nomini kiriting>> ")
    price = int(input("Narxini kiriting>> "))
    ram = int(input("Ram>> "))
    cpu = int(input("Cpu >> "))

    pc = {
        id: {
            "title": title,
            "price": price,
            "ram": ram,
            "cpu": cpu,
            "type": "pc"
        }
    }
    add_data(pc)


def view_phone():
    data = all_data()
    for key, value in data.items():
        if value['type'] == 'phone':
            print(f"Id: {key}, Title: {value['title']}, Price: {value['price']}, Storage: {value['storage']}, Camera: {value['camera']}")

def view_tv():
    data = all_data()
    for key, value in data.items():
        if value['type'] == 'tv':
            print(f"Id: {key}, Title: {value['title']}, Price: {value['price']}, Size: {value['size']}, Dyum: {value['dyum']}")

def view_pc():
    data = all_data()
    for key, value in data.items():
        if value['type'] == 'pc':
            print(f"Id: {key}, Title: {value['title']}, Price: {value['price']}, Ram: {value['ram']}, Cpu: {value['cpu']}")


def delete_product(prod_type):
    data = all_data()
    if prod_type == "phone":
        view_phone()
    elif prod_type == "tv":
        view_tv()
    elif prod_type == "pc":
        view_pc()

    id = input("O'chirmoqchi bo'lgan id si: ")
    if id in data:
        data.pop(id)
        with open("products.json", "w") as f:
            json.dump(data, f, indent=4)
        print("O'chirildi!")
    else:
        print("Bunday id mavjud emas!")


def update_product(prod_type):
    data = all_data()
    if prod_type == "phone":
        view_phone()
        fields = {"1": "title", "2": "price", "3": "storage", "4": "camera"}
    elif prod_type == "tv":
        view_tv()
        fields = {"1": "title", "2": "size", "3": "price", "4": "dyum"}
    elif prod_type == "pc":
        view_pc()
        fields = {"1": "title", "2": "ram", "3": "cpu", "4": "price"}

    id = input("Update id: ")
    if id not in data:
        print("Bunday id mavjud emas!")
        return

    print(f"Update maydonlari: {fields}")
    f_type = input("Qaysi maydonni update qilmoqchisiz? ")
    if f_type not in fields:
        print("Noto'g'ri tanlov!")
        return

    new_field = input("Yangi qiymat kiriting>> ")

    if fields[f_type] in ["price", "ram", "cpu", "size", "dyum", "storage", "camera"]:
        new_field = int(new_field)

    data[id][fields[f_type]] = new_field
    with open("products.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Yangilandi!")


def manager():
    while True:
        print("""
1. Hamma mahsulotni ko'rish
2. Phone qo'shish
3. Tv qo'shish
4. Pc qo'shish
5. Phone update
6. Tv update
7. Pc update
8. Phone delete
9. Tv delete
10. Pc delete
11. Phone ko'rish
12. Tv ko'rish
13. Pc ko'rish
0. Chiqish
""")
        choice = input("Menudan birini tanlang: ")

        if choice == "1":
            view_phone()
            view_tv()
            view_pc()
        elif choice == "2":
            add_phone()
        elif choice == "3":
            add_tv()
        elif choice == "4":
            add_pc()
        elif choice == "5":
            update_product("phone")
        elif choice == "6":
            update_product("tv")
        elif choice == "7":
            update_product("pc")
        elif choice == "8":
            delete_product("phone")
        elif choice == "9":
            delete_product("tv")
        elif choice == "10":
            delete_product("pc")
        elif choice == "11":
            view_phone()
        elif choice == "12":
            view_tv()
        elif choice == "13":
            view_pc()
        elif choice == "0":
            break
        else:
            print("Noto'g'ri tanlov!")

manager()
