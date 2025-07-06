def group_students(students):
    result = {}
    for student in students:
        group = student["group"]
        name = student["name"]
        result.setdefault(group, []).append(name)
    return result