def schedule_appointment():
  AvailEngg = ["Engr. sIUzy", "Engr. sIUzy Saur", "Engr. suzybae", "Engr. iu ", "Engr. 016"]
  AvailTime= ["9:00AM -11:30AM", "1:00PM-3:30PM", "5:00PM-7:30PM"]

  # Ask the user his/her choice 
  print("Please choose an engineer from the following list:")
  for engineer in AvailEngg:
    print(engineer)
  chosen_engineer = input("Enter the name of the engineer you want to schedule an appointment with: ")

  # Check if the chosen engineer exists in the available options
  if chosen_engineer not in AvailEngg:
    print("Invalid engineer. Please choose a valid engineer from the list.")
    return

  print("\nPlease choose a time slot from the following list:")
  for time in AvailTime:
    print(time)
  chosen_time = input("Enter the time slot you want to schedule an appointment for: ")

  # Check if the chosen time exists in the available options
  if chosen_time not in AvailTime:
    print("Invalid time slot. Please choose a valid time slot from the list.")
    return

  # Ask for customer information
  full_name = input("\nPlease enter your full name: ")
  address = input("Please enter your address: ")
  age = input("Please enter your age: ")
  case = input("Please describe the reason for your appointment: ")
  location = input("Please enter the location where you would like to meet the engineer: ")

   # Print out customer information
  print("\nThank you for filling up the needed information.")
  print("\n\nYour appointment is scheduled with", chosen_engineer, "at", chosen_time)
  print("Full Name:", full_name)
  print("Address:", address)
  print("Age:", age)
  print("Case of appointment:", case)
  print("Location of meet up:", location)

# Use a while loop to continuously ask the first question
while True:
  schedule_appointment()

  # Ask the user if they want to schedule another appointment
  answer = input("\nDo you want to schedule another appointment? (yes/no) ")
  if answer.lower() == "no":
    print("Thank you for scheduling an appointment with us. Have a great day!")
    break
