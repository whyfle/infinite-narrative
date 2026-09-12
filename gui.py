import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import sys, os, threading, time
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from main import InfiniteNarrativeEngine

class NarrativeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Infinite Narrative Engine - GUI")
        self.root.geometry("1200x800")
        self.root.configure(bg="#1a1a2e")
        self.engine = None
        self.running = False
        self.create_widgets()
        self.apply_theme()

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use("clam")

        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.control_frame = ttk.LabelFrame(self.main_frame, text="Controls", padding="10")
        self.control_frame.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(self.control_frame, text="Token Target:").grid(row=0, column=0, padx=5)
        self.token_target = tk.StringVar(value="999999")
        ttk.Entry(self.control_frame, textvariable=self.token_target, width=15).grid(row=0, column=1, padx=5)

        ttk.Label(self.control_frame, text="Threads:").grid(row=0, column=2, padx=5)
        self.threads_var = tk.IntVar(value=1)
        ttk.Spinbox(self.control_frame, from_=1, to=4, textvariable=self.threads_var, width=5).grid(row=0, column=3, padx=5)

        self.start_btn = ttk.Button(self.control_frame, text="Start Engine", command=self.start_engine)
        self.start_btn.grid(row=0, column=4, padx=10)

        self.pause_btn = ttk.Button(self.control_frame, text="Pause", command=self.toggle_pause, state=tk.DISABLED)
        self.pause_btn.grid(row=0, column=5, padx=5)

        self.stop_btn = ttk.Button(self.control_frame, text="Stop", command=self.stop_engine, state=tk.DISABLED)
        self.stop_btn.grid(row=0, column=6, padx=5)

        self.clear_btn = ttk.Button(self.control_frame, text="Clear Output", command=self.clear_output)
        self.clear_btn.grid(row=0, column=7, padx=5)

        self.export_btn = ttk.Button(self.control_frame, text="Export", command=self.export_output)
        self.export_btn.grid(row=0, column=8, padx=5)

        self.progress_frame = ttk.LabelFrame(self.main_frame, text="Progress", padding="5")
        self.progress_frame.pack(fill=tk.X, pady=(0, 10))

        self.token_label = ttk.Label(self.progress_frame, text="Tokens: 0 / 999,999")
        self.token_label.pack(side=tk.LEFT, padx=10)

        self.progress = ttk.Progressbar(self.progress_frame, mode="determinate", length=600)
        self.progress.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)

        self.speed_label = ttk.Label(self.progress_frame, text="Speed: 0 tokens/sec")
        self.speed_label.pack(side=tk.RIGHT, padx=10)

        self.log_frame = ttk.LabelFrame(self.main_frame, text="Output Log", padding="5")
        self.log_frame.pack(fill=tk.BOTH, expand=True)

        self.log_text = scrolledtext.ScrolledText(self.log_frame, wrap=tk.WORD, height=20,
            bg="#0d0d1a", fg="#00ff41", insertbackground="#00ff41", font=("Consolas", 9),
            state=tk.DISABLED)
        self.log_text.pack(fill=tk.BOTH, expand=True)

        self.status_bar = ttk.Label(self.root, text="Ready", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.original_print = print
        self.print_callbacks = []

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

    def print(self, *args, **kwargs):
        text = " ".join(str(a) for a in args)
        self.log_text.configure(state=tk.NORMAL)
        self.log_text.insert(tk.END, text + "\n")
        self.log_text.see(tk.END)
        self.log_text.configure(state=tk.DISABLED)
        self.original_print(*args, **kwargs)

    def start_engine(self):
        target = int(self.token_target.get())
        self.engine = InfiniteNarrativeEngine(max_tokens_target=target)
        self.engine.emit = lambda text: self.root.after(0, self.log_output, text)
        self.running = True
        self.start_btn.configure(state=tk.DISABLED)
        self.pause_btn.configure(state=tk.NORMAL)
        self.stop_btn.configure(state=tk.NORMAL)
        self.status_bar.configure(text="Running...")
        self.thread = threading.Thread(target=self.run_engine, daemon=True)
        self.thread.start()
        self.start_time = time.time()

    def run_engine(self):
        try:
            tokens = self.engine.run()
            self.root.after(0, lambda: self.status_bar.configure(text=f"Complete! {tokens:,} tokens consumed"))
            self.root.after(0, lambda: self.start_btn.configure(state=tk.NORMAL))
            self.root.after(0, lambda: self.pause_btn.configure(state=tk.DISABLED))
            self.root.after(0, lambda: self.stop_btn.configure(state=tk.DISABLED))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", str(e)))
            self.root.after(0, lambda: self.status_bar.configure(text="Error"))
            self.root.after(0, lambda: self.start_btn.configure(state=tk.NORMAL))
            self.root.after(0, lambda: self.pause_btn.configure(state=tk.DISABLED))
            self.root.after(0, lambda: self.stop_btn.configure(state=tk.DISABLED))

    def toggle_pause(self):
        pass

    def stop_engine(self):
        self.running = False
        self.status_bar.configure(text="Stopped")
        self.start_btn.configure(state=tk.NORMAL)
        self.pause_btn.configure(state=tk.DISABLED)
        self.stop_btn.configure(state=tk.DISABLED)

    def clear_output(self):
        self.log_text.configure(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.log_text.configure(state=tk.DISABLED)

    def log_output(self, text):
        self.log_text.configure(state=tk.NORMAL)
        self.log_text.insert(tk.END, text + "\n")
        self.log_text.see(tk.END)
        self.log_text.configure(state=tk.DISABLED)
        current = self.engine.tokens_consumed if self.engine else 0
        target = int(self.token_target.get())
        self.progress["value"] = min((current / target) * 100, 100)
        self.token_label.configure(text=f"Tokens: {current:,} / {target:,}")
        elapsed = time.time() - self.start_time
        if elapsed > 0:
            speed = current / elapsed
            self.speed_label.configure(text=f"Speed: {speed:,.0f} tokens/sec")

    def export_output(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if path:
            content = self.log_text.get(1.0, tk.END)
            with open(path, "w") as f:
                f.write(content)
            messagebox.showinfo("Export", f"Exported to {path}")

def main():
    root = tk.Tk()
    app = NarrativeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
