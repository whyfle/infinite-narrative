import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import sys, os, threading, time
from datetime import datetime
from dates import DatingSimulator
from characters import CharacterGenerator

class DatingSimulatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Infinite Dating Simulator - GUI v3.0")
        self.root.geometry("1400x900")
        self.root.configure(bg="#1a1a2e")
        self.dating = DatingSimulator()
        self.dating.generate_player("Player")
        self.char_gen = CharacterGenerator()
        self.running = False
        self.tokens = 0
        self.create_widgets()
        self.apply_theme()

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use("clam")

        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Control Panel
        self.control_frame = ttk.LabelFrame(self.main_frame, text="Game Controls", padding="10")
        self.control_frame.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(self.control_frame, text="Player Name:").grid(row=0, column=0, padx=5)
        self.player_name = tk.StringVar(value="Player")
        ttk.Entry(self.control_frame, textvariable=self.player_name, width=15).grid(row=0, column=1, padx=5)

        ttk.Label(self.control_frame, text="Wealth:").grid(row=0, column=2, padx=5)
        self.wealth_var = tk.IntVar(value=100)
        ttk.Entry(self.control_frame, textvariable=self.wealth_var, width=8).grid(row=0, column=3, padx=5)

        ttk.Label(self.control_frame, text="Target Tokens:").grid(row=0, column=4, padx=5)
        self.token_target = tk.StringVar(value="999999")
        ttk.Entry(self.control_frame, textvariable=self.token_target, width=12).grid(row=0, column=5, padx=5)

        self.start_btn = ttk.Button(self.control_frame, text="Start Dating", command=self.start_game)
        self.start_btn.grid(row=0, column=6, padx=10)

        self.date_btn = ttk.Button(self.control_frame, text="Go on a Date", command=self.go_date)
        self.date_btn.grid(row=0, column=7, padx=5)
        self.date_btn.configure(state=tk.DISABLED)

        self.gift_btn = ttk.Button(self.control_frame, text="Give Gift", command=self.give_gift)
        self.gift_btn.grid(row=0, column=8, padx=5)
        self.gift_btn.configure(state=tk.DISABLED)

        self.confess_btn = ttk.Button(self.control_frame, text="Confess Love", command=self.confess)
        self.confess_btn.grid(row=0, column=9, padx=5)
        self.confess_btn.configure(state=tk.DISABLED)

        self.stop_btn = ttk.Button(self.control_frame, text="Stop", command=self.stop_game)
        self.stop_btn.grid(row=0, column=10, padx=5)
        self.stop_btn.configure(state=tk.DISABLED)

        self.clear_btn = ttk.Button(self.control_frame, text="Clear", command=self.clear_output)
        self.clear_btn.grid(row=0, column=11, padx=5)

        self.export_btn = ttk.Button(self.control_frame, text="Export Save", command=self.export_save)
        self.export_btn.grid(row=0, column=12, padx=5)

        # Stats Bar
        self.stats_frame = ttk.LabelFrame(self.main_frame, text="Player Stats", padding="5")
        self.stats_frame.pack(fill=tk.X, pady=(0, 10))

        self.stats_text = tk.StringVar(value="Wealth: 100 | Charm: 50 | Dates: 0 | Affection: 0 | Day: 1")
        ttk.Label(self.stats_frame, textvariable=self.stats_text).pack(side=tk.LEFT, padx=10)

        self.progress = ttk.Progressbar(self.stats_frame, mode="determinate", length=400)
        self.progress.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)

        self.speed_var = tk.StringVar(value="Speed: 0 tokens/sec")
        ttk.Label(self.stats_frame, textvariable=self.speed_var).pack(side=tk.RIGHT, padx=10)

        # Partner List
        self.partner_frame = ttk.LabelFrame(self.main_frame, text="Love Interests", padding="5")
        self.partner_frame.pack(fill=tk.X, pady=(0, 10))

        self.partner_listbox = tk.Listbox(self.partner_frame, height=4, bg="#0d0d1a", fg="#00ff41",
            font=("Consolas", 9), selectbackground="#0f3460")
        self.partner_listbox.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        self.partner_scroll = ttk.Scrollbar(self.partner_frame, orient=tk.VERTICAL, command=self.partner_listbox.yview)
        self.partner_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.partner_listbox.configure(yscrollcommand=self.partner_scroll.set)

        # Output
        self.output_frame = ttk.LabelFrame(self.main_frame, text="Narrative Output", padding="5")
        self.output_frame.pack(fill=tk.BOTH, expand=True)

        self.output_text = scrolledtext.ScrolledText(self.output_frame, wrap=tk.WORD, height=20,
            bg="#0d0d1a", fg="#00ff41", insertbackground="#00ff41", font=("Consolas", 9),
            state=tk.DISABLED)
        self.output_text.pack(fill=tk.BOTH, expand=True)

        # Status Bar
        self.status_var = tk.StringVar(value="Ready. Click Start Dating to begin.")
        self.status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def apply_theme(self):
        self.root.configure(bg="#1a1a2e")
        style = ttk.Style()
        style.configure("TFrame", background="#1a1a2e")
        style.configure("TLabelframe", background="#1a1a2e", foreground="#00ff41")
        style.configure("TLabelframe.Label", background="#1a1a2e", foreground="#00ff41", font=("Consolas", 10, "bold"))
        style.configure("TButton", background="#16213e", foreground="#00ff41", font=("Consolas", 9))
        style.map("TButton", background=[("active", "#0f3460")])
        style.configure("TLabel", background="#1a1a2e", foreground="#e0e0e0")
        style.configure("TProgressbar", background="#00ff41", troughcolor="#16213e")

    def log(self, text):
        self.output_text.configure(state=tk.NORMAL)
        self.output_text.insert(tk.END, text + "\n")
        self.output_text.see(tk.END)
        self.output_text.configure(state=tk.DISABLED)
        self.tokens += len(text.split())

    def start_game(self):
        self.dating = DatingSimulator()
        name = self.player_name.get()
        self.dating.generate_player(name)
        self.running = True
        self.start_btn.configure(state=tk.DISABLED)
        self.date_btn.configure(state=tk.NORMAL)
        self.gift_btn.configure(state=tk.NORMAL)
        self.confess_btn.configure(state=tk.NORMAL)
        self.stop_btn.configure(state=tk.NORMAL)
        self.status_var.set(f"Game started! Player: {name}. Go on a date!")
        self.update_partner_list()
        self.start_time = time.time()

    def go_date(self):
        if not self.dating.player_relationship:
            self.dating.generate_partner(0)
        partner = random.choice(list(self.dating.player_relationship.keys())) if self.dating.player_relationship else "Stranger"
        if partner == "Stranger":
            partner = self.dating.generate_partner(0)["name"]
        location = random.choice(self.dating.locations)
        date_info, affection = self.dating.generate_date(
            self.dating.player_relationship.get(partner, self.dating.generate_partner(0)),
            self.dating.locations.index(location))
        dialogue = self.dating.generate_date_dialogue(self.dating.generate_partner(0))
        self.log(f"\n--- DATE with {partner} at {location['name']} ---")
        self.log(f"Activity: {location['activity']} | Cost: {location['cost']} gold")
        self.log(f"Affection: +{affection}")
        for d in dialogue:
            self.log(f"  {d}")
        self.update_stats()
        self.update_partner_list()

    def give_gift(self):
        partner = random.choice(list(self.dating.player_relationship.keys())) if self.dating.player_relationship else None
        if not partner:
            self.log("No partners yet! Go on a date first.")
            return
        gift = random.choice(self.dating.gifts)
        result = self.dating.generate_gift_interaction(self.dating.generate_partner(0))
        self.log(f"\n--- GIFT to {partner} ---")
        self.log(f"Gift: {gift['name']} ({gift['description']})")
        self.log(f"Affection: +{gift['affection_bonus']}")
        self.log(f"Reaction: {gift['reaction']}")
        self.update_stats()

    def confess(self):
        partner = random.choice(list(self.dating.player_relationship.keys())) if self.dating.player_relationship else None
        if not partner:
            self.log("No partners yet!")
            return
        result = self.dating.generate_confession(self.dating.generate_partner(0))
        self.log(f"\n--- CONFESSION to {partner} ---")
        self.log(f"Success: {result['success']}")
        self.log(f"Message: {result['message']}")
        self.log(f"Status: {result['status']}")
        self.update_stats()

    def stop_game(self):
        self.running = False
        self.status_var.set("Game stopped.")
        self.start_btn.configure(state=tk.NORMAL)
        self.date_btn.configure(state=tk.DISABLED)
        self.gift_btn.configure(state=tk.DISABLED)
        self.confess_btn.configure(state=tk.DISABLED)
        self.stop_btn.configure(state=tk.DISABLED)

    def update_stats(self):
        if not self.dating.player_relationship:
            return
        total_affection = sum(r["affection"] for r in self.dating.player_relationship.values())
        total_dates = sum(r["dates"] for r in self.dating.player_relationship.values())
        self.stats_text.set(f"Wealth: {self.dating.player_wealth} | Dates: {total_dates} | Affection: {total_affection} | Day: {self.dating.day}")
        target = int(self.token_target.get())
        self.progress["value"] = min((self.tokens / target) * 100, 100)
        if self.start_time and time.time() - self.start_time > 0:
            speed = self.tokens / (time.time() - self.start_time)
            self.speed_var.set(f"Speed: {speed:,.0f} tokens/sec | Total: {self.tokens:,}")

    def update_partner_list(self):
        self.partner_listbox.delete(0, tk.END)
        for name in self.dating.player_relationship.keys():
            r = self.dating.player_relationship[name]
            self.partner_listbox.insert(tk.END, f"{name} ({r['status']}, Affection: {r['affection']})")

    def clear_output(self):
        self.output_text.configure(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.configure(state=tk.DISABLED)
        self.tokens = 0
        self.progress["value"] = 0

    def export_save(self):
        path = filedialog.asksaveasfilename(defaultextension=".json",
            filetypes=[("JSON", "*.json"), ("All files", "*.*")])
        if path:
            save_data = self.dating.save_game()
            import json
            with open(path, "w") as f:
                json.dump(save_data, f, indent=2)
            messagebox.showinfo("Export", f"Save exported to {path}")

def main():
    root = tk.Tk()
    app = DatingSimulatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
