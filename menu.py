import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# =========================
# 🍽 Umer's Flavor Haven GUI
# =========================

menu = {
    "Fast Food": {
        "Burger": 350, "Zinger Burger": 500, "Fries": 200, "Pizza Slice": 300,
        "Club Sandwich": 450, "Shawarma": 250, "Roll Paratha": 220, "Broast": 400,
        "Cheese Burger": 550, "Nuggets (6 pcs)": 300
    },
    "Chinese Food": {
        "Chicken Chowmein": 550, "Fried Rice": 400, "Manchurian": 600, "Chicken Shashlik": 650,
        "Beef Noodles": 700, "Schezwan Rice": 600, "Prawn Chowmein": 750, "Garlic Chicken": 650,
        "Hot & Sour Soup": 300, "Spring Rolls": 200
    },
    "Italian Food": {
        "Pasta Alfredo": 700, "Lasagna": 800, "Margherita Pizza": 900, "Fettuccine": 850,
        "Garlic Bread": 250, "Tiramisu": 450, "Spaghetti": 650, "Risotto": 750,
        "Bruschetta": 300, "Cheese Pizza": 950
    },
    "Desi Food": {
        "Biryani": 350, "Karahi": 900, "Daal Chawal": 250, "Naan": 50, "Haleem": 400,
        "Nihari": 500, "Chapli Kebab": 300, "Pulao": 350, "Qorma": 450, "Paratha": 80
    },
    "Bakery Items": {
        "Cake Slice": 250, "Cupcake": 150, "Cookies (Pack)": 200, "Brownie": 180, "Donut": 200,
        "Croissant": 220, "Puff Pastry": 170, "Tart": 190, "Muffin": 160, "Cream Roll": 180
    },
    "Sweets": {
        "Gulab Jamun": 150, "Jalebi": 180, "Ras Malai": 250, "Barfi": 200, "Kheer": 220,
        "Laddu": 180, "Cham Cham": 250, "Soan Papdi": 300, "Halwa": 200, "Patisa": 250
    },
    "Drinks": {
        "Mineral Water": 100, "Cold Drink": 150, "Juice": 200, "Milkshake": 250, "Smoothie": 300,
        "Energy Drink": 350, "Lemonade": 180, "Mint Margarita": 250, "Iced Coffee": 300, "Cold Water": 70
    },
    "Tea & Coffee": {
        "Tea": 100, "Green Tea": 120, "Coffee": 250, "Cappuccino": 300, "Espresso": 280,
        "Latte": 350, "Iced Tea": 200, "Hot Chocolate": 400, "Black Coffee": 250, "Karak Chai": 150
    }
}

# =========================
# Main Window Setup
# =========================
root = tk.Tk()
root.title("Umer's Flavor Haven")
root.geometry("1050x650")
root.config(bg="#f8f8f8")

order_items = []

# =========================
# Header (Restaurant Logo + Title)
# =========================
header_frame = tk.Frame(root, bg="#222222", height=100)
header_frame.pack(fill="x")

try:
    logo_img = Image.open("logo.png")
    logo_img = logo_img.resize((80, 80))
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(header_frame, image=logo_photo, bg="#222222")
    logo_label.image = logo_photo
    logo_label.pack(side="left", padx=20, pady=10)
except:
    tk.Label(header_frame, text="🍴", font=("Arial", 45), bg="#222222", fg="white").pack(side="left", padx=20, pady=10)

title_label = tk.Label(
    header_frame,
    text="UMER’S FLAVOR HAVEN\n",
    font=("Georgia", 26, "bold"),  # <- larger main name
    bg="#222222",
    fg="#FFD700",
    justify="left"
)
title_label.pack(side="left", pady=10)
title_label2 = tk.Label(
    header_frame,
    text="Where Taste Meets Tradition",
    font=("Georgia", 22),  # <- smaller font for subtitle
    bg="#222222",
    fg="#DDDDDD",
    justify="left"
)
title_label2.place(x=180, y=55)

# =========================
# Layout Frames
# =========================
left_frame = tk.Frame(root, width=250, bg="#333333")
left_frame.pack(side="left", fill="y")

right_frame = tk.Frame(root, bg="#f8f8f8")
right_frame.pack(side="right", expand=True, fill="both")

bill_frame = tk.Frame(right_frame, bg="#f8f8f8")
bill_frame.pack(side="bottom", fill="x")

scrollbar = tk.Scrollbar(bill_frame)
scrollbar.pack(side="right", fill="y")

