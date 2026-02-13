# a = 10, a adalah variable dengan nilai 10

# tipe data: angka satuan {integer}
data_integer = 1
print(type(data_integer))
print("1. data: ", data_integer) 
print("- bertipe", type(data_integer))

# tipe data: angka dengan koma (float)
# python tidak ada double
data_float = 1.5
print("2. data: ", data_float) 
print("- bertipe", type(data_float))

# tipe data: kumpulan karakter (string)
data_string = "ucup"
print("3. data: ", data_string) 
print("- bertipe", type(data_string))

# tipe data: True(1)/False(0) (boolean)
data_boolean = True
print("4. data: ", data_boolean) 
print("- bertipe", type(data_boolean))

data_boolean = False
print("4.1. data: ", data_boolean) 
print("- bertipe", type(data_boolean))

# tipe data: khusus

# bilangan kompleks
data_complex = complex(5,6)
print("5. data: ", data_complex) 
print("- bertipe", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double, c_char
data_c_double = c_double(10.5)
print("6. data: ", data_c_double) 
print("- bertipe", type(data_c_double))