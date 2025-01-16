print('Hello, I am your Robo Friend')
name = input("What is your name friend? ")
age = input("And how old are you " + name + ". ")
print('I am Robo-295, but you can just call me robo')
next_choice();
def next_choice():
  #main portion
  print('')
  print('What else would you like to do \n')
  print('1. Play Game \n')
  print('2. Chat \n')
  print('3. Exit \n')
  choice = input('')
  #seeing what user chose
  if choice == '1':
     game();
  if choice == '2':
    chat();
  else:
     quit

def chat():
  input('How was your day so far');
  print('My day was good, I had a good charge);
  input('How was your sleep?');
  return('this is a place holder chat')
def game();
  return('placeholder')
  
