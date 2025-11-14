# with open("file38.txt", "r") as f:
#     text = f.read()
#
# w = text.split()
# result = []
#
# for w in w:
#     if "c" in w.lower():
#         result.append(w)
#
# with open("file.txt", "w") as f:
#     if result:
#         f.write(" ".join(result))
#     else:
#         f.write("")


import re

contacts = {
    "+998901234567": {
        "name": "Ali",
        "phone number": "+998901234567",
        "email": "ali@mail.com"
    }
}

def add_contact(d: dict):
    name = input("Ism: ")
    phone = input("Telefon raqam: ")
    email = input("Email: ")

    phone_pattern = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
    email_pattern = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"

    if not re.match(phone_pattern, phone):
        print("Telefon raqam formati noto‘g‘ri!")
        return
    if not re.match(email_pattern, email):
        print("Email formati noto‘g‘ri!")
        return
    if phone in d:
        print("Bu telefon raqam allaqachon mavjud!")
        return

    d[phone] = {"name": name, "phone number": phone, "email": email}
    print("Kontakt muvaffaqiyatli qo‘shildi!")


def view_contacts(d: dict):
    if not d:
        print(" Kontaktlar mavjud emas.")
    else:
        for phone, info in d.items():
            print(f"{info['name']} | {info['phone number']} | {info['email']}")


def search_contact(d: dict):
    name = input("Qidirilayotgan ism: ")
    found = False
    for phone, info in d.items():
        if info['name'].lower() == name.lower():
            print(f"Topildi: {info['name']} |  {info['phone number']} |  {info['email']}")
            found = True
    if not found:
        print("Bunday ismli kontakt topilmadi.")


def delete_contact(d: dict):
    phone = input("O‘chiriladigan telefon raqam: ")
    if phone in d:
        del d[phone]
        print("Kontakt o‘chirildi.")
    else:
        print("Bunday telefon raqam topilmadi.")


def update_contact(d: dict):
    phone = input("Yangilanadigan telefon raqam: ")
    if phone in d:
        new_name = input("Yangi ism: ")
        new_phone = input("Yangi telefon raqam: ")
        new_email = input("Yangi email: ")

        phone_pattern = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
        email_pattern = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"

        if not re.match(phone_pattern, new_phone):
            print("Telefon raqam formati noto‘g‘ri!")
            return
        if not re.match(email_pattern, new_email):
            print("Email formati noto‘g‘ri!")
            return

        d.pop(phone)
        d[new_phone] = {
            "name": new_name,
            "phone number": new_phone,
            "email": new_email
        }
        print("Kontakt yangilandi.")
    else:
        print("Bunday telefon raqam topilmadi.")


for _ in range(100):
    print("\n--- CONTACT MANAGER ---")
    print("1. Yangi kontakt qo‘shish")
    print("2. Barcha kontaktlarni ko‘rish")
    print("3. Kontakt qidirish")
    print("4. Kontaktni o‘chirish")
    print("5. Kontaktni yangilash")
    print("6. Chiqish")

    tanlov = input("Tanlovingiz: ")

    if tanlov == "1":
        add_contact(contacts)
    elif tanlov == "2":
        view_contacts(contacts)
    elif tanlov == "3":
        search_contact(contacts)
    elif tanlov == "4":
        delete_contact(contacts)
    elif tanlov == "5":
        update_contact(contacts)
    elif tanlov == "6":
        print("Dastur to‘xtatildi.")
        break
    else:
        print("Noto‘g‘ri tanlov!")


