import random

#data storage
flashTerms = ["placeholder"]
flashDefinitions = ["placeholder"]

#prompt options

while len(flashTerms) > 0:
  
  user_input = input("Would you like to create a [A] flashcard, or begin [B] practicing? ")
  
  if user_input == "A":
    
    inputTerms = input("Please enter the word:")
    flashTerms.append(inputTerms)
    
    inputDefinitions = input("Please enter the meaning:")
    flashDefinitions.append(inputDefinitions)
    
    print("You have successfully created a flashcard")
    
    if flashTerms[0] == "placeholder":
      
      del flashTerms[0]
      del flashDefinitions[0]
    
  elif user_input == "B":
    
    definition = random.choice(flashDefinitions)
    
    answer = input("Enter the word based on the definition, " + definition + ":")
    a = flashDefinitions.index(definition)

    try:
      
      if flashTerms.index(answer) == a and answer in flashTerms:
        print("Correct!")
        del flashTerms[a]
        del flashDefinitions[a]
      elif flashTerms.infex(answer) != a and answer in flashTerms:
        print("Wrong.")
        del flashTerms[a]
        del flashDefinitions[a]

    except:
      print("Wrong.")
      del flashTerms[a]
      del flashDefinitions[a]