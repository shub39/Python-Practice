'''
20.Delete a list of keys from a dictionary
'''
sample_dict = {
    "name" : "Kelly",
    "age" : 25,
    "salary" : 8000,
    "city" : "New york"}
keys = ["name","salary"]
dict1 = {k: sample_dict[k] for k in sample_dict.keys() - keys}
print(dict1)
