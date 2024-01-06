print ("Hello! I am your Unibuddy. Nice meeting you. I am here to help you. ")

print( "Please enter some details before we start chatting. ")# the user is requested to enter some personal information

user_name = input("Please enter your full name : ").capitalize()# the user enters hers/his full name: first name and the surname as requested

user_age =float(input("Please enter your age : "))# the user enters the age

fav_colour = input("Please enter your favourite colour: ").capitalize()# the user enters hers/his favourite colour

if not user_name.isalpha():
  print("Error. You have forgotten to enter your full name. Please try again.")# the user did not enter any [user_name], the programme is sending an error message asking to re-enter the full name

if not fav_colour.isalpha():
  print("No colour entrance. Please try again.")# the programme reminds the user to enter a colour name'''

else:
  print(f"Welcome {user_name}. I am here to help and advise you. ")# the programme is encouraging the user to continue
#break

'''except ValueError as 'NO':
print("NO")
print("You have not entered a number indicating your age. Please try again! ")# the user did not enter any information on their age. The programme prompts the user to try it again.'''

# while:
# the entrance of the age classifies the students into different age groups. Age is an integer.
if user_age >= 15 and user_age <= 17:# age group [15, 17]: 15 to 17 year olds, where the numbers 15 and 17 are included
   
   print("You are a Whizz!")

if user_age >= 18 and user_age <= 21:# age between 18 and 21: the students belong to the freshman group. Ages 18 and 21 both are included.
   print(" You are a freshman. I would like to provide you with some information on freshman - specific events: ")   
   print("""
1. There are several meetings arranged to find out more about the lectures and exam tables. 

2. There are several parties happening on the campus grounds. Keep your eyes open!

3. Don't forget to purchase your gown for upcoming events, such as the Halloween ball, the Winter ball and the Spring ball. 
There will be many more occasions for you to use the gown.
""")
   
if user_age > 21 and user_age < 26:
   print("You belong to Young Adulthood group. Welcome to our campus.")

elif user_age >= 26 and user_age <= 34:# mature undegraduate group, where 26 and 34 are included
   print("You are a mature undergraduate student! I hope you will enjoy your time at our University!")

elif user_age >= 35 and user_age <= 67:# anyone above 34 and studying are classified as a postgraduate group member

   print("You are a postgraduate student. Nice meeting you! Age is no barrier.")# one's age should not restrict their abilities
#else:
#  print("I am not sure you have entered the required information. Please enter your age.")

   # the user is requested to type in the favourite colour. The colour is associated with the the clubs and societies at the University.
if fav_colour == "Red": # user's favourite colour is red. Suggestions about possibilities to join certain clubs.
   print("I can see your favourite colour is RED: just like mine. Try considering the following clubs: ")
   print("""
1. Red Poet Society. 
2. Red Football Team. Could it be Manchester United?!
3. Red Elephant Club. Bridge club.
""")

elif fav_colour == "Blue":# user's favourite colour is blue. Suggestions about possibilities to join certain clubs.
   print("I see your favourite colour is BLUE! Try checking the following clubs that might interest you: ")
   print("""
1. Blue Football Team. Could it be Manchester City Football Club?!
2. Scuba Diving Course.
3. Skiing and Snowboarding Club. Every winter, we organise amazing trips to Europe to enjoy our well earned break! Join us and you will not regret it!
""")

elif fav_colour == "Yellow":# user's favourite colour is yellow. Suggestions about possibilities to join some clubs.
   print("I see your favourite colour is YELLOW! ")

   print("""
Come and Join our excellent clubs:

1. Yellow Drama (LAMDA) Club.
2. Dance Club.
3. Orchestra.
4. Volunteering for the Community: a hands on project. Tutoring mathematics, chemistry and physics.
""")
   
else:
   print("I am not sure if you have entered any colour. Please try again.")

   print("Welcome To our FAQ section. Don't by shy - ask: ")# the programme prints the FAQ (frequently asked questions)

question = input("Please enter your question here: ")
print(f"""

1. Where is the library?
2. Library's opening times: 
3. Where is the gym?
4. Gyms opening times:
5. Where is the cafeteria?
6. How do I access WiFi?
7. Where are the washing machines?
8. How do I pay for the washing?
9. How much does it cost to wash a load of clothes?
10. Where is the nearest store?
11. Where is the closest barber and how much does it cost?
12. Term dates.
13. Exam times.

""")
if question == 'Where is the Library?':
  print("The Library is located in Alan Turner Building.")

elif question  == "Library opening times":
  print("24/7")

elif question == 'Where is the gym?':
  print("John Snow Building.")  

elif question == "Gym opening times":
  print("Every day: 7am - 10pm.")

elif question == "Where is the cafeteria?":
  print("Harry Potter Building.")

elif question == 'How do I access WiFi?':
  print(" You will need to use a password. You should have received one in your email. If NOT, please contact the IT Department.")

elif question == "Where are the washing machines?":
  print("In Helvetia House.")

elif question == "How do I pay for the washing?":
  print("Use the website: www.pay_washing.co.uk")

elif question == "How much does it cost to wash a load of clothes?":
  print("£4.20 per load.")

elif question == "Where is the nearest store?":
  print("17 Market Place.")

elif question == "Where is the closest barber and how much does it cost?":
  print("The Keep Barber Shop, 47 Saddler Street. There is a student discount every Wednesday. It costs £10.00 for a customer with a STUDENT ID.")

elif question == "Term dates":
  print("Check the University's website.")

elif question == "Exam times":
  print("Check the University's website.")
else:
   print("Are these all your questions? I am happy to be of any assisstance to you.")
print("Thank you for using the 'Unibuddy' services.")





#fac_file = open("input.txt", "r")
#fac_list = [] # This is a list

'''temp = lines.strip('\n')
temp == temp.split
print([temp])'''

#joined = " ".join(temp)
#print(joined)

#faq_list.append(joined)
#print(faq_list)

print("This is a 'list' of FAQ: ")

for count, quest in enumerate(" Please enter the number of question you would like to ask: "):

   '''index = choice - 1
   #faq_list == questions
   print(faq_list[faq_list])'''

'''if index == 0:
   print("You have just chosen : {faq_list[index]}")
    
   print("It is in Alan Turner Building. ")

elif index == 1:
   print("24/7")

elif index == 2:
   print("John Snow Building.")

elif index == 3:
   print("Every day: 7am - 10pm.")

elif index == 4:
   print("Harry Potter Building.")

elif index == 5:
   print("You will need to use a password. You should have received one in your email. If NOT, please contact the IT Department.")

elif index == 6:
   print("Helvetia House.")

elif index == 7:
   print("Use the website: www.pay_washing.co.uk ")

elif index == 8:
   print("£4.20 per load.")

elif index == 9:
   print("17 Market Place.")

elif index == 10:
   print("The Keep Barber Shop, 47 Saddler Street.")

elif index == 11:
   print("The Student Discount Applies. On Wednesdays: £10.00.")

elif index == 12:
   print("Check the University's website.")

elif index == 13:
   print("Check the University's website.")

else:
   print("You have not asked any questions. Thank you for using our services. Goodbye!")'''