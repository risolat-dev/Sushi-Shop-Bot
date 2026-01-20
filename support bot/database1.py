courses = [{"name": "Python", "paid": False},
           {"name": "Java", "paid": True},
           {"name": "JavaScript", "paid": False}]

courses_lessons = {
    "Python": ["Dars 1: Kirish", "Dars 2: O'zgaruvchilar", "Dars 3: Funksiyalar"],
    "Java": ["Dars 1: Kirish", "Dars 2: OOP", "Dars 3: Exception"],
    "JavaScript": ["Dars 1: Kirish", "Dars 2: DOM", "Dars 3: Function"]
}

user_progress = {}  # {'user_id': {'Python': 0}}
