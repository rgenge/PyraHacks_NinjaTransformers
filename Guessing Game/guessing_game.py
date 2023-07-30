import random

def guessing_game():
  print("Welcome to the Guessing Game!\n")
  print("Here are the difficulty levels: \n")
  print("1.Easy\n")
  print("2.Medium\n")
  print("3.Hard\n")
  difficulty_level = int(input("Select which difficulty level you would like to play by entering the corresponding number: "
      ))

  # Generate the game for easy mode
  if difficulty_level == 1:
    print(
        "\n I have chosen a number between 1 and 50. You have 15 chances to guess the number.\n"
    )

    # Generates a number that is between 1 and 50
    secret_number1 = random.randint(1, 50)

    # Set the number of attempts allowed
    max_attempts1 = 15
    attempts1 = 0

    while attempts1 < max_attempts1:
      try:
        guess1 = int(input("Enter your guess: "))
      except ValueError:
        print("\nInvalid input. Please enter a valid number. \n")
        continue

      attempts1 += 1

      if guess1 < secret_number1 and guess1 < 50 and guess1 > 1:
        print("\nToo low. Try again. \n")
      elif guess1 > secret_number1 and guess1 < 50 and guess1 > 1:
        print("\nToo high. Try again. \n")
      elif guess1 > 50 or guess1 < 1:
        print("\nPlease enter a number that is equal or greater than one and equal or less than 50. \n")
      else:
        print("\nCongratulations! You guessed the correct number."
        )
        break

    if attempts1 == max_attempts1:
      print(
          "\nSorry, you've reached the maximum number of attempts. The secret number was" + secret_number1 )

  # Generate the game for medium mode
  elif difficulty_level == 2:
    print(
        "\nI have chosen a number between 1 and 100. You have 10 chances to guess the number. \n"
    )

    # Generates a number that is between 1 and 100
    secret_number2 = random.randint(1, 100)

    # Set the number of attempts allowed
    max_attempts2 = 10
    attempts2 = 0

    while attempts2 < max_attempts2:
      try:
        guess2 = int(input("Enter your guess: "))
      except ValueError:
        print("\nInvalid input. Please enter a valid number.\n")
        continue

      attempts2 += 1

      if guess2 < secret_number2 and guess2 < 100 and guess2 > 1:
        print("\nToo low. Try again. \n")
      elif guess2 > secret_number2 and guess2 < 100 and guess2 > 1:
        print("\nToo high. Try again. \n")
      elif guess2 > 100 or guess2 < 1:
        print("\nPlease enter a number that is equal or greater than 1 and equal or less than 100. \n")
      else:
        print(
            "\nCongratulations! You guessed the correct number."
        )
        break

    if attempts2 == max_attempts2:
      print(
          "\nSorry, you've reached the maximum number of attempts. The secret number was {secret_number2}. "
      )

  #generate the game for the hard mode
  elif difficulty_level == 3:
    print(
        "\nI have chosen a number between 1 and 150. You have 5 chances to guess the number. \n"
    )

    # Generates a number that is between 1 and 150
    secret_number3 = random.randint(1, 150)

    # Set the number of attempts allowed
    max_attempts3 = 5
    attempts3 = 0

    while attempts3 < max_attempts3:
      try:
        guess3 = int(input("Enter your guess: "))
      except ValueError:
        print("\nInvalid input. Please enter a valid number. \n")
        continue

      attempts3 += 1

      if guess3 < secret_number3 and guess3 < 150 and guess3 > 1:
        print("\nToo low. Try again. \n")
      elif guess3 > secret_number3 and guess3 < 150 and guess3 > 1:
        print("\nToo high. Try again. \n")
      elif guess3 > 150 or guess3 < 1:
        print("\nPlease enter a number that is equal or greater than 1 and equal or less than 150. \n")
      else:
        print(
            "\nCongratulations! You guessed the correct number."
        )
        break

    if attempts3 == max_attempts3:
      print(
          "\nSorry, you've reached the maximum number of attempts. The secret number was {secret_number3}."
      )

  else:
    print("\ninvalid input. Please enter a valid number")


if __name__ == "__main__":
  guessing_game()