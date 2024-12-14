import tkinter as tk
from tkinter import messagebox

class VotingAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voting Application")

        self.votes = [0, 0]
        self.used_ids = set()

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=20, padx=20)

        self.create_voter_id_frame()

    def create_voter_id_frame(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Enter your 5-digit voter ID:").pack(pady=5)
        self.voter_id_entry = tk.Entry(self.main_frame)
        self.voter_id_entry.pack(pady=5)

        submit_button = tk.Button(
            self.main_frame, text="Submit", command=self.check_voter_id
        )
        submit_button.pack(pady=10)

    def check_voter_id(self):
        voter_id = self.voter_id_entry.get().strip()

        if not voter_id.isdigit() or len(voter_id) != 5:
            messagebox.showerror("Invalid ID", "Please enter a valid 5-digit ID.")
        elif voter_id in self.used_ids:
            messagebox.showerror("Duplicate ID", "This ID has already been used.")
        else:
            self.used_ids.add(voter_id)
            self.show_vote_menu()

    def show_vote_menu(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Vote Menu").pack(pady=5)

        vote_button = tk.Button(
            self.main_frame, text="Vote", command=self.show_candidate_menu
        )
        vote_button.pack(pady=5)

        end_button = tk.Button(
            self.main_frame, text="End Election", command=self.display_results
        )
        end_button.pack(pady=5)

    def show_candidate_menu(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Candidate Menu").pack(pady=5)
        tk.Label(self.main_frame, text="1. Jane").pack()
        tk.Label(self.main_frame, text="2. John").pack()

        self.candidate_choice = tk.IntVar()

        jane_button = tk.Radiobutton(
            self.main_frame, text="Jane", variable=self.candidate_choice, value=1
        )
        jane_button.pack(anchor="w")

        john_button = tk.Radiobutton(
            self.main_frame, text="John", variable=self.candidate_choice, value=2
        )
        john_button.pack(anchor="w")

        vote_button = tk.Button(
            self.main_frame, text="Submit Vote", command=self.record_vote
        )
        vote_button.pack(pady=10)

    def record_vote(self):
        choice = self.candidate_choice.get()

        if choice == 0:
            messagebox.showerror("No Selection", "Please select a candidate.")
        else:
            self.votes[choice - 1] += 1
            messagebox.showinfo("Vote Recorded", "Your vote has been recorded.")
            self.show_vote_menu()

    def display_results(self):
        self.clear_frame()

        candidates = ["Jane", "John"]
        total_votes = sum(self.votes)

        tk.Label(self.main_frame, text="Election Results").pack(pady=5)

        if total_votes == 0:
            tk.Label(self.main_frame, text="No votes were cast.").pack()
            return

        for candidate, vote_count in zip(candidates, self.votes):
            percentage = (vote_count / total_votes) * 100
            result_text = f"{candidate}: {vote_count} vote(s) ({percentage:.2f}%)"
            tk.Label(self.main_frame, text=result_text).pack()

        close_button = tk.Button(
            self.main_frame, text="Close", command=self.root.quit
        )
        close_button.pack(pady=10)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    app = VotingAppGUI(root)
    root.mainloop()
