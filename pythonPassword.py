from random import randint, shuffle
from tkinter import *
# from tkinter import ttk
import pyperclip
import sys

def generate_password(
    length, include_special, include_uppercase, include_lowercase, include_numbers
):
    special_characters = [
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
        "_",
        "+",
        "-",
        "=",
        "{",
        "}",
        "[",
        "]",
        "|",
        "\\",
        ";",
        ":",
        "'",
        '"',
        "<",
        ">",
        ",",
        ".",
        "/",
        "?",
        "`",
        "~",
    ]
    lowercase_letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    uppercase_letters = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Make copies of the original arrays to avoid modifying them
    special_characters_copy = special_characters.copy()
    lowercase_letters_copy = lowercase_letters.copy()
    uppercase_letters_copy = uppercase_letters.copy()
    numbers_copy = numbers.copy()

    # Initialize an empty list to store the character sets based on user input
    character_sets = []

    if include_special:
        character_sets.append(special_characters_copy)
    if include_lowercase:
        character_sets.append(lowercase_letters_copy)
    if include_uppercase:
        character_sets.append(uppercase_letters_copy)
    if include_numbers:
        character_sets.append(numbers_copy)

    # Shuffle each character set
    for char_set in character_sets:
        shuffle(char_set)

    # Generate the password by randomly selecting characters from the shuffled sets
    password = ""
    for _ in range(length):
        # Select a random character set
        selected_set = character_sets[randint(0, len(character_sets) - 1)]
        # Select a random character from the set and add it to the password
        password += selected_set[randint(0, len(selected_set) - 1)]

    return password

def copy_to_clipboard(label):
    text = label['text']
    pyperclip.copy(text)
    label.config(text="Text copied to clipboard",)

    
def main_gui_app():
    def generate_and_display_password():
        # Get the length of the password
        length = int(length_var.get())
        # Get the options for including special characters, uppercase letters, lowercase letters, and numbers
        include_special = special_var.get() == 1
        include_uppercase = uppercase_var.get() == 1
        include_lowercase = lowercase_var.get() == 1
        include_numbers = numbers_var.get() == 1

        # Generate the password
        password = generate_password(
            length,
            include_special,
            include_uppercase,
            include_lowercase,
            include_numbers,
        )

        # Display the password in the label
        password_label.config(text=password)

    # estyle = ttk.Style()
    # estyle.element_create("plain.field", "from", "clam")
    # estyle.layout(
    #     "EntryStyle.TEntry",
    #     [
    #         (
    #             "Entry.plain.field",
    #             {
    #                 "children": [
    #                     (
    #                         "Entry.background",
    #                         {
    #                             "children": [
    #                                 (
    #                                     "Entry.padding",
    #                                     {
    #                                         "children": [
    #                                             ("Entry.textarea", {"sticky": "nswe"})
    #                                         ],
    #                                         "sticky": "nswe",
    #                                     },
    #                                 )
    #                             ],
    #                             "sticky": "nswe",
    #                         },
    #                     )
    #                 ],
    #                 "border": "2",
    #                 "sticky": "nswe",
    #             },
    #         )
    #     ],
    # )

    # estyle.configure(
    #     "EntryStyle.TEntry",
    #     fieldbackground="#261d31",  # Set background color
    #     foreground="white",  # Set color of elements
    #     bordercolor="white",
    # )  # Set color here

    root = Tk()
    root.geometry("400x400")
    root.configure(bg="#261d31")
    root.title("Password Maker")
    # icon= PhotoImage(file="lock.ico")
    root.iconbitmap(sys.executable)
    # root.iconphoto(True,icon)

    # Length entry
    length_var = StringVar()
    length_label = Label(
        root,
        text="Length of password:",
        background="#261d31",
        foreground="white",
        font="Helvetica",
    )
    length_label.pack(pady=5)
    length_entry = Entry(
        root,
        textvariable=length_var,
    )
    length_entry.pack(pady=10)

    # Checkboxes for including special characters, uppercase letters, lowercase letters, and numbers
    special_var = IntVar()
    special_checkbox = Checkbutton(
        root,
        text="Include special characters",
        variable=special_var,
        onvalue=1,
        offvalue=0,
            background="#261d31",
        foreground="#7436ca",
    )
    special_checkbox.pack(pady=5)
    uppercase_var = IntVar()
    uppercase_checkbox = Checkbutton(
        root,
        text="Include uppercase letters",
        variable=uppercase_var,
        onvalue=1,
        offvalue=0,
            background="#261d31",
        foreground="gray",
    )
    uppercase_checkbox.pack()
    lowercase_var = IntVar()
    lowercase_checkbox = Checkbutton(
        root,
        text="Include lowercase letters",
        variable=lowercase_var,
        onvalue=1,
        offvalue=0,
            background="#261d31",
        foreground="gray",
    )
    lowercase_checkbox.pack(pady=5)
    numbers_var = IntVar()
    numbers_checkbox = Checkbutton(
        root, text="Include numbers", variable=numbers_var, onvalue=1, offvalue=0,
            background="#261d31",
        foreground="gray",
    )
    numbers_checkbox.pack(pady=5)

    # Button to generate password
    generate_button = Button(
        root,
        text="Generate Password",
        command=generate_and_display_password,
        background="#261d31",
        foreground="gray",
    )
    generate_button.pack(pady=10)

    # Label to display the generated password
    password_label = Label(
        root,
        text="Your Password",
        background="#261d31",  # Set background color
        foreground="white",  # Set color of elements
        font="Helvetica",
    )
    password_label.pack(pady=10)

    password_label.bind("<Button-1>", lambda event: copy_to_clipboard(password_label))


    # entry = ttk.Entry(root, style="EntryStyle.TEntry")
    # entry.pack(padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main_gui_app()
