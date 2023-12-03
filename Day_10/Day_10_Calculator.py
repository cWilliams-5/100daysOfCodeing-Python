#Calculator app
from art import logo
def calculator():
  alpha = float(input("Enter the first number:\n"))
  print("+\n-\n*\n/")
  operator = input("Enter the operator:\n")
  beta = float(input("Enter the second number:\n"))
  if operator == "+":
    return (alpha + beta)
  elif operator == "-":
    return (alpha - beta)
  elif operator == "*":
    return (alpha * beta)
  elif operator == "/":
    return (alpha / beta)
  else:
    print("Invalid Operator")

def main():
    print(logo)
    print("Welcome to the Calculator App")
    answer = calculator()
    print(answer)

if __name__ == "__main__":
    main()