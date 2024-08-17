import random

print('Juego Piedra Papel o Tijera')

def choose_options():
  user_option = input('piedra, papel o tijera => ').lower()
  options = ('piedra','papel','tijera') # Tuple
  if not user_option in options:
    print('Esa Opcion no es valida')
    # continue
    return None, None
  
  computer_option =   random.choice(options)
  
  print('User Option =>',user_option)
  print('Computer Option =>',computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gano!')
      user_wins += 1
    else:
      print('papel gana a piedra')
      print('computer gano!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gano!')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computer gano!')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':  
      print('tijera gana a papel')
      print('user gano!')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computer gano!')
      computer_wins += 1
      
  return user_wins, computer_wins


def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1
  while True:
    print('*'*10)
    print('Round', rounds)
    print('*'*10)
  
    print('computer wins',computer_wins)
    print('user wins',user_wins)
  
    user_option, computer_option = choose_options()
    
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    
    if computer_wins == 2:
      print('El ganador es la computadora')
      break
  
    if user_wins == 2:
      print('El ganador es el usuario')
      break
  
    rounds += 1

run_game()