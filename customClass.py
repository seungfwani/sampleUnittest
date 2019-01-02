
def custom_function(file_name):
    with open(file_name, 'rt') as f:
        return sum(1 for _ in f)
