from art import logo5,logo6
from datagame import data
import random

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
    
# print(logo6)
# print(f'Number of hits: {acertos}')
# print(f"Personality {escolha1}")
# print(logo5)
# print(f"Has more followers on Instagram than : {escolha2}")