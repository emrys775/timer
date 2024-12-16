import tkinter as tk
import time



class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")

        self.time_left = 0
        self.is_paused = False
        self.is_running = False

        self.label = tk.Label(master, text="00:00:00", font=("Helvetica", 144), fg="white", bg="black")
        self.label.pack(expand=True, fill=tk.BOTH)

        # Align the buttons horizontally
        button_frame = tk.Frame(master)
        button_frame.pack(side=tk.BOTTOM)

        self.start_button = tk.Button(button_frame, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(button_frame, text="Pause", command=self.pause_timer)
        self.pause_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT)

        reg = master.register(self.validate_input)
        self.entry = tk.Entry(master, justify='center', validate='key', validatecommand=(reg, '%S'))
        self.entry.pack()
        self.entry.insert(0, "Enter time in seconds")

    def validate_input(self, char):
        return char.isdigit()

    def start_timer(self):
        if not self.is_running:
            self.time_left = int(self.entry.get())
            self.is_running = True
            self.countdown()

    def countdown(self):
        if self.time_left > 0 and not self.is_paused:
            mins, secs = divmod(self.time_left, 60)
            hours, mins = divmod(mins, 60)
            self.label.config(text=f"{hours:02}:{mins:02}:{secs:02}")
            self.time_left -= 1
            self.master.after(1000, self.countdown)
        elif self.time_left == 0:
            self.timer_finished()

    def pause_timer(self):
        self.is_paused = not self.is_paused

    def stop_timer(self):
        self.is_running = False
        self.time_left = 0
        self.label.config(text="00:00:00")

    def timer_finished(self):
        self.is_running = False
        while True:
            self.label.config(bg="red", fg="black")
            self.master.update()
            time.sleep(1)
            if self.master.focus_get() is None:
                break
            self.label.config(bg="white", fg="black")
            self.master.update()
            time.sleep(1)
            if self.master.focus_get() is None:
                break

if __name__ == "__main__":
    root = tk.Tk()
    timer_app = CountdownTimer(root)
    root.mainloop()