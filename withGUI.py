#Uses qrcode library for qr code generation
import qrcode


#Tkinter library for adding for GUI
import tkinter as tk
from tkinter import Tk, Label, Entry, Button, messagebox, filedialog, ttk



#Create Window
win = tk.Tk()
win.title("QR Code Generator - AD")
win.geometry("400x300")



#Adding Style object
style = ttk.Style()


#print(style.theme_names())
style.theme_use("xpnative")

#Taking the input

#create a text label above the entry field
ttk.Label(win, text="Enter text/URL").pack(pady = 10)

#a single-line text box allowing users to type URL/text
#set to 50 characters wide
data_entry = Entry(win, width=100)


#positions text box below the label using Tkinter's pack manager
data_entry.pack(pady = 10)



def generate():
    # .get() to use the string
    data = data_entry.get().strip()
    while data == "":
            messagebox.showerror("Error", "Empty Text")
            return True
    while len(data) > 100:
        messagebox.showerror("Error", "Too Long")
        return True

    qr = qrcode.QRCode(
       version=1,

        #Low error correction sets the QR code to the lowest "safety level" for fixing mistakes
        #meaning it can still work even if up to 7% of the code gets damaged, like if it's scratched or dirty.
        #This is like adding a small backup plan to the QR so a scanner can guess and fix small errors
        #at the same time keeps the QR small and holds more real info.
        error_correction=qrcode.constants.ERROR_CORRECT_L,


        #make each tiny square (called a module) in the QR pattern 10 pixels wide and tall.
        box_size = 10,
        border = 2
    )






    #add data to the qr
    qr.add_data(data)

    #picking the right size(version) for qr code without wasting space
    qr.make(fit=True)



    #making the qr
    img = qr.make_image(fill_color = 'black', back_colour = 'white')



    #Creating Save dialog
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if filename:
        img.save(filename)
        messagebox.showinfo("Success", f"QR saved as {filename}")
    else:
        messagebox.showinfo("Cancelled", "Save cancelled.")


#About section
def about():
    messagebox.showinfo("About", "QR Code Generator || Created by Aranyak Dutta")

#Button
ttk.Button(win, text="Generate & Save QR", command=generate).pack(pady=20)
ttk.Button(win, text= "About the creator", command= about).pack(pady=10)





#Starting Tkinter's event loop
#keeping the window open and responsive to user actions like typing or clicking until closed
win.mainloop()


