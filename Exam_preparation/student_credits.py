def students_credits(*args):
    credits_info = []
    total_credits = 0
    for course in args:
        course_name, *info = [int(x) if x.isdigit() else x for x in course.split("-")]
        credits = info[0]
        max_test_points = info[1]
        diyans_points = info[2]
        credits_gained = (credits * diyans_points) / max_test_points
        total_credits += credits_gained
        credits_info.append((course_name, credits_gained))
    credits_info.sort(key=lambda x: x[1], reverse=True)
    if total_credits >= 240:
        message =  f"Diyan gets a diploma with {total_credits:.1f} credits."
    else:
        message =  f"Diyan needs {240 - total_credits:.1f} credits more for a diploma."

    result = message + "\n"

    for course in credits_info:
        result += f"{course[0]} - {course[1]:.1f}\n"

    return result


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
