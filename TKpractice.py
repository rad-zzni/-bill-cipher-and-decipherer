import tkinter as tk
from tkinter import ttk, TclError

# region tkinter1

window = tk.Tk()
window.title("Bill Cipher and Will Decipher")
window.geometry('400x650')

## MINIMUM SIZING
window.minsize(width=350, height=600)
##
window.attributes('-topmost', True)
astring = ''
copy1_button = None
copy2_button = None

### title i 
title_label = ttk.Label(master = window, text = 'Use the Bill Cipher:', font = 'Times 20 bold')
title_label.pack(pady = 5)

# endregion

### function area
def cipher(): 
    global copy1_button
    def copy_output():
        text = output_text.get("1.0", "end-1c") #IMPORTANT LINE
        window.clipboard_clear()
        window.clipboard_append(text)
    if not copy1_button :
        copy1_button = tk.Button(master = window, text="copy", command=copy_output)
        copy1_button.pack(after=output_text)
    astring = entry_string.get()
    leng = len(astring)
    try:
        key = entry_int.get()
        output_text.configure(state='normal')
        output_text.delete("1.0", "end")
        if 1 <= key <= 99:
            ciphered = []
            for i in range(0,key,1):
                ciphered.append(astring[i:leng:key] + "_")
            if key >= leng or key == 1:
                output_text.insert("1.0", ''.join(ciphered) + "\n \n ...You are not very bright. Why would you ever choose this key. Your words are not ciphered and thus unsafe.")
            else: 
                output_text.insert("1.0", ''.join(ciphered)) #VERY IMPORTANT LINE
        else:
            output_text.insert("1.0", 'You must choose a number from 1 to 99 as your \'Encryption key\'.')
        output_text.configure(state='disabled')
    except TclError:
        output_text.configure(state='normal')
        output_text.delete("1.0", "end")
        output_text.insert("1.0", 'Key must be a valid number.')
        output_text.configure(state='disabled')


def decipher():
    global copy2_button
    def copy_output2():
        text = output_text2.get("1.0", "end-1c")
        window.clipboard_clear()
        window.clipboard_append(text)
    if not copy2_button:
        copy2_button = tk.Button(master = window, text="copy", command=copy_output2)
        copy2_button.pack(after=output_text2)
    bstring = entry_string2.get()
    deciphered = []
    spl = bstring.split("_")
    maximum = len(spl[0]) + 1
    for i in range(1,maximum,1):
        for x in spl:
            if len(x) >= i:
                deciphered.append((x[i-1]))
    output_text2.configure(state='normal')
    output_text2.delete("1.0", "end")
    output_text2.insert("0.0", ''.join(deciphered))
    output_text2.configure(state='disabled')

#  region tkinter2

### input area for Bill
input_frame = ttk.Frame(master=window)
entry_string = tk.StringVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_string, width=int(30))
button = ttk.Button(master=input_frame, text = 'Commence', command = cipher)
entry.pack(pady=10)
button.pack()
input_frame.pack(pady=5)

### additional input of key
# input_frame2 = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry2 = ttk.Entry(master=input_frame, textvariable=entry_int, justify='left', width= int(4))
entry2.pack(side='right', pady=20)

### additional label
thisiskey= ttk.Label(master = input_frame, text = 'Enter the encryption key:', font = 'Times 15 bold')
thisiskey.pack(side='left', padx=5)
### output
output_text = tk.Text(master=window, height=5, width=40, font=('Times', 15), wrap='word')
output_text.pack()
output_text.configure(state='disabled')

### FIRST COPY BUTTON


### title for Will
title_label2 = ttk.Label(master = window, text = 'Use the Will Decipher:', font = 'Times 20 bold')
title_label2.pack(pady=15)

### input area for Will
input_frame2 = ttk.Frame(master=window)
entry_string2 = tk.StringVar()
entry2 = ttk.Entry(master=input_frame2, textvariable=entry_string2, width=int(30))
button2 = ttk.Button(master=input_frame2, text = 'Commence', command = decipher)
entry2.pack(pady=10)
button2.pack()
input_frame2.pack(pady=5)

### output for Will
output_text2 = tk.Text(master=window, height=5.5, width=40, font=('Times', 15), wrap='word')
output_text2.pack()
output_text2.configure(state='disabled')


### run
window.mainloop()
# endregion