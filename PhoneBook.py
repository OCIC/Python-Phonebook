#import statements
import os
import random
#A global variable used when handling writing onto a file 
keys_to_skip = 0 
#contacts_list is a python dictionary - a data type which stores key-value pairs
contacts_list = {}

#Since this program can make contacts, it is useful to be able to store them
# within a file so that they could be accessed later on 
 
# file_name contains the file location of a file 
# where the contacts will be stored
file_name = "C:/Users/lap/OneDrive/Desktop/Python projects/APCSP/contacts.txt"

#The line below, opens the file stored in the directory using utf8 fomratting
with open(file_name, encoding= "utf8") as file_object:
    
    #Create a list of lines from the file and 
    # store them in a variable, lines
    lines = file_object.readlines()

    # Main idea: The following format will be used to store 
    # each contact'information:
    # 444444444 - Phone number
    # First   }
    # Middle  }Full name 
    # Last    }
    # Thus when converting these lines into a list
    # the phone number will be index zero
    # followed by indecies 1 - 3 for the naming information
    # As a result the information of the succeeding contact
    # will start at index 4. So each new contact starts at 4 * n
    
    #For the above idea to work, n is initially zero
    n = 0
    #Through the while loop below we assing the key value pairs
    #to the contacts_list dictionary by doing the following:
    while n < len(lines):
        
        #int(lines[n]) - The key of a contact in the 
        # dictionary will be the contact's phone number stored
        # at line n as a string which is converted to an 
        # integer using the int() method 
        # lines[n + 1: n + 4] - the values held by that key
        # are the names stored in the three indecies following n.
        # We have an n + 4 for the second index since the range 
        # of a list excludes the end bound.

        #So the line below simply assigns the phone number 
        #as the key and the range of the 
        # list, lines, as the values stored in the dictionary
        contacts_list[int(lines[n].rstrip())] = lines[n + 1: n + 4]
        
        #The below variable stores the list held by the
        # aforementioned key. This is done in order to avoid
        # using the lengthy syntax of contacts_list[int(lines[n])]
        # as a name for the list of values whenever it is referenced
        # within the program 
        list_from_key = contacts_list[int(lines[n])]
        
        #The elements within each list contain \n at the end, 
        #part of the formatting of the file previously opened
        # This cause formating problems later on in the project 
        for element in list_from_key:
            #The above for loop loops through each list element, 
            #clears out the \n stored at the end using the rstrip() method
            #and reassings that formated element to the the same index in
            # the list_from_key list
            list_from_key[list_from_key.index(element)] = element.rstrip()
        keys_to_skip += 1    
        #Getting new values of n by using the formula n = n + 4
        n += 4
        """try:
            int(line)
            contacts_list[line] = []
        except:
            continue"""

#Once all information is extracted from the file, close it
file_object.close()       
        
#print(contacts_list) - line used for testing purposes 


#Function declarations

#Code for clear() obtained from https://stackoverflow.com/q/517970
#Function which clears the console of any text
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

#Function which takes in string of letters and returns
#a word with only the first letter capitalized
#words {list} - a list of strings 
#return formated {list} - list of strings with the first letter capitalized  

#code for infinitly many parameters https://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch15s09.html#:~:text=Python%20lets%20us%20define%20a,be%20collected%20into%20a%20tuple%20.
def format_capital_letter(*words):
    #list for storing formated words 
    formated_words = []
    
    """A python test in which the program attempts to:
    try:
        Store the lower case letters in a variable, lower_case_letters
        word[1: len(word)] - slice up the original word into a new 
        word which will contain the second letter of the 
        orignial word, index 1, and the last letter, the lenght of the word
        lower_case_letters = word[1: len(word)]
        if the above statement is successful then print the variable
        to the console
        print(lower_case_letters)
        
    except: - if an exception occurs print an error message to the console 
    As a result the program will not crash in case of an error
        #print("Sorry an error occured")
        
        Since the lower_case_letters line was successful 
        during the testing period 
        it can be used below without the test
    """
    #Simple counter variable meant for running a while loop
    counter = 0
    
    #While the value of counter is less than the length of the words list:
    while(counter < len(words)):
        
        #Store a word from the words list
        word = words[counter]
    
        #print(str(counter) + "Counter") - line meant for testing purposes
    
        #Capitalize the first letter, index 0, 
        #of the string using the upper() method
        capitalized = word[0].upper()
        
        #Seperate the other letters from the first letter 
        #and store them in a variable. 
        #Note: the lower() method conver ts 
        #all letters to lowercase form
        lower_letters = word[1: len(word)].lower()
        
        #Combine the capital letter with the remaining lowercase
        #letters to form a single word and store it in the variable formated 
        formated = capitalized + lower_letters
        
        #Insert the formated words to the list, formated_words
        formated_words.insert(counter, formated)

        #Update the counter variable
        counter += 1
        
    #Once the loop is complete, return the list, formated_words
    return formated_words

