"""
Function to calculate the tip.
The function takes two parameters: bill_amount and tip_porcentage.
Calculate and return the total tip. 
"""


def calculate_tip(bill_amount, tipPercentage):
  """Function calculate tip."""
  tip = bill_amount * (tipPercentage / 100)
  return round(tip, 2)


if __name__ == '__main__':
  """Function start"""
  bill_amount = 1524.3355
  tipPercentage = 25

  tip = calculate_tip(bill_amount, tipPercentage)
  print(f"Tip: {tip}")
