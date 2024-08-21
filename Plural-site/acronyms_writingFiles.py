def find_acronym():
    look_up = input("What software acronym would you like to look up?\n")

    found = False

    with open('.\Plural-site\software_Acronyms.txt') as file:
        for line in file:
            if look_up in line:
                print(line)
                found = True
                break

    if not found:
        print('The acronym does not exist.')

def add_acronym():
    acronym = input('What acronym do you want to add?\n')
    definition = input('What is the definition?\n')
    with open('.\Plural-site\software_Acronyms.txt', 'a') as file:  # Open the file in append mode
        file.write(acronym + ': ' + definition + '\n')

def main():
    # ask the user whether they want to find or add an acronym
    choice = input('Do you want to find (F) or add (A) an acronym? ')
    if choice.upper() == 'F':
        find_acronym()
    elif choice.upper() == 'A':
        add_acronym()
    else:
        print('You chose the wrong option.')

main()
