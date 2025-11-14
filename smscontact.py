import json
from datetime import datetime

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"contacts": {}, "messages": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_contact(name, phone):
    data = load_data()
    if name in data["contacts"]:
        print("Bu ism allaqachon mavjud.")
    else:
        data["contacts"][name] = phone
        save_data(data)
        print(f"{name} kontakt qo‘shildi.")

def show_contacts():
    data = load_data()
    contacts = data["contacts"]
    if not contacts:
        print("Kontaktlar mavjud emas.")
    else:
        print("\n--- Kontaktlar ---")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        print("------------------")

def read_contact(name):
    data = load_data()
    phone = data["contacts"].get(name)
    if phone:
        print(f"{name}: {phone}")
    else:
        print("Bu ismli kontakt topilmadi.")

def get_phone(name):
    data = load_data()
    return data["contacts"].get(name)

def send_sms(name, message):
    data = load_data()
    phone = data["contacts"].get(name)
    if not phone:
        print("Bu ismli kontakt topilmadi!")
        return
    sms = {
        "to": name,
        "phone": phone,
        "message": message,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    data["messages"].append(sms)
    save_data(data)
    print(f"{name} ga SMS yuborildi!")

def view_sms():
    data = load_data()
    messages = data["messages"]
    if not messages:
        print("Hali SMS yuborilmagan.")
    else:
        print("\n--- Yuborilgan SMSlar ---")
        for msg in messages:
            print(f"Kimga: {msg['to']} | Tel: {msg['phone']} | Xabar: {msg['message']} | Sana: {msg['date']}")
        print("--------------------------")

def read_sms(name):
    data = load_data()
    messages = [msg for msg in data["messages"] if msg["to"] == name]
    if not messages:
        print(f"{name} ga hech qanday SMS yuborilmagan.")
    else:
        print(f"\n--- {name} ga yuborilgan SMSlar ---")
        for msg in messages:
            print(f"Xabar: {msg['message']} | Sana: {msg['date']}")
        print("--------------------------")

def main():
    while True:
        print("""
--- Contact & SMS Manager ---
1. Kontakt qo‘shish
2. Kontaktlarni ko‘rish
3. SMS yuborish
4. SMSlarni ko‘rish
5. Kontaktni o‘qish (Reader)
6. SMSlarni o‘qish (Reader)
0. Chiqish
        """)
        choice = input("Tanlang: ")

        if choice == "1":
            name = input("Ism: ")
            phone = input("Telefon: ")
            add_contact(name, phone)

        elif choice == "2":
            show_contacts()

        elif choice == "3":
            name = input("Kimga (ism): ")
            message = input("Xabar matni: ")
            send_sms(name, message)

        elif choice == "4":
            view_sms()

        elif choice == "5":
            name = input("Qaysi kontaktni o‘qish: ")
            read_contact(name)

        elif choice == "6":
            name = input("Qaysi kontaktning SMSlarini o‘qish: ")
            read_sms(name)

        elif choice == "0":
            print("Dastur tugadi.")
            break
        else:
            print("Noto‘g‘ri tanlov, qayta urinib ko‘ring.")

if __name__ == "__main__":
    main()