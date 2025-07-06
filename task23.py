def group_indices(numbers):
    result = {}
    for i, n in enumerate(numbers):
        result.setdefault(n, []).append(i)
    return result