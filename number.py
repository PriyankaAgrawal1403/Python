def forward_number_system(n):
  for i in range(1, n + 1):
      print(' '.join(map(str, range(1, i + 1))))

def backward_number_system(n):
  for i in range(n, 0, -1):
      print(' '.join(map(str, range(1, i + 1))))

def vertical_number_system(n):
  for i in range(1, n + 1):
      print(' '.join(map(str, range(1, i + 1))))
  for i in range(n - 1, 0, -1):
      print(' '.join(map(str, range(1, i + 1))))

def horizontal_number_system(n):
  for i in range(1, n + 1):
      print(' '.join(map(str, range(1, i + 1))), end=' ')
  for i in range(n - 1, 0, -1):
      print(' '.join(map(str, range(1, i + 1))), end=' ')

def main():
  n = int(input("Enter the number of lines: "))
  print("\nForward Number System:")
  forward_number_system(n)

  print("\nBackward Number System:")
  backward_number_system(n)

  print("\nVertical Number System:")
  vertical_number_system(n)

  print("\nHorizontal Number System:")
  horizontal_number_system(n)

if __name__ == "__main__":
  main()