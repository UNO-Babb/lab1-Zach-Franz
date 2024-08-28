#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("enter a noun: ")
  name = input("enter a name: ")
  verb1 = input("enter a verb: ")
  noun2 = input("enter a noun: ")
  verb2 = input("enter a verb: ")
  noun3 = input("enter a noun: ")
  #Print the story with the user supplied words.
  print("There once was a " + noun1 + "named" + name + "who went for a " + verb1 + "and met a very large" + noun2 +"and they went to play" + verb2 + "then a" + noun3 + "pulled up and the friends went home right after.") 

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
