import tkinter 
button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["svn", "8", "nne", "×"], 
    ["4", "fve", "6", "-"],
    ["one", "2", "tre", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "=", "0", ".","√"]
top_symbols = ["AC", "+/-", "%"]
custom = ["svn", "nne", "one", "tre"]

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_red = "#FF0000"
color_white = "white"

window = tkinter.Tk()
window.title("YOYO")
window.resizable(False, False)
def jam():
    if button:
     value = "5"        
frame = tkinter.Frame(window)
label = tkinter.Label(frame, font =("Arial", 40), width=column_count, text="0" ,background= color_dark_gray, anchor="w")

label.grid(row=0, columnspan= column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30), width=column_count -1, height= -1
                                , command=lambda value = value : buttonClicked(value))
        if value in top_symbols:
            button.config(foreground= color_red, background=color_white)
        elif value in right_symbols:
            button.config(foreground=color_red, background= color_white)
        elif value in custom:
            button.config(foreground= color_black, background=color_dark_gray)

        else:
            button.config(foreground=color_white, background=color_red)    
        button.grid(row=row+1, column=column)
        frame.pack()
# print(dir(button.config()))


window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/ 2))
window_y = int((screen_height/2)- (window_height/2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()


if buttonClicked((value)):
    print("hello owrld")
#window setup
# window = tkinter.Tk() #create the window
# window.title("Calculator")
# window.resizable(False, False)
# x = "samihdaushduahdowhduqm1389"
# v = hash(x)
# z = hash(v)
# print(v)

# import hashlib

# def hash_with_sha256(input_string):
#     """
#     Hashes the input string using SHA-256 and returns the hexadecimal digest.
#     """
#     if not isinstance(input_string, str):
#         raise ValueError("Input must be a string.")
    
#     # Encode the string to bytes
#     encoded_input = input_string.encode('utf-8')
    
#     # Create a SHA-256 hash object
#     sha256_hash = hashlib.sha256()
    
#     # Update the hash object with the encoded input
#     sha256_hash.update(encoded_input)
    
#     # Return the hexadecimal representation of the hash
#     return sha256_hash.hexdigest()

# # Example usage
# input_data = "sdjooq"
# hashed_data = hash_with_sha256(input_data)
# print(f"SHA-256 Hash: {hashed_data}")
