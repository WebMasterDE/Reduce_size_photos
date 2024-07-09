import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
from compress_photos import Compress_photos



class FolderPathApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Path Importer")
        self.root.geometry("400x200")

        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Custom colors
        self.style.configure('TFrame', background='#2b2b2b')
        self.style.configure('TLabel', background='#2b2b2b', foreground='#ffffff', font=('Helvetica', 12))
        self.style.configure('TEntry', foreground='#333333', fieldbackground='#f0f0f0', font=('Helvetica', 10))
        self.style.configure('TButton', background='#4caf50', foreground='#ffffff', font=('Helvetica', 10))
        self.style.map('TButton',
                       background=[('active', '#45a049'), ('pressed', '#388e3c')])

        self.frame = ttk.Frame(root, padding=10)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.label = ttk.Label(self.frame, text="Select a folder:")
        self.label.pack(pady=10)

        self.path_display = ttk.Entry(self.frame, width=50)
        self.path_display.pack(pady=5)

        # Configure drag and drop for the entire window
        self.root.drop_target_register(DND_FILES)
        self.root.dnd_bind('<<Drop>>', self.drop_inside_entry)

        self.browse_button = ttk.Button(self.frame, text="Browse", command=self.browse_folder)
        self.browse_button.pack(pady=5)

        self.execute_button = ttk.Button(self.frame, text="Execute Program", command=self.execute_program)
        self.execute_button.pack(pady=20)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.path_display.delete(0, tk.END)
            self.path_display.insert(0, folder_path)

    def drop_inside_entry(self, event):
        folder_path = event.data
        # Remove any curly braces wrapping the path on Windows
        if folder_path.startswith('{') and folder_path.endswith('}'):
            folder_path = folder_path[1:-1]
        # Ensure the path is valid and only take the first dropped item if multiple are dropped
        folder_path = folder_path.split(' ')[0]
        self.path_display.delete(0, tk.END)
        self.path_display.insert(0, folder_path)

    def execute_program(self):
        folder_path = self.path_display.get()
        if folder_path:
            try:
                # Replace this with the actual code you want to execute
                self.run_program(folder_path)
                messagebox.showinfo("Success", "Program executed successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "Please select a folder first.")

    def create_choice_window(self, number_images, folder_path):
        # Function to handle the button click event
        def handle_choice(choice):
            #messagebox.showinfo("Choice", f"You chose: {choice}")
            # When Proceed is clicked
            if choice == "YES":

                # call the function to reduce size > fullhd to fullhd
                compress_photos = Compress_photos()
                compress_photos.compress_images(folder_path)

            root.destroy()

        # Create the main window
        root = tk.Tk()
        root.title("Number of images")

        # Create a label inside the frame
        label = tk.Label(root, text=f"Number of image files:{number_images}")
        label.pack(side=tk.TOP, padx=10, pady=10)

        # Set window size
        root.geometry("300x200")

        # Create and place the first button
        button1 = tk.Button(root, text="Proceed", command=lambda: handle_choice("YES"))
        button1.pack(pady=20)

        # Create and place the second button
        button2 = tk.Button(root, text="STOP", command=lambda: handle_choice("NO"))
        button2.pack(pady=20)

        # Start the main event loop
        root.mainloop()
        return res

    def run_program(self, folder_path):
        # Example program logic
        print(f"Running program with folder: {folder_path}")

        compress_photos=Compress_photos()

        # image count
        image_file_count = compress_photos.count_image_files(folder_path)  # richiamo la funzione che mi conta quante immagini sono presenti nella directory_path
        choice = self.create_choice_window(image_file_count, folder_path)

if __name__ == "__main__":
    if os.name == 'posix':
        # Additional setup or alternative handling for Linux if needed
        print("Running on a POSIX-compliant system (Linux/Mac).")

    root = TkinterDnD.Tk()
    app = FolderPathApp(root)
    root.mainloop()
