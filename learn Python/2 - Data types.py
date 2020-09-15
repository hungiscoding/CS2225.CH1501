# int
print(type(1));

# float
print(type(1.5));

# complex (số phức)
z = complex(2,3);
print(type(z));

# string
print(type('1'));
# print(type('1' + 1)); can only concatenate str (not 'int') to str

# boolean
print(type(True));

# list
list = [1, 'a', 2]
print(type(list));
for item in list:
    print(item);

# tuple
tuple = (1, 'a', 2)
print(type(tuple));
for item in tuple:
    print(item);

# range
r = range(6)
print(type(r));
for index in r:
    print(index);

# dictionary
d = {'key1': 1, 'key2': 'value2'};
print(type(d));
for key in d:
    print(key);     # key
    print(d[key]);  # value

# set
s = {1, 'a', 2};
print(type(s));
for item in s:
    print(item);

# frozenset 
fs = frozenset({1, 'a', 2});
print(type(fs));
for item in fs:
    print(item);

# bytes
byte = b"Hello"	
print(byte);
print(type(byte));

# bytearray
ba = bytearray(5)
print(ba);
print(type(ba));

# memoryview
mv = memoryview(bytes(5))
print(mv);
print(type(mv));

# My questions:
    # What is the difference between list, tuple & set