#Function which asks the user to enter a phone number of positive integers
#There are two possible outputs:
#return number {integer} - a positve integer returned only when the user enters positive integers to the console
#message {string} - in case the user doesn't enter a positive integer, an error message is printed to the screen
def ask_phone_number():
    #Use a while loop to make sure the user enters positive integers only
    while True:
    #Ask for a phone number
        number = input("\nEnter a phone number: ")
        #Clear the console
        clear()
        
        try:
            #Try to convert the user input into an integer
            int(number)
            #If successful, return the number as an integer
            return int(number)
        except:
            #In case of an exception
            #print an error message onto the screen
            print("\nEnter positive integers only")
    
    
#Function which takes in a list and prints a series of numbered lines.
# list {list} - a list of elements
# output: 
#[1] Element1
#[2] Element2
#[3] Element3
#[N] ElementN
#P.S: N - a positive integer
def display_numbered_lines(list):
    line_number = 1
    for information in list:
        #Show the inputs with bracket or line numbers
        #Convert all list elements into strings
        #"[" + str(line_number) + "] " - this line is responsible for
        #the bracket number style
        print("[" + str(line_number) + "] " +  str(information))
        
        #Update the line_number varibale by 1
        line_number += 1



#Function which takes in a list of words as strings and alphabetizes such strings.
# list {list} - a list of strings with words
#  return list {list} - a list of strings alphabetized
def alphabetize_list(list):

    #A list of characters in the alphabet
    alphabet = [
    "a", "b", "c","d","e",
    "f", "g", "h", "i", "j", 
    "k", "l", "m", "n","o",
    "p", "q", "r", "s", "t", 
    "u", "v", "w", "x", "y", "z"
    ]

    #The program below performs sorting by pairs which gets better
    #with more trial. The k variable keeps track of how many trials were conducted
    #and eventually stops the main while loop below
    k = 0
    while k < 50:

        i = 0
        while i < len(list) -1:

            #In order to alphabetize a list two words
            #have to be compared, thus two words from 
            #the list are stored in two sepearate variables, first_word, second_word
            first_word = list[i]
            second_word = list[i + 1]
            """try:
                #In case the index of the theoretical second word 
                # is larger that the input list's length, 
                # an instance for the occurance of an exception, 
                # then return the inputed list which will be
                # alphabetized after a few iterations 
                second_word = list[i + 1]
            except:
                return list"""
            #Go through each character in the string stored in first_word using a for loop 
            for char in first_word:
                #print(char) - line used for testing

                # char.lower() - gives the first letter of the string and converts it to lowercase
                # alphabet.index() - the index method is used to find the 
                # index of an argument inside the alphabet list

                # Main idea: if the first letter of the first word has a larger index than 
                # the first letter of the second word in the list alphabet, 
                # then the second word should go before the first_word 
                if alphabet.index(char.lower()) > alphabet.index(second_word[first_word.index(char)].lower()):
                    #As a result the values held the two pair indecies are switched around
                    list[i] = second_word

                    list[i + 1] = first_word

                    #Break out of the for loop and move 
                    #on to the next set of words
                    break    
                
                # Main idea: if the first letter of the first word matches the index of 
                # the first letter of the second word in the list alphabet: 
                if alphabet.index(char.lower()) == alphabet.index(second_word[first_word.index(char)].lower()):
                    # then the check to see if both words are the same
                    # Just in case the two words are written 
                    # with innappropriate capitalization, 
                    # convert both of them to lowercase form 
                    if first_word.lower() == second_word.lower():
                        #If the statement above evaluates to true
                        #break out of the for loop and move 
                        # on to the next set of words
                        break
                    #if the two words aren't the same, then continue through the
                    #for loop until two different characters are located
                    continue
                
                #If the character of the first word has a 
                #smaller index than the character of the second word within
                #the alphabet list, then nothing needs to be 
                #done except breaking out of the for loop and moving on
                #to the next set of words
                if alphabet.index(char.lower()) < alphabet.index(second_word[first_word.index(char)].lower()):
                    break
            #Once all analysis is complete, update the counter variable
            i += 1
        #Update the k variable when one sorting trial is complete
        k += 1
    
    #At the end return the same list, but alphabetized
    return list


