import tkinter as tk
from tkinter import filedialog
import PyPDF2


class PDFMergerApp:
    def __init__(self, master):
        self.master = master
        master.title("PDF Merger")

        # create top frame and bottom frame
        top_frame = tk.Frame(master, bd=5, relief=tk.RIDGE)
        top_frame.grid(row=0, column=0, padx=25, pady=25)

        bottom_frame = tk.Frame(master, relief=tk.GROOVE, border=3)
        bottom_frame.grid(row=1, column=0, pady=5)

        # Create buttons to select PDF files

        frame1 = tk.Frame(top_frame, bd=3, relief=tk.RAISED)
        frame1.grid(row=0, column=0, padx=5, pady=5)

        frame2 = tk.Frame(top_frame, bd=3, relief=tk.RAISED)
        frame2.grid(row=0, column=1, padx=5, pady=5)

        frame3 = tk.Frame(top_frame, bd=3, relief=tk.RAISED)
        frame3.grid(row=0, column=2, padx=5, pady=5)

        frame4 = tk.Frame(top_frame, bd=3, relief=tk.RAISED, bg='grey')
        frame4.grid(row=1, column=2, padx=5, pady=5, sticky=tk.E)

        self.canvas1 = tk.Canvas(frame1, width=20, height=20)
        self.canvas1.create_oval(2, 2, 18, 18, fill='grey')
        self.canvas1.grid(row=0, column=0)

        self.button1 = tk.Button(
            frame1, text="Select PDF 1", command=self.select_pdf1)
        self.button1.grid(row=0, column=1)

        self.canvas2 = tk.Canvas(frame2, width=20, height=20)
        self.canvas2.create_oval(2, 2, 18, 18, fill='grey')
        self.canvas2.grid(row=0, column=0)

        self.button2 = tk.Button(
            frame2, text="Select PDF 2", command=self.select_pdf2)
        self.button2.grid(row=0, column=1)

        # Create button to merge PDF files
        self.canvas3 = tk.Canvas(frame3, width=20, height=20)
        self.canvas3.create_oval(2, 2, 18, 18, fill='grey')
        self.canvas3.grid(row=0, column=0)

        self.merge_button = tk.Button(
            frame3, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_button.grid(row=0, column=1)

        self.restart_button = tk.Button(
            frame4, text="Restart", command=self.restart, bg='grey')
        self.restart_button.grid(row=0, column=0)

        # 会变颜色圆圈的提示词
        self.canvas4 = tk.Canvas(bottom_frame, width=20, height=20)
        self.canvas4.create_oval(2, 2, 18, 18, fill='grey')
        self.canvas4.grid(row=0, column=0, sticky=tk.W)

        self.label1 = tk.Label(
            bottom_frame, text=" represents Not selected or Not finished.")
        self.label1.grid(row=0, column=1, sticky=tk.W)

        self.canvas5 = tk.Canvas(bottom_frame, width=20, height=20)
        self.canvas5.create_oval(2, 2, 18, 18, fill='green')
        self.canvas5.grid(row=1, column=0, sticky=tk.W)

        self.label2 = tk.Label(
            bottom_frame, text=" represents selected or finished.")
        self.label2.grid(row=1, column=1, sticky=tk.W)

    def select_pdf1(self):
        self.pdf1_path = filedialog.askopenfilename(
            title="Select PDF 1", filetypes=[("PDF Files", "*.pdf")])
        if(self.pdf1_path == ''):
            print("No file was selected!")
        else:
            self.canvas1.create_oval(2, 2, 18, 18, fill='green')
            print("PDF 1 selected:", self.pdf1_path)

    def select_pdf2(self):
        self.pdf2_path = filedialog.askopenfilename(
            title="Select PDF 2", filetypes=[("PDF Files", "*.pdf")])
        self.canvas2.create_oval(2, 2, 18, 18, fill='green')
        print("PDF 2 selected:", self.pdf2_path)

    def merge_pdfs(self):
        pdf1 = open(self.pdf1_path, "rb")
        pdf2 = open(self.pdf2_path, "rb")
        merger = PyPDF2.PdfMerger()
        merger.append(pdf1)
        merger.append(pdf2)

        # Prompt user to select destination folder and filename for merged PDF
        save_path = filedialog.asksaveasfilename(
            title="Save Merged PDF", filetypes=[("PDF Files", "*.pdf")])

        # Save merged PDF to destination folder
        merged_pdf = open(save_path, "wb")
        merger.write(merged_pdf)

        # Close files
        pdf1.close()
        pdf2.close()
        merged_pdf.close()
        self.canvas3.create_oval(2, 2, 18, 18, fill='green')
        print("PDFs merged and saved to:", save_path)

    def restart(self):
        self.pdf1_path = ''
        self.pdf2_path = ''
        self.canvas1.create_oval(2, 2, 18, 18, fill='grey')
        self.canvas2.create_oval(2, 2, 18, 18, fill='grey')
        self.canvas3.create_oval(2, 2, 18, 18, fill='grey')


root = tk.Tk()
app = PDFMergerApp(root)
root.mainloop()
