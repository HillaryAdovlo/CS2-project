from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow):
    def vote_menu() -> str:
        """
        Displays the vote menu and prompts the user for their choice.

        Returns:
            str: The user's choice ("vote" or "end").
        """
        while True:
            print("\nVote Menu")
            print("1. Vote")
            print("2. End Election")

            choice = input("\nEnter choice (1,2 or 3): ").strip()

            if choice == "1":
                return "vote"
            elif choice == "2":
                return "end"
            else:
                print("Invalid choice. Please try again.")

    def candidate_menu() -> int:
        """
        Displays the candidate menu and prompts the user to select a candidate.

        Returns:
            int: The index of the selected candidate (1 or 2).
        """
        while True:
            print("\nCandidate Menu")
            print("==============")
            print("1. Jane")
            print("2. John")

            try:
                choice = int(input("\nEnter choice (1-2): ").strip())
                if 1 <= choice <= 2:
                    return choice
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def display_results(votes: list[int]) -> None:
        """
        Displays the election results based on the given vote counts.

        Args:
            votes (list[int]): A list containing the number of votes for each candidate.
        """
        candidates = ["Jane", "John"]
        total_votes = sum(votes)

        print("\nElection Results")
        print("================")

        if total_votes == 0:
            print("No votes were cast.")
            return

        for candidate, vote_count in zip(candidates, votes):
            percentage = (vote_count / total_votes) * 100
            print(f"{candidate}: {vote_count} vote(s) ({percentage:.2f}%)")

    def get_unique_id(used_ids: set[str]) -> str:
        """
        Prompts the user to enter a unique 5-digit voter ID, ensuring that
        it has not been used before.

        Args:
            used_ids (set[str]): A set of already used voter IDs.

        Returns:
            str: A valid unique 5-digit voter ID.
        """
        while True:
            voter_id = input("\nEnter your 6-digit voter ID: ").strip()
            if not voter_id.isdigit() or len(voter_id) != 5:
                print("Invalid ID. Please ensure it is a 5-digit number.")
            elif voter_id in used_ids:
                print("This ID has already been used. Please enter a different ID.")
            else:
                return voter_id

    def main_logic() -> None:
        """
        Runs the main logic of the voting system, allowing users to vote
        and displaying results when the election ends.
        """
        votes = [0, 0]
        used_ids = set()

        while True:
            voter_id = get_unique_id(used_ids)
            used_ids.add(voter_id)

            choice = vote_menu()

            if choice == "vote":
                candidate = candidate_menu()
                votes[candidate - 1] += 1
                print("\nVote recorded.")
            else:
                display_results(votes)
                break