bill_text = tk.Text(bill_frame, height=8, bg="#ffffff", font=("Arial", 12), yscrollcommand=scrollbar.set)
bill_text.pack(fill="x", padx=10, pady=5)
scrollbar.config(command=bill_text.yview)

# =========================
# Functions
# =========================
def show_category(category_name):
    for widget in right_frame.winfo_children():
        if widget != bill_frame:
            widget.destroy()

    tk.Label(right_frame, text=f"{category_name}", font=("Arial", 18, "bold"), bg="#f8f8f8").pack(pady=10)

    for item, price in menu[category_name].items():
        item_frame = tk.Frame(right_frame, bg="#ffffff", bd=1, relief="solid")
        item_frame.pack(fill="x", pady=2, padx=10)

        tk.Label(item_frame, text=f"{item} - Rs.{price}", font=("Arial", 12), bg="#ffffff").pack(side="left", padx=10)
        qty_entry = tk.Entry(item_frame, width=5)
        qty_entry.pack(side="right", padx=10)

        tk.Button(item_frame, text="Add", bg="#4CAF50", fg="white",
                  command=lambda i=item, p=price, e=qty_entry: add_item(i, p, e)).pack(side="right", padx=5)

def add_item(i, p, e):
    global bill_text
    qty = e.get()
    if qty.isdigit() and int(qty) > 0:
        if not bill_text or not bill_text.winfo_exists():
            messagebox.showwarning("Error", "Bill area not found! Please restart your order.")
            return
        order_items.append((i, int(qty), p))
        bill_text.insert(tk.END, f"{i} x {qty} = Rs.{int(qty)*p}\n")
        bill_text.see(tk.END)
        e.delete(0, tk.END)
    else:
        messagebox.showwarning("Invalid", "Enter a valid quantity!")

def show_total():
    global bill_text
    if not order_items:
        messagebox.showwarning("Empty", "No items in your order!")
        return
    if not bill_text or not bill_text.winfo_exists():
        messagebox.showwarning("Error", "Bill area not found! Please restart your order.")
        return

    bill_text.insert(tk.END, "\n-----------------------------------\n", "sep")
    bill_text.insert(tk.END, "🧾 Final Order Summary 🧾\n", "head")
    bill_text.insert(tk.END, "-----------------------------------\n", "sep")

    total = 0
    for item, qty, price in order_items:
        total += qty * price
        bill_text.insert(tk.END, f"{item} x {qty} = Rs.{qty*price}\n")

    bill_text.insert(tk.END, "-----------------------------------\n", "sep")
    bill_text.insert(tk.END, f"TOTAL BILL: Rs.{total:.2f}\n", "total")
    bill_text.tag_config("head", font=("Arial", 13, "bold"), foreground="#000080")
    bill_text.tag_config("total", font=("Arial", 14, "bold"), foreground="red")
    bill_text.tag_config("sep", font=("Arial", 12, "bold"))
    bill_text.see(tk.END)
    messagebox.showinfo("Total Bill", f"💰 Your total bill is Rs. {total:.2f}")

def clear_bill():
    global bill_text
    order_items.clear()
    if not bill_text or not bill_text.winfo_exists():
        bill_text = tk.Text(bill_frame, height=8, bg="#ffffff", font=("Arial", 12))
        bill_text.pack(fill="x", padx=10, pady=5)
        scrollbar.config(command=bill_text.yview)
        bill_text.config(yscrollcommand=scrollbar.set)
    bill_text.delete("1.0", tk.END)
    messagebox.showinfo("Cleared", "🧾 Bill cleared! Start a new order.")

def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

# =========================
# Left Menu Buttons
# =========================
tk.Label(left_frame, text="🍽 Categories", font=("Arial", 16, "bold"), fg="white", bg="#333333").pack(pady=10)

for category in menu.keys():
    tk.Button(left_frame, text=category, font=("Arial", 12), width=20, bg="#555555", fg="white",
              command=lambda c=category: show_category(c)).pack(pady=5)

tk.Button(left_frame, text="💰 Total Bill", font=("Arial", 12, "bold"), bg="#2196F3", fg="white",
          command=show_total).pack(pady=10)

tk.Button(left_frame, text="🆕 New Order", font=("Arial", 12, "bold"), bg="#FF9800", fg="white",
          command=clear_bill).pack(pady=10)

tk.Button(left_frame, text="🚪 Exit", font=("Arial", 12, "bold"), bg="#E53935", fg="white",
          command=exit_app).pack(pady=10)

# Run the GUI
root.mainloop()