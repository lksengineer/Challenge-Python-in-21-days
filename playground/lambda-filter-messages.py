"""
Function lambda with filter function for filter
messages from a specific user
"""

def filter_user_messages(messages, user):
  """Function to filter messages by user"""
  filtered_messages = list(filter(lambda message: message["sender"] == user, messages))
  return filtered_messages


if __name__ == '__main__':
  """Start Function"""
  
  messages = [
    {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
    {'sender': 'Bob', 'content': '¡Bien, gracias!'},
    {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
    {'sender': 'Charlie', 'content': 'Hola a todos.'},
    {'sender': 'Alice', 'content': 'Nos vemos luego.'}
  ]
  
  user = 'Alice'
  
  print(filter_user_messages(messages, user))