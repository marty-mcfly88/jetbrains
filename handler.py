import sys
import os
import hashlib

if len(sys.argv) < 2:
    print("Directory is not specified")
else:
    path_to_process = sys.argv[1]
# ".\\" +
print("Enter file format:")
file_format = input()
print()

print("Size sorting options:")
print("1. Descending")
print("2. Ascending")

while True:
    print()
    print("Enter a sorting option:")
    sorting = input()
    if sorting not in ('1', '2'):
        print("Wrong option")
        continue
    else:
        break

files_info = {}
names_list = []

for root, dirs, files in os.walk(path_to_process, topdown=False):
    for name in files:
        if file_format == "":
            search = name
        else:
            search = "." + file_format
        if search in name:
            full_name = os.path.join(root, name)
            size = os.path.getsize(os.path.join(root, name))
            if size in files_info.keys():
                names_list = files_info[size]
                names_list.append(full_name)
                files_info[size] = names_list
            else:
                names_list = [full_name]
                files_info[size] = names_list

if sorting == '1':
    sorted_files = sorted(files_info, reverse=True)
else:
    sorted_files = sorted(files_info)

for x in sorted_files:
    if len(files_info[x]) > 1:
        print(f"{x} bytes")
        for y in files_info[x]:
            print(y)

print()

while True:
    print()
    print("Check for duplicates?")
    check_dublicate = input()
    if check_dublicate not in ('yes', 'no'):
        print("Wrong option")
        continue
    else:
        break

if check_dublicate == 'yes':
    counter = 1
    for x in sorted_files:
        if len(files_info[x]) > 1:
            print(f"{x} bytes")
            hash_dict = {}
            for y in files_info[x]:
                with open(y, 'rb') as file_2_hash:
                    hash = hashlib.md5(file_2_hash.read())
                    if hash.hexdigest() in hash_dict.keys():
                        names_list = hash_dict[hash.hexdigest()]
                        names_list.append(y)
                        hash_dict[hash.hexdigest()] = names_list
                    else:
                        names_list = [y]
                        hash_dict[hash.hexdigest()] = names_list
            for y in hash_dict.keys():
                if len(hash_dict[y]) > 1:
                    print(f'Hash {y}')
                    files_list = hash_dict[y]
                    for z in files_list:
                        print(f'{counter}. {z}')
                        counter += 1
# Should we delete
while True:
    print()
    print("Delete files?")
    to_delete_or_not = input()
    if to_delete_or_not not in ('yes', 'no'):
        print("Wrong option")
        continue
    else:
        break


# Get files to delete
def check_input(input_list):
    all_ints = False
    for i in input_list:
        if i.isdigit():
            continue
        else:
            all_ints = False
            return all_ints
    all_ints = True
    return all_ints


while True:
    print()
    print("Enter file numbers to delete:")
    files_to_delete = input().split()
    if not check_input(list(files_to_delete)):
        print("Wrong format")
        continue
    elif not files_to_delete:
        print("Wrong format")
        continue
    else:
        break
# print(files_to_delete)


if to_delete_or_not == 'yes':
    counter = 1
    freed_space = 0
    for x in sorted_files:
        if len(files_info[x]) > 1:
            print(f"{x} bytes")
            hash_dict = {}
            for y in files_info[x]:
                with open(y, 'rb') as file_2_hash:
                    hash = hashlib.md5(file_2_hash.read())
                    if hash.hexdigest() in hash_dict.keys():
                        names_list = hash_dict[hash.hexdigest()]
                        names_list.append(y)
                        hash_dict[hash.hexdigest()] = names_list
                    else:
                        names_list = [y]
                        hash_dict[hash.hexdigest()] = names_list
            for y in hash_dict.keys():
                if len(hash_dict[y]) > 1:
                    print(f'Hash {y}')
                    files_list = hash_dict[y]
                    for z in files_list:
                        if str(counter) in files_to_delete:
                            freed_space += x
                            os.remove(z)
                            # print(f'{counter}. {z}')
                        counter += 1
print(f'Total freed up space: {freed_space} bytes')
