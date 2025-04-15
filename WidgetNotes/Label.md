## **What is a `Label` Widget?**

The `Label` widget in Tkinter is used to display text or images in a window. It is a static widget, meaning it doesn’t accept user input like buttons or entry fields. Labels are useful for providing instructions, displaying output, or simply adding visual elements to your GUI.

---

### **Basic Syntax**
The basic syntax for creating a label in Tkinter is:

```python
from tkinter import *

root = Tk()
root.geometry("800x600+20+20")

label = Label(root, text="Welcome to Tkinter!", font=("Arial", 16), fg="blue", bg="lightyellow")
label.place(x = 300, y = 100, width = 200, height = 50)

root.mainloop()
```

Tkinter labels can be customized in several ways using different options. Here are a few common properties:

| Option     | Description                                   |
|------------|-----------------------------------------------|
| `text`     | The text to display on the label.             |
| `font`     | Specifies the font type and size.             |
| `fg`       | The text (foreground) color.                  |
| `bg`       | The background color of the label.            |
| `width`    | The width of the label (in characters).       |
| `height`   | The height of the label (in lines of text).   |
| `borderwidth`| Adds a border around the label.             |
| `relief`   | Changes the border style (e.g., raised, sunken). |
| `image`    | Displays image.                               |

#### Example: Customizing a Label's Appearance

```python
label = Label(root, 
              text="Stylized Label", 
              font=("Helvetica", 20, "bold"), 
              fg="white", 
              bg="black", 
              borderwidth=2, 
              relief="solid")
label.pack(padx=20, pady=20)
```

---


### **Interactive Example: Label Update Based on Button Click**

You can update the content of a label in response to an event, such as a button click.

#### Example: Changing Label Text on Button Press

```python
from tkinter import *

root = Tk()

# Function to update the label
def update_label():
    label.config(text="Button Clicked!")

# Create a label
label = Label(root, text="Initial Text", font=("Arial", 14))
label.place(x = 300, y = 100, width = 200, height = 50)

# Create a button that updates the label
button = Button(root, text="Click Me", command=update_label)
label.place(x = 300, y = 200, width = 200, height = 50)

root.mainloop()
```

In this example, the text in the label changes when the button is clicked, demonstrating how labels can be updated dynamically.
