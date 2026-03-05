from telebot import TeleBot, types

bot = TeleBot("8242361499:AAGq0Yp9ECUALiaxvD2sixlRZu106weeAAY")  # Bot tokeningizni shu yerga yozing

# ================== FOYDALANUVCHI DATA ==================
user_step = {}
user_mode = {}
user_choice = {}
user_data = {}
products = {}

# ================== FORMULALAR ==================
formulas = {
    "KAN Truba 100":{"Uzunlik":1, "Unitaz":1, "Chashagen":1},
    "KAN Truba 50":{"Vanna":1, "Rakvina":1, "Kirmashina":1, "Taxorat":1},
    "PPR Truba 32 sovuq":{"Yomkist 350l":8, "Yomkist 500l":8, "Yomkist 650l":8, "Yomkist 750l":8, "Yomkist 1000l":8},
    "PPR Truba 25 sovuq":{"Yomkist 350l":8, "Yomkist 500l":8, "Yomkist 650l":8, "Yomkist 750l":8,"Yomkist 1000l":8},
    "PPR Truba 20 sovuq":{"Uzunlik":1, "Kenglik":1, "Dush":1, "Boiler 30l":1, "Boiler 50l":1, "Boiler 80l":1, "Boiler 100l":1, "Rakvina":1, "Unitaz":1, "Chashagen":1, "Mustahab":1, "Taxorat":1, "Kirmash":1},
    "PPR Truba 20 issiq":{"Uzunlik":1, "Kenglik":1, "Dush":1, "Rakvina":1, "Mustahab":1, "Taxorat":1, "Boiler 30l":1, "Boiler 50l":1, "Boiler 80l":1, "Boiler 100l":1},
    "KAN Atvot 100":{"Unitaz":2, "Chashagen":2},
    "KAN Atvot 50":{"Vanna":2, "Rakvina":1, "Taxorat":1, "Kirmashina":1},
    "PPR Atvot 32":{"Yomkist 350l":4, "Yomkist 500l":4, "Yomkist 650l":4, "Yomkist 750l":4, "Yomkist 1000l":4},
    "PPR Atvot 25":{"Yomkist 350l":8, "Yomkist 500l":8, "Yomkist 650l":8, "Yomkist 750l":8, "Yomkist 1000l":8},
    "PPR Atvot 20":{"Boiler 30l":4, "Boiler 50l":4, "Boiler 80l":4, "Boiler 100l":4, "Rakvina":2, "Unitaz":2, "Chashagen":2, "Mustahab":2, "Taxorat":2, "Kirmashina":2, "Dush":2},
    "KAN Pol Atvot 100":{"Unitaz":2, "Chashagen":2},
    "KAN Pol Atvot 50":{"Vanna":2, "Rakvina":2, "Taxorat":2, "Kirmashina":2},
    "PPR Pol Atvot 32":{"Yomkist 350l":2, "Yomkist 500l":2, "Yomkist 650l":2, "Yomkist 750l":2, "Yomkist 1000l":2},
    "PPR Pol Atvot 25":{"Yomkist 350l":2, "Yomkist 500l":2, "Yomkist 650l":2, "Yomkist 750l":2, "Yomkist 1000l":2},
    "PPR Pol Atvot 20":{"Boiler 30l":2, "Boiler 50l":2, "Boiler 80l":2, "Boiler 100l":2, "Rakvina":2, "Unitaz":1, "Chashagen":1, "Mustahab":2, "Taxorat":2, "Kirmashina":1, "Dush":2},
    "KAN Traynik 100×100":{"Unitaz":1, "Chashagen":1},
    "KAN Traynik 100×50":{"Vanna":1, "Taxorat":1, "Kirmashina":1},
    "PPR Traynik 32":{"Yomkist 350l":2, "Yomkist 500l":2, "Yomkist 650l":2, "Yomkist 750l":2, "Yomkist 1000l":2},
    "PPR Traynik 25":{"Yomkist 350l":2, "Yomkist 500l":2, "Yomkist 650l":2, "Yomkist 750l":2, "Yomkist 1000l":2},
    "PPR Traynik 20":{"Rakvina":2, "Dush":2, "Unitaz":1, "Chashagen":1, "Mustahab":2, "Taxorat":2, "Kirmashina":1, "Boiler 30l":2, "Boiler 50l":2, "Boiler 80l":2, "Boiler 100l":2},
    "KAN Mufta 100":{"Unitaz":1, "Chashagen":1, "Vanna":1, "Rakvina":1, "Taxorat":1, "Kirmashina":1},
    "KAN Mufta 50":{"Vanna":1, "Rakvina":1, "Tahorat":1,"Kirmashina":1},
    "PPR Mufta 32":{"PPR Truba 32 sovuq":0.25},
    "PPR Mufta 25":{"PPR Truba 25 sovuq":0.25},
    "PPR Mufta 20":{"PPR Truba 20 sovuq":0.25, "PPR Truba 20 issiq":0.25},
    "PPR Mo'stik 20":{"Boiler 30l":1, "Boiler 50l":1, "Boiler 80l":1, "Boiler 100l":1, "Dush":1, "Rakvina":1, "Mustahab":1, "Taxorat":1},
    "PPR Perexod 32×25":{"Yomkist":2},
    "PPR Perexod 25×20":{"Yomkist":2},
    "PPR Klipsa 32":{"PPR Truba 32 sovuq":3},
    "PPR Klipsa 25":{"PPR Truba 25 sovuq":3},
    "PPR Klipsa 20":{"PPR Truba 20 sovuq":3, "PPR Truba 20 issiq":3},
    "PPR Ushastik 20 (shablon) ichki":{"Dush":1, "Taxorat":1, "Mustahab":1},
    "PPR Ushastik 20 (1 talik) ichki":{"Rakvina":2, "Unitaz":1, "Chashagen":1, "Kirmashina":1},
    "PPR Krannik 25":{"Yomkist 350l":2, "Yomkist 500l":2, "Yomkist 650l":2, "Yomkist 750l":2, "Yomkist 1000l":2},
    "PPR Nakidnoy 25×3/4":{"Yomkist 350l":2, "Yomkist 500l":2, "Yomkist 650l":2, "Yomkist 750l":2, "Yomkist 1000l":2},
    "PPR Nakidnoy 25×1/2":{"Yomkist 350l":1, "Yomkist 500l":1, "Yomkist 650l":1, "Yomkist 750l":1, "Yomkist 1000l":1},
    "PPR Nakidnoy 20×1/2":{"Boiler 30l":2, "Boiler 50l":2, "Boiler 80l":2, "Boiler 100l":2},
    "Paplavoy 1/2":{"Yomkist 350l":1, "Yomkist 500l":1, "Yomkist 650l":1, "Yomkist 750l":1, "Yomkist 1000l":1},
    "Bosim uchun nasos 3/4":{"Yomkist 350l":1, "Yomkist 500l":1, "Yomkist 650l":1, "Yomkist 750l":1, "Yomkist 1000l":1},
    "Amerikanka 32 tashqi":{"Yomkist 350l":1, "Yomkist 500l":1, "Yomkist 650l":1, "Yomkist 750l":1, "Yomkist 1000l":1},
    "Vanna":{"Vanna":1},
    "Vanna sifon":{"Vanna":1},
    "Vanna plintus":{"Vanna":1},
    "Vanna duga":{"Dush":1},
    "Dush parda":{"Dush":1},
    "Dush trap":{"Trap":1, "Taxorat":1},
    "Rakvina":{"Rakvina":1},
    "Rakvina smesitel":{"Rakvina":1},
    "Rakvina sifon":{"Rakvina":1},
    "Rakvina kriplena":{"Rakvina":1},
    "Kantrol kran 1/2":{"Chashagen":1, "Unitaz":1, "Rakvina":2},
    "Kantrol kran 3/4":{"Kirmashina":1},
    "Unitaz":{"Unitaz":1},
    "Unitaz sifon":{"Unitaz":1},
    "Unitaz kriplena":{"Unitaz":1},
    "Bachok shlank":{"Unitaz":1, "Chashagen":1},
    "Chashagen":{"Chashagen":1},
    "Chashagen sifon":{"Chashagen":1},
    "Mustahab smesitel":{"Mustahab":1},
    "Taxorat smesitel":{"Taxorat":1},
    "Dush stayak":{"Dush":1},
    "Yomkist 350 litr":{"Yomkist 350l":1},
    "Yomkist 500 litr":{"Yomkist 500l":1},
    "Yomkist 650 litr":{"Yomkist 650l":1},
    "Yomkist 750 litr":{"Yomkist 750l":1},
    "Yomkist 1000 litr":{"Yomkist 1000l":1},
    "Suv isitgich 30 litr":{"Boiler 30l":1},
    "Suv isitgich 50 litr":{"Boiler 50l":1},
    "Suv isitgich 80 litr":{"Boiler 80l":1},
    "Suv isitgich 100 litr":{"Boiler 100l":1},

# Shu yerga boshqa fitinglar va ularning formulalarini qo'shasiz
}