#Function idea from #Function idea from https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
#Function which takes in a value that is supposed to be associated with some key, which if found
#within the contacts_list dictionary, is returned. Otherwise a string holding an error message is returned
# val {string} - a string stored as a value in the contacts_list dictionary
# return key {any data type} - any data type which serves as the key to the value passed as an argument
# return "Error" {string} - a string returned in case the desired key isn't found  
def find_key(val):
    #Search through the key value pairs stored in the contacts_list dictionary
    for key, value in contacts_list.items():
        #If the value matches the requested value then return the appropriate key
        if val == value[0]:
            return key
    return "Error"


    
# Function which prints the key value pairs 
# stored in the dictionary contacts_info in the following style:
# First Full Name - Phone number
# Second Full Name - Phone number 
def show_contacts_info(alphabetize= False):
    #A counter variable meant to keep track of the line numbers
    #that are going to be used 
    #in the format described in the function's API
    counter = 1

    #A list which will store all the full names created later
    fully_names = []
    #Tell the user what you are describing with each line
    print("        Name       Phone number ")

    #Split the keys form the dictionary's values through the items() method
    # store the keys in a variable, number and the values in varable names
    # Note: only a single value and a single key is stored through each iteration  
    for number, names in contacts_list.items():

        full_name = ""    
        for name in names:

            #Make sure the full_name doesn't contain any NOs, 
            # since the user could've entered NO for any input field 
            #they didn't wish to fill out during the data gathering process

            #So check if at any point through the looping process 
            # the list of names contains a NO. If so do not add such data to the full_name variable
            if name.lower() == "no":
                #The continue keyword helps in the skipping process 
                continue
            
            #Since the if statement above takes care of the aforementioned scenario
            #add any string stored in the name variable to 
            # the full_name variable to generate a full name
            full_name += name + " "

        #However the full_name variable will be left blank 
        # if the user entered NO for all name input fields
        #In such a case a default value is assinged to the variable
        if full_name == "":
            #Assignment of default value
            full_name = "No Name "
        
        # Once the above lines are executed, 
        # combine the full name and the contact's phone number
        # into a single line that will be printed onto 
        # the screen in the format described in the function's API

        if alphabetize == True:
            fully_names.append(full_name)
        else:
            print("\n[" + str(counter) + "] " + full_name + "- " + str(number))
            counter += 1
     
    if alphabetize == True:

        numbers = list(contacts_list.keys())
        alpha_names = alphabetize_list(fully_names)
        counter = 0
        while counter < len(numbers):
            #alpha_names[counter].split()[0] - since the full name 
            # (found within the alpha_names list at some index, a value stored in the counter) 
            # is multiple words fused together it is necessary to convert the string into a list 
            # of words using the split() method.
            # Once converted we take the first word of in this list
            # and convert it to an all lowercase letter format
            #print(alpha_names[counter].split()[0]) #- line used for testing
            print(
                "\n[" + str(counter + 1) +  "] " + alpha_names[counter] + " - " 
                + str(find_key(alpha_names[counter].split()[0]) ) 
                )    
            counter += 1
    
    """ for number,names in contacts_list.items():
        for name in names:
            print(name)
        #Create an empty full_name variable in
        #which the full name of the user is stored
        
        #Clear the list with the naming information, names from any NOs
        for field in names:
            #If the element which is stored in field is the string "no"
            if field.lower() == "no":
                #Delete the element stored at the index of the variable field
                #names.index(field.lower()) - a way to find the index of the field variable
                del names[names.index(field.lower())]
                
        #Once the list is cleared and only the names remain do the following:
        
        #Check to see if anything is in the list; 
        #the user may have put No for all
        #naming fields and thus made the length of the cleared list 0 
        if len(names) != 0:
            
            for part in names:
                #Create a full name by combining the contents of the full_name variable
                #and the value stored in the part variable which loops through all
                #the elements of the list, names.
                #Put a space inbetween the two strings
                full_name = full_name + " " + part
    print(full_name)    
    #Print out the output as a numbered line 
    #with the contact's name and phone number
    #print("[" + str(counter) + "] " + full_name + " - " + str(number))
"""

