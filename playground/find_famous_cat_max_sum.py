def find_famous_cat(cats):
  """Function find famous cat"""
  # Suma max the followers of a cats 
  followers_max = max([sum(follow['followers']) for follow in cats])

  # followers_max2 = max(sum(follow['followers']) for follow in cats)
  # Cat famous tha has followers == followers_max
  famous_cat = [cat['name'] for cat in cats if followers_max == sum(cat['followers'])]
  return famous_cat


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

famous_cat = find_famous_cat(cats)
print(famous_cat)
