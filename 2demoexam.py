# import json
#
# file_name = "2demoexam.json"
#
# def all_users():
#     try:
#         with open(file_name, "r", encoding="utf-8") as f:
#             data = f.read().strip()
#             if not data:
#                 return {}
#             try:
#                 return json.loads(data)
#             except json.JSONDecodeError:
#                 print("Hisoblar mavjud emas.")
#                 return {}
#     except FileNotFoundError:
#         return {}
#
# def save_accounts(data: dict):
#     with open(file_name, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=4)
#
# def clean_card(card):
#     return "".join(ch for ch in card if ch.isdigit())
#
# def is_valid_card(card):
#     card = clean_card(card)
#     return len(card) == 16 and card.isdigit()
#
# def is_valid_pin(pin):
#     return len(pin) == 4 and pin.isdigit()
#
# def create_account():
#     accounts = all_users()
#     acc_id = input("Yangi hisob ID: ").strip()
#     if not acc_id:
#         print("ID kiritilmadi.")
#         return
#     if acc_id in accounts:
#         print("Bunday ID allaqachon mavjud.")
#         return
#
#     name = input("Mijoz ismi: ").strip()
#
#     while True:
#         card = input("Karta raqami: ").strip()
#         card_clean = clean_card(card)
#         if not is_valid_card(card_clean):
#             print("Karta raqami 16 raqamdan iborat bo'lishi kerak.")
#             continue
#         exists = any(v.get("card") == card_clean for v in accounts.values())
#         if exists:
#             print("Bu karta allaqachon mavjud. Boshqa karta kiriting.")
#             continue
#         break
#
#     while True:
#         pin = input("PIN kod (4 raqam): ").strip()
#         if not is_valid_pin(pin):
#             print("PIN 4 raqamdan iborat bo'lishi kerak.")
#             continue
#         pin2 = input("PIN ni tasdiqlang: ").strip()
#         if pin != pin2:
#             print("PIN lar mos emas, qayta kiriting.")
#             continue
#         break
#
#     try:
#         balance = float(input("Dastlabki balans: ").strip() or 0)
#     except ValueError:
#         print("Noto'g'ri summa; 0 deb o'rnatildi.")
#         balance = 0.0
#
#     accounts[acc_id] = {
#         "name": name,
#         "balance": balance,
#         "sms": None,
#         "card": card_clean,
#         "pin": pin,
#         "pin_attempts": 0,
#         "blocked": False
#     }
#     save_accounts(accounts)
#     print(f"Hisob {acc_id} yaratildi. Karta: **** **** **** {card_clean[-4:]}")
#
# def login_by_card():
#     accounts = all_users()
#     if not accounts:
#         print("Hisoblar mavjud emas.")
#         return None
#
#     card = clean_card(input("Karta raqamingizni kiriting: ").strip())
#     for acc_id, v in accounts.items():
#         if v.get("card") == card:
#             if v.get("blocked"):
#                 print("Bu karta bloklangan.")
#                 return None
#
#             for i in range(3):
#                 pin = input("PIN kodni kiriting: ").strip()
#                 if pin == v.get("pin"):
#                     v["pin_attempts"] = 0
#                     save_accounts(accounts)
#                     print(f"{v.get('name','Mijoz')} hisobiga kirdingiz (ID: {acc_id})")
#                     return acc_id
#                 else:
#                     attempts = int(v.get("pin_attempts", 0)) + 1
#                     v["pin_attempts"] = attempts
#                     if attempts >= 3:
#                         v["blocked"] = True
#                         save_accounts(accounts)
#                         print("PIN 3 marta noto'g'ri kiritildi. Karta bloklandi.")
#                         return None
#                     save_accounts(accounts)
#                     left = 3 - attempts
#                     print(f"PIN noto‘g‘ri. Qolgan urinishlar: {left}")
#             return None
#
#     print("Karta topilmadi yoki noto‘g‘ri kiritildi.")
#     return None
#
# def choose_account():
#     accounts = all_users()
#     if not accounts:
#         print("Hisoblar mavjud emas. Yangi hisob yarating.")
#         return None
#
#     print("\nMavjud hisoblar:")
#     for k, v in accounts.items():
#         print(f"ID: {k} | {v.get('name','-')} | {v.get('card','-')} | {v.get('balance','-')} | SMS: {v.get('sms','-')}")
#
#     acc_id = input("Ishlash uchun hisob ID ni kiriting: ").strip()
#     if not acc_id:
#         return None
#     if acc_id not in accounts:
#         print("Bunday ID topilmadi.")
#         return None
#     if accounts[acc_id].get("blocked"):
#         print("Bu hisob bloklangan. Bank bilan bog'laning.")
#         return None
#
#     pin = input("PIN kodni kiriting: ").strip()
#     if pin == accounts[acc_id].get("pin"):
#         accounts[acc_id]["pin_attempts"] = 0
#         save_accounts(accounts)
#         print(f"{accounts[acc_id].get('name','Mijoz')} hisobiga muvaffaqiyatli kirdingiz (ID: {acc_id})")
#         return acc_id
#     else:
#         attempts = int(accounts[acc_id].get("pin_attempts", 0)) + 1
#         accounts[acc_id]["pin_attempts"] = attempts
#         if attempts >= 3:
#             accounts[acc_id]["blocked"] = True
#             save_accounts(accounts)
#             print("PIN 3 marta noto'g'ri kiritildi. Hisob bloklandi.")
#             return None
#         else:
#             save_accounts(accounts)
#             left = 3 - attempts
#             print(f"PIN noto‘g‘ri. Qolgan urinishlar: {left}")
#             return None
#
# def view_balance(acc_id):
#     accounts = all_users()
#     if not acc_id or acc_id not in accounts:
#         print("Hisob topilmadi.")
#         return
#     acc = accounts[acc_id]
#     sms_txt = acc.get("sms") or "sms xabarnomaga ulanmagan"
#     card = acc.get("card")
#     card_tail = f"**** **** **** {card[-4:]}" if card else "karta yo'q"
#     print(f"\nHisob ID: {acc_id}")
#     print(f"Ism: {acc.get('name')}")
#     print(f"Karta: {card_tail}")
#     print(f"Balans: {acc.get('balance')}")
#     print(f"SMS holati: {sms_txt}")
#
# def deposit(acc_id):
#     accounts = all_users()
#     if not acc_id or acc_id not in accounts:
#         print("Hisob topilmadi.")
#         return
#     try:
#         amt = float(input("Summa kiriting: ").strip())
#     except ValueError:
#         print("Noto'g'ri summa.")
#         return
#     accounts[acc_id]["balance"] = float(accounts[acc_id].get("balance", 0)) + amt
#     save_accounts(accounts)
#     print(f"{amt} qo'shildi. Yangi balans: {accounts[acc_id]['balance']}")
#     if accounts[acc_id].get("sms"):
#         print(f"Hisobingizga {amt} so'm qo‘shildi, balans: {accounts[acc_id]['balance']}")
#
# def pul_yechish(acc_id):
#     accounts = all_users()
#     if not acc_id or acc_id not in accounts:
#         print("Hisob topilmadi.")
#         return
#     try:
#         minus = float(input("Qancha yechmoqchisiz: ").strip())
#     except ValueError:
#         print("Noto'g'ri summa.")
#         return
#     current = float(accounts[acc_id].get("balance", 0))
#     if minus > current:
#         print("Hisobingizda yetarli mablag' yo'q.")
#         return
#     accounts[acc_id]["balance"] = current - minus
#     save_accounts(accounts)
#     print(f"{minus} yechildi. Qolgan balans: {accounts[acc_id]['balance']}")
#     if accounts[acc_id].get("sms"):
#         print(f"Hisobingizdan {minus} so'm yechildi, balans: {accounts[acc_id]['balance']}")
#
# def link_sms(acc_id):
#     accounts = all_users()
#     if not acc_id or acc_id not in accounts:
#         print("Hisob topilmadi.")
#         return
#     if accounts[acc_id].get("sms"):
#         print(f"SMS xabarnomaga ulangan: {accounts[acc_id]['sms']}")
#         return
#     phone = input("SMS uchun telefon raqam kiriting: ").strip()
#     accounts[acc_id]["sms"] = phone
#     save_accounts(accounts)
#     print(f"SMS xabarnoma {phone} bilan ulandi.")
#
# def unlink_sms(acc_id):
#     accounts = all_users()
#     if not acc_id or acc_id not in accounts:
#         print("Hisob topilmadi.")
#         return
#     if accounts[acc_id].get("sms"):
#         accounts[acc_id]["sms"] = None
#         save_accounts(accounts)
#         print("SMS xabarnoma o‘chirildi.")
#     else:
#         print("SMS xabarnoma ulanmagan.")
#
# def account_manager(acc_id):
#     while True:
#         print(f"\n=== Hisob: {acc_id} ===")
#         print("1. Balansni ko'rish")
#         print("2. Pul qo'shish")
#         print("3. Pul yechish")
#         print("4. SMS xabarnomani ulash")
#         print("5. SMS xabarnomani o'chirish")
#         print("0. Orqaga")
#         choice = input("Tanlang: ").strip()
#         if choice == "0":
#             break
#         elif choice == "1":
#             view_balance(acc_id)
#         elif choice == "2":
#             deposit(acc_id)
#         elif choice == "3":
#             pul_yechish(acc_id)
#         elif choice == "4":
#             link_sms(acc_id)
#         elif choice == "5":
#             unlink_sms(acc_id)
#         else:
#             print("Yuqoridagilardan birini tanlang.")
#
# def main_menu():
#     while True:
#         print("\n--- ATM MAIN MENU ---")
#         print("1. Hisob yaratish (yangi)")
#         print("2. Hisobga kirish")
#         print("3. Mavjud hisoblarni ko'rish")
#         print("0. Chiqish")
#         choice = input("Tanlang: ").strip()
#         if choice == "0":
#             print("Amal yakunlandi.")
#             break
#         elif choice == "1":
#             create_account()
#         elif choice == "2":
#             acc_id = login_by_card()
#             if acc_id:
#                 account_manager(acc_id)
#         elif choice == "3":
#             acc_id = choose_account()
#             if acc_id:
#                 account_manager(acc_id)
#         else:
#             print("Bunday raqam mavjud emas.")
#
#
# if __name__ == "__main__":
#     main_menu()
