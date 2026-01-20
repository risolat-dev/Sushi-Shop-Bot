from database1 import courses, courses_lessons, user_progress

def check_course_exists(course_name):
    return next((c for c in courses if c["name"].lower() == course_name.lower()), None)

def update_user_progress(user_id, course_name):
    if user_id not in user_progress:
        user_progress[user_id] = {}
    if course_name not in user_progress[user_id]:
        user_progress[user_id][course_name] = 0

    index = user_progress[user_id][course_name]
    lessons = courses_lessons.get(course_name, [])
    if index < len(lessons):
        user_progress[user_id][course_name] += 1
        return lessons[index], False
    else:
        return None, True

def get_user_current_course(user_id):
    if user_id in user_progress:
        for course_name, index in user_progress[user_id].items():
            if index < len(courses_lessons[course_name]):
                return course_name
    return None

def add_course(course_name, paid=False):
    courses.append({"name": course_name, "paid": paid})
