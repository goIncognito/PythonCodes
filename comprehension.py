data = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]
old_value = "Bob"
new_value = "Robert"

data = [(i, new_value) if name == old_value else (i, name) for i, name in data]
print(data)
