#!/usr/bin/env python3
# Thomas Sellars Netacea Technical Task.

def main():
  #Loops from 1 to 100, range(Start, End) isn't inclusive of its end point.
  for i in range(1, 101):
    if i % 3 == 0  and i % 5 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)

if __name__ == "__main__":
  main()