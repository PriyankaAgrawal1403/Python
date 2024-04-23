class VotingSystem:
    
  def __init__(self):
      self.candidates = {}

  def add_candidate(self, candidate_name):
      if candidate_name not in self.candidates:
          self.candidates[candidate_name] = 0
          print(f"{candidate_name} has been added as a candidate.")
      else:
          print(f"{candidate_name} is already a candidate.")

  def vote(self, candidate_name):
      if candidate_name in self.candidates:
          self.candidates[candidate_name] += 1
          print(f"Thank you for voting for {candidate_name}.")
      else:
          print(f"{candidate_name} is not a valid candidate.")

  def display_results(self):
      print("Voting Results:")
      for candidate, votes in self.candidates.items():
          print(f"{candidate}: {votes} votes")

def main():
  voting_system = VotingSystem()

  while True:
      print("\n1. Add Candidate")
      print("2. Vote")
      print("3. Display Results")
      print("4. Exit")

      choice = input("Enter your choice: ")

      if choice == '1':
          candidate_name = input("Enter the name of the candidate: ")
          voting_system.add_candidate(candidate_name)
      elif choice == '2':
          candidate_name = input("Enter the name of the candidate you want to vote for: ")
          voting_system.vote(candidate_name)
      elif choice == '3':
          voting_system.display_results()
      elif choice == '4':
          print("Exiting...")
          break
      else:
          print("Invalid choice. Please choose again.")

if __name__ == "__main__":
  main()
