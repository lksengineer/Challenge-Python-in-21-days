def calculateScore(score):
  print(f"Score: {score}")
  if score < 0 or score > 100:
    print("The score must be between '0 and 100'")
  elif score >= 90:
    print("Obtuviste una A")
  elif score >= 80:
    print("Obtuviste una B")
  elif score >= 70:
    print("Obtuviste una C")
  else:
    print("Obtuviste una calificación insuficiente")
    

if __name__ == "__main__":
  print("\n******Example 1: Calculate score******")
  score = 89
  calculateScore(score)
