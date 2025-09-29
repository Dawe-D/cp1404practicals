
MENU = "Menu \n H: Hello \n G: Goodbye \n Q: Quit"

first_name = str(input("Please enter your first name: "))
surname = str(input("Please enter your surname name: "))

print(MENU)
choice = input("> ").upper()
while choice != "Q":
   if choice == "H":
       print(f"Hello {first_name} {surname}.")
   elif choice == "G":
        print(f"Goodbye {first_name} {surname}.")
   else:
       print("Invalid choice.")
   print(MENU)
   choice = input("> ").upper()
print("Finished.")