# ================== FUNKSIYALAR ==================
def add_product(user_id, name, qty):
    try:
        qty = int(qty)
    except:
        qty = 0
    user_data.setdefault(user_id, {})
    user_data[user_id][name] = user_data[user_id].get(name, 0) + qty
    products.setdefault(user_id, {})
    products[user_id][name] = products[user_id].get(name, 0) + qty

def hisobla_va_chiqar(user_id):
    products.setdefault(user_id, {})
    hide = types.ReplyKeyboardRemove()
    bot.send_message(user_id, "📦 Hisoblanmoqda...", reply_markup=hide)

    result = {}

    # ================== FORMULALAR ASOSIDA HISOB ==================
    for fiting, rule in formulas.items():
        total = 0
        for product, count in rule.items():
            total += products[user_id].get(product, 0) * count
        if total > 0:
            result[fiting] = total

# === TRUBALARNI PRODUCTS GA QAYTARAMIZ (MUFTA/ KLIPSA HISOBI UCHUN) ===
    truba_list = [
        "PPR Truba 32 sovuq",
        "PPR Truba 25 sovuq",
        "PPR Truba 20 sovuq",
        "PPR Truba 20 issiq"
    ]

    for truba in truba_list:
        if truba in result:
            add_product(user_id, truba, result[truba])  # truba metrini lug'atga yozamiz

