#Report File
def generate_report(text):
  word_count = {}
  words = text.split()

  for word in words:
      if word in word_count:
          word_count[word] += 1
      else:
          word_count[word] = 1

  print("Word\t\tCount")
  print("-------------------")
  for word, count in word_count.items():
      print(f"{word.ljust(15)}{count}")

def main():
  text = input("Enter the text for generating the report: ")
  generate_report(text)

if __name__ == "__main__":
  main()