clear()

#Print a short description of the program
print("Create contacts with this program"
+ "\nPut NO for any information that you don't want to enter or alter")


flag = True
while flag:

    #A list of actions that the user can execute with the program
    actions = [
    "Quit",
    "View contacts",
    "Alphabetize contacts",
    "Random contact"
    ]
    
    #Ask the user whether they want to create a contact
    ask = input("\nDo you want to create a contact[Yes/No]: ")
    
    #Convert the text the user enters to all lower case in case they 
    #do not enter something properly
    if ask.lower() == "yes":
        #Begin by asking the user to enter a phone number through the 
        #function ask_phone_number()
        phone_number = ask_phone_number()
         
        #Ask for the full name of the contact in seperate pieces: 
        #first name, middle name and last name
        first_name = input("\nEnter first name of contact: ")
        middle_name = input("\nEnter middle name of contact: ")
        last_name = input("\nEnter last name of contact: ")
    
        #Format the names properly using 
        #the format_capital_letter function.
        #As a result only the first letter of each word is left capitalized. 
        #Store the output in another list, temporary_list
        temporary_list = format_capital_letter(first_name, middle_name, last_name)

        #Clear the console
        clear()
        
        #Add the phone_number to the temporary_list
        temporary_list.append(phone_number) 
    
        print("\nYou have entered the following name information:")
        #Show the user their inputs in a numbered line format
        #Go to the fucntion decalrtion section for more details
        #on the display_numbered_lines function
        display_numbered_lines(temporary_list)
    
        #Ask the user whether they are happy with what they entered
        #Use the while loop to make sure they enter only yes or no
        while True: 
            ask_change = input("Do you want to change anything[Yes/No]: ")
            
            #If the user enters either yes or no do the following
            if(ask_change.lower() == "yes" or ask_change.lower() == "no"):
                #break out of the loop
                break
            #In case they enter something else
            else:
                #Print an error message
                #And continue to ask them whether 
                #they want to alter any info
                print("\nPlease enter yes or no")
        
        #If the input stored in the variable, ask_change is yes:
        if ask_change.lower() == "yes":
            change = ""
            #Open a while loop which runs until the user enters no
            while True:
                
                #Ask them what specifically they wanted changed
                change = input("\nEnter a valid bracket number to alter information: ")
                if change.lower() == "no":
                    #In case the input is no, clear the console of any input
                    clear()

                    #Break out of the while loop
                    break
                #try to convert the input stored in the change variable into an 
                #an integer. 
                try:
                    int(change)
                    
                    #If successful show the appropriate input field to the user
                    #depending on the number entered in the variable
                    if int(change) == 1:

                        first_name = input("\nEnter first name of contact: ")

                        #The line below assigns the new value of first_name to
                        #the list, temporary_list using the format_capital_letter 
                        #funciton to format the passed string properly. 
                        #Since the function takes in a list of values and that list
                        #will contain only one element (at index 0) we want to assign only
                        #that element to temporary_list. Otherwise we would have a nested list
                        #or a list within a list.
                        temporary_list[0] = format_capital_letter(first_name)[0]
                    elif int(change) == 2:
                        
                        #Prompt the user to enter the information
                        middle_name = input("\nEnter middle name of contact: ")
                        
                        #Store the information in the temporary_list list
                        #Note: refer to the comment in the main if statement for more
                        #details on the syntax regarding the use of the
                        #function format_capital_letter
                        temporary_list[1] = format_capital_letter(middle_name)[0]
                        

                    elif int(change) == 3:
                        
                        last_name = input("\nEnter last name of contact: ")

                        #Store the value in temporary_list and formatting it properly 
                        temporary_list[2] = format_capital_letter(last_name)[0]

                    elif int(change) == 4:
                        
                        phone_number = ask_phone_number()
                        temporary_list[-1] = phone_number
                    

                    #If the user entered an integer outside the domain 0 < x < 5 
                    else:
                        #Continue on, getting back to the beginning of the loop
                        #and try asking the user the same questions all over again
                        continue
                    
                    #Clear the console of any text
                    clear()

                    print("\nYou have entered the following name information:")
                    #Show the user their inputs in a numbered line format
                    #Go to the fucntion decalrtion section for more details
                    #on the display_numbered_lines function
                    display_numbered_lines(temporary_list)

                #In case the user entered something other than an integer, 
                #a scenario which would prompt an error to occur do the following 
                except: #Recognise the exception and continue running the program
                        #instead of crushing it and ruining the user experience
                        
                    #Clear the console
                    clear()
                    
                    #Remind the user that they can enter no to avoid the input field
                    print("Enter NO if you don't want to alter anything\n")
                    
                    #Print the user's inputs with numbered lines
                    display_numbered_lines(temporary_list)
                    
                    #Tell the user they have entered an invalid input
                    print("\nInvalid input\n")
                    
            #Once complete, the program will get back to the beginning of the
            #loop and will ask the user to enter a valid line number
                       
        #After all inputs are collected, store the information
        #in the contacts_list dictionary using the phone number (index -1
        # of the temporary_list) as a key and the rest of the 
        #temporary_list (elements with indexes between 0 and 3) as the value.
        contacts_list[temporary_list[-1]] = temporary_list[0:3]
        #print(contacts_list) - line used for testing

        temporary_list = []
            
    if ask.lower() == "no":
    
        #Clear the console
        clear()
        
        #Inform the user of the possible actions they could enter 
        print("Other actions include:")
        
        #Print the list of actions onto the screen with numbered lines 
        display_numbered_lines(actions)
        
        #pick is a variable which stores the user's bracket number 
        #The while loop below is used to make sure that the user enters a number
        #between 1 < x < 5 since there are 4 possible options to chose from.
        # int(pick) == ValueError - this statement ensures that even in case of an error 
        # the program will keep running and prompt the user to enter a valid bracket number 
        pick = 0
        while int(pick) < 1 or int(pick) > 4:

            pick = input("\nEnter a valid bracket number to proceed: ")

            #Try to convert the user's input in an integer
            try:
                
                int(pick)

            #In case the above fails, a ValueError will be raised
            except ValueError:
                #Asaign a value of 0 to pick so that the while loop can continue
                pick = 0
                #Do not crash the program, but continue 
                #to run the while loop until a valid integer is entered
                continue

        #If statements for each action in the actions list


        # if the user enters 1 then set the falg variable to false
        # and thus break out of the while loop 
        if int(pick) == 1:
            
            flag = False
        
        # if the user enters 2 then show them their contacts 
        # using the show_contacts_info function 
        # (go to function declaration for more detals)
        if int(pick) == 2:
            #Clear out the console of any text
            clear()

            #Print contacts 
            show_contacts_info()

        # if the user enters 3 then show them their contacts 
        # using the show_contacts_info function and passing the True argument
        # to tell the function to alphabetically dispay the contacts
        # (go to function declaration for more detals)
        if int(pick) == 3:
            #Clear out the console of any text
            clear()

            #Print contacts alphabetically
            show_contacts_info(True)

        # if the user enters 4 then print a random contact onto the screen
        # using the random.choice function to select a random values of the list
        # of dictionary keys obtained throgh the keys() method
        if int(pick) == 4:
            #Clear the console of any text
            clear()

            print("Your random contact")
            #Picking a random key 
            random_key = random.choice(list(contacts_list.keys()))

            #Print the random contact in a proper format
            print("\n[1] " + contacts_list[random_key][0] + " - "  + str(random_key))

#Print the newly contacts onto the screen
#The below line opens the file in append mode so that it can be written on it
with open(file_name, "a", encoding= "utf8", ) as f_object:
    #Loop through the list of keys in the contacts_list dictionary
    for key in contacts_list.keys(): 
        #if the index of the key picked during the looping process
        # is less than the integer value stored in keys_to_skip, 
        #then skip over to the next iteration of the loop 
        if list(contacts_list.keys()).index(key) < keys_to_skip:
            continue
        else:

            #Once the loop skips all the contacts that are already written 
            #onto the file, it can start writing all other contacts 
            #stored in the dictionary using the write() method
            
            #First it writes the key, the phone number
            f_object.write("\n" + str(key))

            #Then, using a for loop, it prints all the information held within
            #the value unlocked by the key
            for element in contacts_list[key]:
                f_object.write("\n" + element)

#print(contacts_list) - line used for testing
print("\nThank you for using our program")       
f_object.close()


                    
                
                    
                
    
    