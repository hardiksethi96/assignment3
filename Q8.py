Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
set_a = Set1 ^ Set2
print(set_a)
set_b = Set1 ^ Set2 ^ Set3
print(set_b)
set_c = (Set1 & Set2) | (Set1 & Set3) | (Set2 & Set3)
print(set_c)
set_d = {x for x in range(1, 11)} - Set1
print(set_d)
set_e = {x for x in range(1, 11)} - Set1 - Set2 - Set3
print(set_e)
