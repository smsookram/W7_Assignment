#Codeforces 4A Solution
import sys

def can_split_watermelon(w: int) -> bool:
  """
  Determine if a watermelon weight (w) can be split into two positive even parts
  """

#check if w is even
  is_even = (w % 2 == 0)

#check that the weight is greater than 2 so the answer is positive
  greater_than_two = (w > 2)

#both things need to be true
  return is_even and greater_than_two

def main():
  #read raw input
  raw = sys.stdin.readline()

  if raw is None:
    #if there is no input, let user know and exit with error code
    print("Error: No input received.", file=sys.stderr)
    sys.exit(1)
    
  raw = raw.strip()

  if raw == "":
    #Empty line
    print("Error: Empty input. Please provide valid integer weight (1-100).", file=sys.stderr)
    sys.exit(1)

  #try to parse integer and handle bad input
  try:
    w= int(raw)
  except ValueError:
    #if parsing fails print error and exit non-zero
    print(f"Error: Invalid weight input: {repr(raw)}", file=sys.stderr)
    sys.exit(1)

  #validate input range
  if not (1 <= w <= 100):
    print(f"Error: Input allowed range (1 <= w <=100). Got: {w}", file=sys.stderr)
    sys.exit(1)

  #compute the result
  result = can_split_watermelon(w)

  #print answer
  print("YES" if result else "NO")

if __name__ == "__main__":
    main()
  

