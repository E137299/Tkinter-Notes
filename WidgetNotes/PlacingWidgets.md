## **Placing Widgets on the `root` Window**

In Tkinter, the **`root` window** (created with `Tk()`) is the main container where all widgets—like buttons, labels, and entry fields—are placed. You use **geometry managers** to control where and how widgets appear inside this window.

---

### **Three Ways to Place Widgets**

Tkinter provides **three geometry managers** to position widgets:

| Geometry Manager | Description                                             |
|------------------|---------------------------------------------------------|
| `pack()`         | Stacks widgets vertically or horizontally (simplest)   |
| `grid()`         | Arranges widgets in a table-like row/column structure  |
| `place()`        | Positions widgets at specific x, y coordinates         |

---

### **Using `pack()`**

The `pack()` method is the simplest layout manager. It stacks widgets **top to bottom** by default.

```python
from tkinter import *

root = Tk()

Label(root, text="Top").pack()
Button(root, text="Middle").pack()
Entry(root).pack()

root.mainloop()
```

**Options:**
- `side="left"`: Stack left-to-right
- `fill="x"` or `fill="y"`: Expand to fill space
- `expand=True`: Widget expands to fill extra space

---

### **Using `grid()`**

The `grid()` method arranges widgets in a **row/column format** like a spreadsheet.

```python
from tkinter import *

root = Tk()

Label(root, text="Name:").grid(row=0, column=0)
Entry(root).grid(row=0, column=1)

Label(root, text="Email:").grid(row=1, column=0)
Entry(root).grid(row=1, column=1)

Button(root, text="Submit").grid(row=2, columnspan=2)

root.mainloop()
```

**Options:**
- `row`, `column`: Grid position
- `columnspan`: Span multiple columns
- `padx`, `pady`: Padding around the widget
- `sticky`: Align widget (`N`, `E`, `S`, `W`)

> 🔔 **Note**: Do **not mix** `pack()` and `grid()` inside the same container (e.g., `root` or a `Frame`).

---

### **Using `place()`**

The `place()` method gives you **absolute control** by setting pixel coordinates.

```python
from tkinter import *

root = Tk()
root.geometry("400x300")

Label(root, text="Username").place(x=50, y=50)
Entry(root).place(x=150, y=50)

Label(root, text="Password").place(x=50, y=100)
Entry(root, show="*").place(x=150, y=100)

Button(root, text="Login").place(x=150, y=150)

root.mainloop()
```

**Options:**
- `x`, `y`: Pixel coordinates from the top-left corner
- `width`, `height`: Set exact size
- `relx`, `rely`: Relative position (0.0 to 1.0)
- `anchor`: Anchor the widget at a reference point (e.g., `"center"`)

---

### **Choosing the Right Geometry Manager**

| Use Case                          | Recommended Manager |
|----------------------------------|---------------------|
| Simple stacking layout           | `pack()`            |
| Form-like layout (rows/columns)  | `grid()`            |
| Pixel-perfect layout             | `place()`           |

---

### **Example: Combining `Frame` with Layouts**

You can divide your window into sections using `Frame`, then use different layout managers inside each frame.

```python
top_frame = Frame(root)
top_frame.pack()

Label(top_frame, text="Top Section").pack()

bottom_frame = Frame(root)
bottom_frame.pack()

Button(bottom_frame, text="Click Me").pack()
```
