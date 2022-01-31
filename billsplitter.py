# write your code here
import random
numberOfGuests = input("Enter the number of friends joining (including you): \n")
if numberOfGuests <= "0":
    print("No one is joining for the party")
    exit()

nameOfGuests_dict = {}
print("\nEnter the name of every friend (including you), each on a new line: ")
for guest in range(int(numberOfGuests)):
    nameOfGuests = input()
    nameOfGuests_dict[nameOfGuests] = 0
    # print("")

billTotal = input("\nEnter the total bill value: \n")
perPersonTotal = int(billTotal) / int(numberOfGuests)
perPersonTotal = round(perPersonTotal, 2)

enable_whoIsLucky = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
if enable_whoIsLucky == "No":
    print("\nNo one is going to be lucky\n")
    for k, v in nameOfGuests_dict.items():
        nameOfGuests_dict[k] = perPersonTotal
    print(nameOfGuests_dict)
    exit()

persons = list(nameOfGuests_dict)
whoIsLucky = random.choice(persons)

perPersonTotal = int(billTotal) / (int(numberOfGuests) - 1)
perPersonTotal = round(perPersonTotal, 2)

# Update the dictionary with new split values and 0 for the lucky person;
for k, v in nameOfGuests_dict.items():
    if k != whoIsLucky:
        nameOfGuests_dict[k] = perPersonTotal

print(f'\n{whoIsLucky} is the lucky one!\n')
print(nameOfGuests_dict)
