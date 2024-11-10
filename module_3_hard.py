def calculate_structure_sum(data_structure):
    sum = 0
    def recursive_sum(element):
        nonlocal sum
        if isinstance(element, (list, tuple)):
            for i in element:
                recursive_sum(i)
        elif isinstance(element, dict):
            for i, v in element.items():
                recursive_sum(i)
                recursive_sum(v)
        elif isinstance(element, str):
            sum += len(element)
        elif isinstance(element, (int, float)):
            sum += element
    for item in data_structure:
        recursive_sum(item)
    return sum
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)