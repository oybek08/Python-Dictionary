def group_by_age(people):
    result = {}
    for person in people:
        age = person["age"]
        name = person["name"]
        result.setdefault(age, []).append(name)
    return result