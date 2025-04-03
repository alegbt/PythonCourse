import tkinter
from tkinter.font import Font


def create_popup():
    popup = tkinter.Toplevel()
    popup.title("window name")
    popup.geometry("500x500")

    font = Font(family="Helvetica", size=20)

    inputField = tkinter.Entry(popup, font=font)


    labels = ["DOCUMENTO ID",
              "Numero Documento id",
              "Data rilascio documento id",
              "Scadenza documento id",
              "TESSERA SANITARIA",
              "Scadenza tessera Sanitaria",
              "Codice fiscale"]

    for i, n in enumerate(labels):
        labels = tkinter.Label(popup, text=n, font=font)
        checkbutton = tkinter.Checkbutton(popup)
        labels.grid(row=i + 1, column=0, sticky='w', pady=2, padx=10)
        checkbutton.grid(row=i + 1, column=1, sticky='w')

    popup.resizable(True, True)


root = tkinter.Tk()
root.title("main")

popupBtn = tkinter.Button(root, text="open", command=create_popup)
popupBtn.pack(pady=20)

root.mainloop()