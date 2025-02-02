import customtkinter

def greet():
  """Displays the entered name in a label."""
  name = entry.get()
  label.configure(text=f"Hello, {name}!")

# Initialize CustomTkinter
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Create the main window
window = customtkinter.CTk()
window.title("Name Greeter")

# Create a label for the input field
label_name = customtkinter.CTkLabel(master=window, text="Enter your name:")
label_name.grid(row=0, column=0, padx=0, pady=0)

# Create an entry field for the user to input their name
entry = customtkinter.CTkEntry(master=window)
entry.grid(row=1, column=0, padx=0, pady=0)

# Create a button to trigger the greeting
button = customtkinter.CTkButton(master=window, text="Greet", command=greet)
button.grid(row=2, column=0, padx=0, pady=0)

# Create a label to display the greeting message
label = customtkinter.CTkLabel(master=window, text="")
label.grid(row=3, column=0, padx=0, pady=0)

# Start the GUI event loop
window.mainloop()