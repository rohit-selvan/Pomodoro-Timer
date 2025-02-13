import tkinter as tk
import time
from tkinter import messagebox

class PomodoroTimer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro Timer")
        self.geometry("600x650")
        self.configure(bg="#ffe4e1")  
        self.reps = 0
        self.timer = None
        self.create_widgets()

    def create_widgets(self):
        
        tk.Label(self, text="Pomodoro Timer", font=("Verdana", 28, "bold"), bg="#ffe4e1", fg="#333").pack(pady=20)
        
        
        self.timer_label = tk.Label(self, text="25:00", font=("Verdana", 48, "bold"), bg="#ffe4e1", fg="#333")
        self.timer_label.pack(pady=20)
        
        
        settings_frame = tk.Frame(self, bg="#ffe4e1")
        settings_frame.pack(pady=10)
        
        tk.Label(settings_frame, text="Work Duration (min):", font=("Verdana", 12), bg="#ffe4e1").grid(row=0, column=0, padx=5)
        self.work_entry = tk.Entry(settings_frame, font=("Verdana", 12), width=5)
        self.work_entry.insert(0, "25")
        self.work_entry.grid(row=0, column=1, padx=5)
        
        tk.Label(settings_frame, text="Break Duration (min):", font=("Verdana", 12), bg="#ffe4e1").grid(row=1, column=0, padx=5)
        self.break_entry = tk.Entry(settings_frame, font=("Verdana", 12), width=5)
        self.break_entry.insert(0, "5")
        self.break_entry.grid(row=1, column=1, padx=5)
        
      
        tk.Label(settings_frame, text="Session Name:", font=("Verdana", 12), bg="#ffe4e1").grid(row=2, column=0, padx=5)
        self.session_name_entry = tk.Entry(settings_frame, font=("Verdana", 12), width=20)
        self.session_name_entry.insert(0, "Study Session")
        self.session_name_entry.grid(row=2, column=1, padx=5)
        
       
        button_frame = tk.Frame(self, bg="#ffe4e1")
        button_frame.pack(pady=20)
        tk.Button(button_frame, text="Start", command=self.start_timer, font=("Verdana", 14), bg="#b5e7a0", fg="white", width=10).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Reset", command=self.reset_timer, font=("Verdana", 14), bg="#f4cccc", fg="white", width=10).grid(row=0, column=1, padx=10)
        
        
        self.sessions_label = tk.Label(self, text="Completed Sessions: 0", font=("Verdana", 14), bg="#ffe4e1", fg="#333")
        self.sessions_label.pack(pady=20)
        
        
        self.encouragement_label = tk.Label(self, text="Let's get started!", font=("Verdana", 14, "italic"), bg="#ffe4e1", fg="#666")
        self.encouragement_label.pack(pady=10)

    def start_timer(self):
        try:
            work_duration = int(self.work_entry.get()) * 60
            break_duration = int(self.break_entry.get()) * 60
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for durations.")
            return
        
        self.reps += 1
        session_name = self.session_name_entry.get().strip() or "Session"
        if self.reps % 8 == 0:
            self.countdown(break_duration * 4)  
            self.timer_label.config(text=f"Long Break", fg="#e53935")
            self.encouragement_label.config(text="Great job! Enjoy a long break! 🌟")
        elif self.reps % 2 == 0:
            self.countdown(break_duration)  
            self.timer_label.config(text=f"Break", fg="#fdd835")
            self.encouragement_label.config(text=f"Well done! Take a short break. ☕")
        else:
            self.countdown(work_duration)  
            self.timer_label.config(text=f"{session_name} (Work)", fg="#43a047")
            self.encouragement_label.config(text="Stay focused! You got this! 💪")

    def reset_timer(self):
        if self.timer:
            self.after_cancel(self.timer)
        self.timer_label.config(text="25:00", fg="#333")
        self.sessions_label.config(text="Completed Sessions: 0")
        self.encouragement_label.config(text="Let's get started!")
        self.reps = 0

    def countdown(self, count):
        minutes = count // 60
        seconds = count % 60
        self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
        if count > 0:
            self.timer = self.after(1000, self.countdown, count - 1)
        else:
            self.start_timer()
            completed_sessions = self.reps // 2
            self.sessions_label.config(text=f"Completed Sessions: {completed_sessions}")

if __name__ == "__main__":
    app = PomodoroTimer()
    app.mainloop()
