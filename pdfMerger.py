# Importing the necessary library for GUI
import os
from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfMerger

# Creating a function to select PDF files
def select_files():
    # Opening a file dialog window to select PDF files
    files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    # Looping through the selected files and appending them to the PdfFileMerger object
    for file in files:
        pdf_merger.append(file)

    # Updating the listbox with selected PDF files
    update_listbox(files)

# Creating a function to merge the selected PDF files
def merge_files():
    # Getting the current working directory
    cwd = os.getcwd()
    # Writing the merged PDF file to the current working directory
    pdf_merger.write(os.path.join(cwd, 'merged_file.pdf'))
    # Closing the PDF file objects
    pdf_merger.close()

# Creating a function to clear the selected PDF files
def clear_files():
    # Clearing the PdfFileMerger object
    pdf_merger.pages = []
    # Displaying a message to the user
    # print("Selected PDF files have been cleared.")
    popup_window()

# Creating a function to display a pop-up window
def popup_window():
    # Creating a new window using Toplevel()
    popup = Toplevel()
    # Setting the title of the window
    popup.title("Alert")
    # Setting the size of the window
    popup.geometry("300x50")
    # Creating a label for the window
    label = Label(popup, text="Selected PDF files have been cleared.")
    # Packing the label into the window
    label.pack(pady=10)

# Function to update the listbox with selected PDF files
def update_listbox(files):
    # Clearing the current items in the listbox
    listbox.delete(0, END)
    # Looping through the selected files and adding them to the listbox
    for file in files:
        listbox.insert(END, os.path.basename(file))

# Creating a GUI window
root = Tk()

# Setting the title of the window
root.title("PDF Merger")

# Setting the size of the window
root.geometry("400x400")

# Creating a label for instructions
label = Label(root, text="Select two or more PDF files to merge")

# Creating a button to  select PDF files
select_button = Button(root, text="Select Files", command=select_files)

# Creating a listbox to display the selected PDF files
listbox = Listbox(root, selectmode=MULTIPLE)

# Creating a button to merge the selected PDF files
merge_button = Button(root, text="Merge Files", command=merge_files)

# Creating a button to clear the selected PDF files
clear_button = Button(root, text="Clear Files", command=clear_files)

# Packing the label and buttons into the window
label.pack(pady=10)
select_button.pack(pady=10)
# Adding the listbox to the window
listbox.pack(pady=10)
merge_button.pack(pady=10)
clear_button.pack(pady=10)

# Creating an object of PdfFileMerger class
pdf_merger = PdfMerger()

# Running the GUI window
root.mainloop()
