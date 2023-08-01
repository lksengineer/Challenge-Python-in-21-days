def get_student_average(students):
  """Function Get Student Average"""
  
  # Inicio variable para el promedio del salón
  average_general = 0

  # Inicio dictionario a retornar
  average_list = {
      "class_average": 0,
      "students": [],
  }

  # Bucle to iterar the listy and get the dict to iterar 
  for item in students:
    average = 0

    # Bucle for Iterar el dict and get the student average
    for value in item["grades"]:
      average += value

    # Calcule the student average
    average_student = average / len(item["grades"])
    average_student = round(average_student, 2)

    # Add to dict the student and average round with .00
    average_list["students"].append({
        "name": item["name"],
        "average": average_student
    })
    # average_list["students"] = {"name": item["name"], "average": average_student}

    # Calcule the general average
    average_general += average_student

  average_general = average_general / len(students)
  average_general = round(average_general, 2)

  # Add to dict the general average
  average_list["class_average"] = average_general

  # Return the dict with the general and student average
  return average_list


students = [
    {
        'name': 'Pedro',
        'grades': [90, 87, 88, 90],
    },
    {
        "name": "Jose",
        "grades": [99, 71, 88, 96],
    },
    {
        "name": "Maria",
        "grades": [92, 81, 80, 96],
    },
]

student_average = get_student_average(students)
print(student_average)