# === MUFTA VA KLIPSA HISOBI ===
    for fiting, rule in formulas.items():
        total = 0
        for product, factor in rule.items():
            qty = products[user_id].get(product, 0)
            total += qty * factor
        if total > 0:
            result[fiting] = round(total)

    # Topli pol hisob
    isitish = user_choice.get(user_id, "yoq")
    if isitish != "yoq":
        uzunlik = float(products[user_id].get("Uzunlik", 0))
        kenglik = float(products[user_id].get("Kenglik", 0))
        maydon = uzunlik * kenglik

        if isitish == "suv":
            result["Topli pol trubasi (metr)"] = round(maydon * 7)
            result["Penaplast (list)"] = round(maydon / 0.7)
            result["Alyumin folga (m²)"] = round(maydon)
            result["Skoba (dona)"] = round(maydon * 3)
        elif isitish == "kabel":
            result["Isitish kabeli (metr)"] = round(maydon * 10)
            result["Penaplast (list)"] = round(maydon / 0.7)
            result["Alyumin folga (m²)"] = round(maydon)
            result["Termoregulyator (datchik)"] = 1

    text = "📦 Kerakli materiallar:\n\n"
    for name in sorted(result):
        text += f"{name} : {result[name]}\n"

    bot.send_message(user_id, text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("/start")
    bot.send_message(user_id, "🔄 Yangi hisoblash uchun /start tugmasini bosing", reply_markup=markup)

    # Tozalash
    user_step[user_id] = "start"
    products[user_id] = {}
    user_choice[user_id] = {}
    user_data[user_id] = {}

# ================== START ==================
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    user_step[user_id] = "mode"
    user_mode[user_id] = None
    user_choice[user_id] = None
    user_data[user_id] = {}
    products[user_id] = {}

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("🏠 Hovli uy", "🏢 Honadon")
    bot.send_message(user_id, "Hisoblash turini tanlang:", reply_markup=markup)

# ================== ALL MESSAGES ==================
@bot.message_handler(func=lambda message: True)
def all_messages(message):
    user_id = message.chat.id
    text = message.text.strip()
    step = user_step.get(user_id, "start")

    # ---------- MODE ----------
    if step == "mode":
        if "Hovli" in text:
            user_mode[user_id] = "hovli"
        elif "Honadon" in text:
            user_mode[user_id] = "honadon"
        else:
            bot.send_message(user_id, "Iltimos tugmalardan birini tanlang.")
            return
        user_step[user_id] = "uzunlik"
        bot.send_message(user_id, "📏 Xamom uzunligini metrda kiriting (masalan: 5.2)")
        return

    # ---------- UZUNLIK ----------
    elif step == "uzunlik":
        try:
              value = float(text.replace(",", "."))
              add_product(user_id, "Uzunlik", value)
        except:
            bot.send_message(user_id, "Iltimos raqam kiriting")
            return
        user_step[user_id] = "kenglik"
        bot.send_message(user_id, "📏 Endi kenglikni kiriting:")
        return

    # ---------- KENGLIK ----------
    elif step == "kenglik":
        try:
            value = float(text.replace(",", "."))
            add_product(user_id, "Kenglik", value)
        except:
            bot.send_message(user_id, "Iltimos raqam kiriting.")
            return

        if user_mode.get(user_id) == "hovli":
            user_step[user_id] = "yomkist"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            markup.add("350l", "500l", "650l", "750l", "1000l", "Yo'q keyingisi")
            bot.send_message(user_id, "🛢 Yomkist hajmini tanlang:", reply_markup=markup)
        else:
            user_step[user_id] = "boiler"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            markup.add("30l", "50l", "80l", "100l", "Yo'q keyingisi")
            bot.send_message(user_id, " ⚡️Suv isitgich (ariston) qo'yamizmi?", reply_markup=markup)
        return

    # ---------- YOMKIST ----------
    elif step == "yomkist":
        if text != "Yo'q keyingisi":
            add_product(user_id, f"Yomkist {text}", 1)
        user_step[user_id] = "boiler"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add("30l", "50l", "80l", "100l", "Yo'q keyingisi")
        bot.send_message(user_id,"⚡️ Suv isitgich (ariston) qo'yamizmi?", reply_markup=markup)
        return

    # ---------- BOILER ----------
    elif step == "boiler":
        if text != "Yo'q keyingisi":
            add_product(user_id, f"Boiler {text}", 1)
        user_step[user_id] = "vanna"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add("Ha 1 dona", "Ha 2 dona", "Yo'q keyingisi")
        bot.send_message(user_id, "🛁 Vanna qo'yamizmi?", reply_markup=markup)
        return

    # ---------- VANNA ----------
    elif step == "vanna":
        if text.startswith("Ha"):
            qty = 2 if "2" in text else 1
            add_product(user_id, "Vanna", qty)
        else:
            add_product(user_id, "Vanna", 0)
            add_product(user_id, "Trap", 1)
        user_step[user_id] = "dush"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add("Ha 1 dona", "Ha 2 dona", "Yo'q")
        bot.send_message(user_id, "🚿 Dush smesiteli bormi?", reply_markup=markup)
        return

    # ---------- DUSH ----------
    elif step == "dush":
        if text.startswith("Ha"):
            qty = 2 if "2" in text else 1
            add_product(user_id, "Dush", qty)
        else:
            add_product(user_id, "Dush", 0)
        user_step[user_id] = "rakvina"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add("Ha 1 dona", "Ha 2 dona", "Yo'q keyingisi")
        bot.send_message(user_id, "🛀 Rakvina qo'yamizmi?", reply_markup=markup)
        return

    # ---------- RAKVINA ----------
    elif step == "rakvina":
        if text.startswith("Ha"):
            qty = 2 if "2" in text else 1
            add_product(user_id, "Rakvina", qty)
        else:
            add_product(user_id, "Rakvina", 0)
        user_step[user_id] = "unitaz"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        if user_mode.get(user_id) == "hovli":
            markup.add("Unitaz 1ta", "Unitaz 2ta",
                       "Chashagen 1ta", "Chashagen 2ta",
                       "Unitaz+Chashagen 1ta", "Unitaz+Chashagen 2ta",
                       "Yo'q keyingisi")
        else:
            markup.add("Unitaz 1ta", "Unitaz 2ta", "Yo'q keyingisi")
        bot.send_message(user_id, "🚽 Unitaz qo'yamizmi?", reply_markup=markup)
        return

    # ---------- UNITAZ ----------
    if step == "unitaz":
        if text == "Yo'q keyingisi":
            add_product(user_id, "Unitaz", 0)
            add_product(user_id, "Chashagen", 0)

        # Unitaz yo'q → Mustahab savoli chiqmaydi
            if user_mode.get(user_id) == "hovli":
                user_step[user_id] = "taxorat"
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.add("Ha 1 ta", "Ha 2 ta", "Yo'q keyingisi")
                bot.send_message(user_id, "💧 Taxorat uchun joy qo'yamizmi?", reply_markup=markup)
            else:
                user_step[user_id] = "kirmashina"
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.add("Ha 1 ta", "Ha 2 ta", "Yo'q keyingisi")
                bot.send_message(user_id, "🧺 Kir mashina uchun joy qoldiramizmi?", reply_markup=markup)
            re

    # Agar unitaz bor bo'lsa
        qty = 2 if "2ta" in text else 1
        if "Unitaz" in text:
            add_product(user_id, "Unitaz", qty)
        if user_mode.get(user_id) == "hovli" and "Chashagen" in text:
            add_product(user_id, "Chashagen", qty)

        # Unitaz bor → Mustahab savolini chiqaramiz
        user_step[user_id] = "mustahab"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Ha", "Yo'q keyingisi")
        bot.send_message(user_id, "🔧 Mustahab smesitel qo'yamizmi?", reply_markup=markup)

    # ---------- MUSTAHAB ----------
    if step == "mustahab":
        if text == "Ha":
            add_product(user_id, "Mustahab", 1)
        else:
            add_product(user_id, "Mustahab", 0)

        # Keyingi stepga o'tamiz
        if user_mode.get(user_id) == "hovli":
            user_step[user_id] = "taxorat"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add("Ha 1 ta", "Ha 2 ta", "Yo'q keyingisi")
            bot.send_message(user_id, "💧 Taxorat uchun joy qo'yamizmi?", reply_markup=markup)
        else:
            user_step[user_id] = "kirmashina"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add("Ha 1 ta", "Ha 2 ta", "Yo'q keyingisi")
            bot.send_message(user_id, "🧺 Kir mashina uchun joy qoldiramizmi?", reply_markup=markup)

    # ---------- TAXORAT ----------
    elif step == "taxorat":
        if text.startswith("Ha"):
            qty = 2 if "2" in text else 1
            add_product(user_id, "Taxorat", qty)
        else:
            add_product(user_id, "Taxorat", 0)
        user_step[user_id] = "kirmashina"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add("Ha 1 ta", "Ha 2 ta", "Yo'q keyingisi")
        bot.send_message(user_id, "🧺 Kir mashina uchun joy qoldiramizmi?", reply_markup=markup)
        return

    # ---------- KIR MASHINA ----------
    elif step == "kirmashina":
        if text.startswith("Ha"):
            qty = 2 if "2" in text else 1
            add_product(user_id, "Kirmashina", qty)
        else:
            add_product(user_id, "Kirmashina", 0)
        user_step[user_id] = "isitish"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add("Poldan suvlik", "Poldan kabellik", "Yo'q")
        bot.send_message(user_id, "🔥 Isitish tizimi turini tanlang:", reply_markup=markup)
        return

    # ---------- ISITISH ----------
    elif step == "isitish":
        if text == "Poldan suvlik":
            user_choice[user_id] = "suv"
        elif text == "Poldan kabellik":
            user_choice[user_id] = "kabel"
        else:
            user_choice[user_id] = "yoq"
        # Yakuniy natija
        hisobla_va_chiqar(user_id)
        return

# ================== BOT START ==================
bot.infinity_polling()
