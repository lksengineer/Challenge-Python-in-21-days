def find_famous_cat(cats):
  """Function find found cat"""
  if len(cats) > 0:
    
    # List to add famous cat
    famous_cat_total = []
    # Value for sum the total followers
    total_followers = 0
  
    # Itero every element of the array
    for cat in cats:
      # Value for the sum of followers
      suma_followers = 0
      # Itero every element of the array and the sum in the value suma_followers
      for follow in cat['followers']:
        suma_followers += follow
      if suma_followers > total_followers:
        famous_cat_total.clear()
        total_followers = suma_followers
        famous_cat_total.append(cat['name'])
        # famous_cat_total.append({"names": cat['name'], 'followersss': suma_followers})
      elif suma_followers == total_followers:
        famous_cat_total.append(cat['name'])
        # famous_cat_total.append({"names": cat['name'], 'followersss': total_followers})
    return famous_cat_total
  else:
    # return ("The array has no cats")
    print("The array has no cats")

cats = [
  {
    "name": "Luna",
    "followers": [100, 20, 100]
    },
    {
      "name": "Sol",
      "followers": [500, 1000, 100]
    },
    {
      "name": "Estrella",
      "followers": [500, 1000, 100]
    },
    {
      "name": "Arcoiris",
      "followers": [200, 1000, 100]
    },
    {
      "name": "Alc[on",
      "followers": [500, 1000, 100]
    }
]

# for cat in cats:
#   print(f"Name: {cat['name']}, Followers: {max(cat['followers'])}")
famous_cat = find_famous_cat(cats)
print(famous_cat)