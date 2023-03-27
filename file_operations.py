import os.path
import shelve

# path concat
path = os.path.join('/home', 'Users')
print(path)
# current path
path = os.getcwd()
print(path)
# change dir
os.chdir('../')
path = os.getcwd()
print(path)

# recursive create dir
try:
    os.makedirs('./tmp/sub')
except FileExistsError:
    print('existed')

# relative path to absolute path
abs_path = os.path.abspath('./')
print('', abs_path)
# check if absolute path
print(os.path.isabs(abs_path))

os.chdir('data-processing-basic')

# open file
readme_file = open('./README.md')
# read file
content = readme_file.read()
print(content)
readme_file.close()
print("======")
# read file line
readme_file = open('./README.md')
content_line = readme_file.readlines()
print(content_line)

# write file, coverage
write_file = open('./text.txt', 'w')
write_file.write('hello python')
write_file.close()

# write file, add
write_file = open('./text1.txt', 'a')
write_file.write('hello python\n')
write_file.close()

# shelve  save bin file
shelve_file = shelve.open('./text2.txt')
shelve_file['fruit'] = 'apple'  # key-value's pattern
shelve_file.close()
# shelve read bin file
shelve_file = shelve.open('./text2.txt')
print(shelve_file['fruit'])  # list(shelve_file.keys())  list(shelve_file.values())
shelve_file.close()
