## **What is a `Canvas` Widget?**

The `Canvas` widget in Tkinter is a versatile space where you can draw **shapes**, **display images**, **render text**, and create **custom graphics**. It is often used for diagrams, games, visualizations, and interactive applications.

---

### **Creating a Basic Canvas**

```python
from tkinter import *

root = Tk()
root.title("Canvas Example")

canvas = Canvas(root, width=400, height=300, bg="white")
canvas.pack()

root.mainloop()
```

**Explanation:**
- `width` and `height`: Define the canvas size.
- `bg`: Sets the background color of the canvas.

---

### **Drawing Shapes on the Canvas**

Tkinter's canvas has built-in methods to draw shapes like rectangles, ovals, lines, polygons, and arcs.

---

### **1. Drawing a Line**

```python
canvas.create_line(50, 100, 300, 100, fill="black", width=3)
```

- Draws a line from (50, 100) to (300, 100).
- `fill`: Line color.
- `width`: Thickness of the line.

---

### **2. Drawing a Rectangle**

```python
canvas.create_rectangle(50, 50, 200, 150, fill="skyblue", outline="black", width=2)
```

- Coordinates: Top-left (50, 50) to bottom-right (200, 150).
- `fill`: Interior color.
- `outline`: Border color.
- `width`: Border thickness.

---

### **3. Drawing an Oval**

```python
canvas.create_oval(100, 100, 200, 200, fill="yellow")
```

- Draws an ellipse that fits inside the bounding box from (100, 100) to (200, 200).
- If width = height, it becomes a circle.

---

### **4. Drawing a Polygon**

```python
canvas.create_polygon(150, 50, 200, 150, 100, 150, fill="green")
```

- Coordinates are x1, y1, x2, y2, ...
- Can be used to draw triangles, hexagons, etc.

---

### **5. Drawing Text**

```python
canvas.create_text(200, 20, text="Hello Canvas!", font=("Arial", 16), fill="blue")
```

- Places text at coordinates (200, 20).
- `font`: Set font and size.
- `fill`: Text color.

---

### **6. Drawing an Arc**

```python
canvas.create_arc(50, 50, 200, 200, start=0, extent=150, fill="orange")
```

- Draws part of an oval (like a pie slice).
- `start`: Starting angle in degrees.
- `extent`: How many degrees to draw from the start.

---

### **Common `Canvas` Methods**

| Method                 | Description                                   |
|------------------------|-----------------------------------------------|
| `create_line()`        | Draw a straight line                          |
| `create_rectangle()`   | Draw a rectangle                              |
| `create_oval()`        | Draw an ellipse or circle                     |
| `create_polygon()`     | Draw a shape with multiple sides              |
| `create_text()`        | Render text                                   |
| `create_arc()`         | Draw an arc or pie slice                      |
| `create_image()`       | Display an image (requires `PhotoImage`)      |
| `delete(item)`         | Remove a specific item                        |
| `coords(item, ...)`    | Get or set the coordinates of an item         |
| `move(item, dx, dy)`   | Move an item by dx and dy                     |

---

### **Moving and Deleting Canvas Items**

When you create shapes, you can assign them to a variable or ID, and then manipulate them:

```python
# Draw a rectangle and move it
rect = canvas.create_rectangle(50, 50, 150, 100, fill="red")
canvas.move(rect, 20, 30)  # Moves the rectangle 20px right and 30px down
```

```python
# Delete the rectangle later
canvas.delete(rect)
```

---

### **Interactive Example: Drawing with the Mouse**

```python
def draw_circle(event):
    x, y = event.x, event.y
    canvas.create_oval(x-10, y-10, x+10, y+10, fill="purple")

canvas = Canvas(root, width=400, height=300, bg="white")
canvas.pack()
canvas.bind("<Button-1>", draw_circle)  # Left mouse click

root.mainloop()
```

**Explanation:**
- This creates a circle wherever the user clicks.
- `event.x`, `event.y`: Coordinates of the mouse click.
- `bind("<Button-1>", ...)`: Listens for left-clicks on the canvas.

---

### **Using Tags to Group Items**

You can assign **tags** to canvas items to group and manipulate them:

```python
canvas.create_rectangle(10, 10, 100, 100, fill="blue", tags="box")
canvas.itemconfig("box", fill="green")  # Changes color of all items with tag "box"
canvas.delete("box")  # Deletes all items with tag "box"
```

---

### **Displaying Images on a Canvas**

```python
img = PhotoImage(file="example.png")
canvas.create_image(100, 100, image=img, anchor=CENTER)
```

- `anchor=CENTER`: Centers the image at the given coordinates.
- Keep a reference to the image (`img`) or it may not display correctly due to garbage collection.

---

## **When Should You Use a Canvas?**

- Drawing diagrams, shapes, or charts
- Making interactive applications (e.g., games)
- Custom GUI elements
- Animations or mouse-driven apps

