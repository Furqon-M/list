## ----- LIST -----

# KUMPULAN DATA NUMBERS
data_angka = [1,5,2,3]
print(data_angka)

# KUMPULAN DATA STRINGS
data_string = ["satu", "dua", "tiga"]
print(data_string)

# KUMPULAN DATA BOOLEAN
data_boolean = [True, False, True, True]
print(data_boolean)

# KUMPULAN DATA CAMPURAN
data_campuran = [1, "dua", True, "cireng"]
print(data_campuran)

## cara alternatif membuat list
data_range = range(0,10,2) # range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
# list_pake_for = [i for i in range(0,10)]
list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i != 5]
print(list_pake_for_if)

# GENAP
list_pake_for_if = [i for i in range(0,10) if i % 2 == 0]
print(list_pake_for_if)

# GANJIL
list_pake_for_if = [i for i in range(0,10) if i % 2 != 0]
print(list_pake_for_if)

# GANJIL DI KUADRAT
list_pake_for_if = [i**2 for i in range(0,10) if i % 2 != 0]
print(list_pake_for_if)