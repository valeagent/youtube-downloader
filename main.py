import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import subprocess
import threading
import os
import sys
import shutil
import json
from datetime import datetime
import random
import webbrowser

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Load user agent from config
        self.user_agent = self.load_user_agent()
        
        # Set a dark theme
        self.root.configure(bg='#2b2b2b')
        
        # Check dependencies
        self.check_dependencies()
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # URL input
        ttk.Label(
            self.main_frame,
            text="YouTube URL:",
            foreground='white',
            background='#2b2b2b'
        ).grid(row=0, column=0, sticky=tk.W)
        
        self.url_entry = ttk.Entry(self.main_frame, width=50)
        self.url_entry.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E), padx=5)
        
        # Cookies input
        cookies_frame = ttk.LabelFrame(
            self.main_frame,
            text="Cookies (for age-restricted/private videos)",
            padding="5"
        )
        cookies_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(
            cookies_frame,
            text="Get fresh cookies while signed in to YouTube:",
            foreground='white',
            background='#2b2b2b'
        ).grid(row=0, column=0, sticky=tk.W)
        
        # Get Cookies button with hyperlink
        self.get_cookies_btn = ttk.Button(
            cookies_frame,
            text="Get Cookies Extension",
            command=lambda: webbrowser.open("https://chromewebstore.google.com/detail/cclelndahbckbenkjhflpdbgdldlbecc?utm_source=item-share-cb")
        )
        self.get_cookies_btn.grid(row=0, column=1, sticky=tk.W, padx=5)
        
        self.cookies_text = scrolledtext.ScrolledText(
            cookies_frame,
            width=50,
            height=5,
            bg='#1e1e1e',
            fg='#00ff00'
        )
        self.cookies_text.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # Load existing cookies if available
        self.load_cookies()
        
        # Save cookies button
        self.save_cookies_btn = ttk.Button(
            cookies_frame,
            text="Save Cookies",
            command=self.save_cookies
        )
        self.save_cookies_btn.grid(row=2, column=0, sticky=tk.W, pady=5)
        
        # Download options
        options_frame = ttk.LabelFrame(
            self.main_frame,
            text="Download Options",
            padding="5"
        )
        options_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        # Format selection
        ttk.Label(
            options_frame,
            text="Format:",
            foreground='white',
            background='#2b2b2b'
        ).grid(row=0, column=0, sticky=tk.W)
        
        self.format_var = tk.StringVar(value="best")
        format_combo = ttk.Combobox(options_frame, textvariable=self.format_var, state="readonly")
        format_combo['values'] = ('best', '720p', '480p', '360p')
        format_combo.grid(row=0, column=1, sticky=tk.W, padx=5)
        
        # Media type selection
        ttk.Label(
            options_frame,
            text="Media Type:",
            foreground='white',
            background='#2b2b2b'
        ).grid(row=1, column=0, sticky=tk.W)
        
        self.media_var = tk.StringVar(value="video")
        media_combo = ttk.Combobox(options_frame, textvariable=self.media_var, state="readonly")
        media_combo['values'] = ('video', 'audio')
        media_combo.grid(row=1, column=1, sticky=tk.W, padx=5)
        
        # Download button
        self.download_btn = ttk.Button(
            self.main_frame,
            text="Download",
            command=self.start_download
        )
        self.download_btn.grid(row=3, column=1, pady=10)
        
        # Nuclear Button
        self.nuclear_btn = ttk.Button(
            self.main_frame,
            text="Nuclear Button",
            command=self.nuclear_button,
            style='Danger.TButton'
        )
        self.nuclear_btn.grid(row=3, column=2, pady=10, padx=5)
        
        # Create a style for the nuclear button
        style = ttk.Style()
        style.configure('Danger.TButton', foreground='red')
        
        # Log area
        self.log_text = scrolledtext.ScrolledText(
            self.main_frame,
            width=70,
            height=20,
            bg='#1e1e1e',
            fg='#00ff00'
        )
        self.log_text.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        # Configure grid weights
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(4, weight=1)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        # Create downloads directory if it doesn't exist
        if not os.path.exists('downloads'):
            os.makedirs('downloads')

    def load_user_agent(self):
        """Load user agent from config.json."""
        try:
            with open('config.json', 'r') as f:
                config = json.load(f)
                return config.get('user_agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36')
        except FileNotFoundError:
            return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'

    def check_dependencies(self):
        """Check for required dependencies and show error messages if missing."""
        missing_deps = []
        
        # Check yt-dlp
        try:
            import yt_dlp
        except ImportError:
            missing_deps.append("yt-dlp")
        
        # Check ffmpeg
        if shutil.which("ffmpeg") is None:
            missing_deps.append("ffmpeg")
        
        if missing_deps:
            message = "The following dependencies are missing:\n\n"
            for dep in missing_deps:
                message += f"- {dep}\n"
            message += "\nPlease install them and try again."
            messagebox.showerror("Missing Dependencies", message)
            sys.exit(1)

    def load_cookies(self):
        try:
            if os.path.exists('cookies.txt'):
                with open('cookies.txt', 'r') as f:
                    self.cookies_text.delete(1.0, tk.END)
                    self.cookies_text.insert(tk.END, f.read())
        except Exception as e:
            self.log(f"Error loading cookies: {str(e)}")

    def save_cookies(self):
        try:
            cookies_content = self.cookies_text.get(1.0, tk.END).strip()
            if not cookies_content:
                messagebox.showwarning("Warning", "No cookies content to save.")
                return
                
            with open('cookies.txt', 'w', encoding='utf-8') as f:
                f.write(cookies_content)
            self.log("Cookies saved successfully!")
        except Exception as e:
            self.log(f"Error saving cookies: {str(e)}")
            messagebox.showerror("Error", f"Failed to save cookies: {str(e)}")

    def log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Color coding for different types of messages
        if "error" in message.lower():
            color = "#ff0000"  # Red for errors
        elif "warning" in message.lower():
            color = "#ffff00"  # Yellow for warnings
        elif "success" in message.lower():
            color = "#00ff00"  # Green for success
        else:
            color = "#00ff00"  # Default green for normal messages
            
        self.log_text.tag_config("colored", foreground=color)
        self.log_text.insert(tk.END, f"[{timestamp}] ", "colored")
        self.log_text.insert(tk.END, f"{message}\n", "colored")
        self.log_text.see(tk.END)

    def get_format(self):
        format_map = {
            'best': 'best',
            '720p': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
            '480p': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
            '360p': 'bestvideo[height<=360]+bestaudio/best[height<=360]'
        }
        base_format = format_map[self.format_var.get()]
        if self.media_var.get() == 'audio':
            return 'bestaudio/best'
        return base_format

    def download_video(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Warning", "Please enter a YouTube URL")
            return

        try:
            # Build the command
            cmd = [
                "yt-dlp",
                "--no-playlist",
                "--user-agent", self.user_agent,
                "-o", "downloads/%(title)s [%(id)s].%(ext)s"
            ]

            # Add format if not "best"
            if self.get_format() != "best":
                cmd.extend(["-f", self.get_format()])

            # Add cookies if available
            if os.path.exists('cookies.txt'):
                cmd.extend(["--cookies", "cookies.txt"])

            # Add audio extraction if audio is selected
            if self.media_var.get() == 'audio':
                cmd.extend(["-x", "--audio-format", "mp3"])

            # Add the URL
            cmd.append(url)

            self.log(f"Starting download: {url}")
            self.log(f"Command: {' '.join(cmd)}")
            
            # Run the command and capture output
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                bufsize=1
            )

            # Read output in real-time
            for line in process.stdout:
                self.log(line.strip())

            # Wait for the process to complete
            process.wait()
            
            if process.returncode == 0:
                self.log("Download completed successfully!")
                messagebox.showinfo("Success", "Download completed successfully!")
            else:
                self.log(f"Download failed with return code {process.returncode}")
                messagebox.showerror("Error", "Download failed. Check the log for details.")

        except Exception as e:
            self.log(f"Error during download: {str(e)}")
            messagebox.showerror("Error", f"Download failed: {str(e)}")

    def start_download(self):
        self.download_btn.config(state='disabled')
        download_thread = threading.Thread(target=self.download_video)
        download_thread.daemon = True
        download_thread.start()
        self.root.after(100, self.check_download_status, download_thread)

    def check_download_status(self, thread):
        if thread.is_alive():
            self.root.after(100, self.check_download_status, thread)
        else:
            self.download_btn.config(state='normal')

    def nuclear_button(self):
        """Nuclear Button: Force upgrade yt-dlp and clear all caches."""
        if messagebox.askyesno("Nuclear Button", 
            "This will:\n"
            "1. Force upgrade yt-dlp to the latest version\n"
            "2. Clear all caches\n"
            "3. Restart the application\n\n"
            "Are you sure you want to proceed?"):
            
            self.log("Nuclear Button activated! Initiating system reset...")
            
            try:
                # Force upgrade yt-dlp
                self.log("Upgrading yt-dlp...")
                subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "--force-reinstall", "yt-dlp"], 
                             check=True, capture_output=True, text=True)
                self.log("yt-dlp upgraded successfully")
                
                # Clear caches
                self.log("Clearing caches...")
                cache_dirs = [
                    os.path.expanduser("~/.cache/yt-dlp"),
                    os.path.expanduser("~/.cache/youtube-dl")
                ]
                for cache_dir in cache_dirs:
                    if os.path.exists(cache_dir):
                        shutil.rmtree(cache_dir)
                        self.log(f"Cleared cache: {cache_dir}")
                
                self.log("System reset complete! Restarting application...")
                messagebox.showinfo("Success", "System reset complete! The application will now restart.")
                
                # Restart the application
                python = sys.executable
                os.execl(python, python, *sys.argv)
                
            except Exception as e:
                self.log(f"Error during system reset: {str(e)}")
                messagebox.showerror("Error", f"Failed to complete system reset: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop() 