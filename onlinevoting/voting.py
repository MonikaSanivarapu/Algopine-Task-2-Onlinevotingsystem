class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

class VotingSystem:
    def __init__(self):
        self.candidates = []
        self.voters = set()

    def add_candidate(self, name):
        candidate = Candidate(name)
        self.candidates.append(candidate)

    def display_candidates(self):
        for i, candidate in enumerate(self.candidates, 1):
            print(f"{i}. {candidate.name}")

    def vote(self, voter_id, candidate_index):
        if voter_id in self.voters:
            print("You have already voted.")
            return

        if 1 <= candidate_index <= len(self.candidates):
            candidate = self.candidates[candidate_index - 1]
            candidate.votes += 1
            self.voters.add(voter_id)
            print(f"Vote for {candidate.name} recorded successfully.")
        else:
            print("Invalid candidate index.")

    def display_results(self):
        print("\nElection Results:")
        for candidate in self.candidates:
            print(f"{candidate.name}: {candidate.votes} votes")

def main():
    voting_system = VotingSystem()

    voting_system.add_candidate("Candidate A")
    voting_system.add_candidate("Candidate B")
    voting_system.add_candidate("Candidate C")

    while True:
        print("\n1. Display Candidates")
        print("2. Vote")
        print("3. Display Results")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            voting_system.display_candidates()
        elif choice == "2":
            voter_id = input("Enter your voter ID: ")
            candidate_index = int(input("Enter the index of the candidate you want to vote for: "))
            voting_system.vote(voter_id, candidate_index)
        elif choice == "3":
            voting_system.display_results()
        elif choice == "4":
            print("Exiting the voting system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
