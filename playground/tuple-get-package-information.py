def get_packages_info(packages):
  """Function Get Packages Information"""
  
  total_weight = 0
  registration_pack = {
    "total_weight": 0,
    "destinations": {},
  }
  
  for pack in packages:
    total_weight += pack[1]

    # destination = pack[2]
    if pack[2] not in registration_pack["destinations"]:
      registration_pack["destinations"][pack[2]] = 1
    else:
      registration_pack["destinations"][pack[2]] += 1

  total_weight = round(total_weight, 2)
  
  registration_pack["total_weight"] = total_weight
  
  return registration_pack



if __name__ == '__main__':
  # (id, weight, destination)
  packages = [
    (1, 20, "Mexico"),
    (2, 15.5, "Colombia"),
    (3, 30, "Mexico"),
    (4, 12, "Argentina"),
    (5, 8.2, "Colombia"),
    (6, 25, "Mexico"),
    (7, 18.7, "Argentina"),
    (8, 5, "Colombia"),
    (9, 22.3, "Argentina"),
    (10, 14.8, "Colombia")
  ]
  
  response = get_packages_info(packages)
  print(response)
