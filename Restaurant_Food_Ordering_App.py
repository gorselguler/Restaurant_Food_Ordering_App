import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Delicious Restaurant")
        self.root.geometry("900x700")
        self.root.configure(bg="#FFF5E6")
        
        self.menu = {
            "Burger": 8.99,
            "Pizza": 12.99,
            "Pasta": 10.99,
            "Salad": 6.99,
            "Fries": 3.99,
            "Soda": 1.99,
            "Coffee": 2.49,
            "Ice Cream": 4.99,
            "Sandwich": 7.49,
            "Soup": 5.99
        }
        
        self.emojis = {
            "Burger": "🍔",
            "Pizza": "🍕",
            "Pasta": "🍝",
            "Salad": "🥗",
            "Fries": "🍟",
            "Soda": "🥤",
            "Coffee": "☕",
            "Ice Cream": "🍦",
            "Sandwich": "🥪",
            "Soup": "🍲"
        }
        
        self.cart = {}
        self.order_history = []
        self.create_widgets()
    
    def create_widgets(self):
        header_frame = tk.Frame(self.root, bg="#FF6B35", height=80)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="DELICIOUS RESTAURANT",
            font=("Arial", 24, "bold"),
            bg="#FF6B35",
            fg="white"
        )
        title_label.pack(side="left", padx=20, pady=20)
        
        history_btn = tk.Button(
            header_frame,
            text="Order History",
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#FF6B35",
            cursor="hand2",
            command=self.show_order_history,
            padx=20,
            pady=5
        )
        history_btn.pack(side="right", padx=20)
        
        main_frame = tk.Frame(self.root, bg="#FFF5E6")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        left_frame = tk.Frame(main_frame, bg="white", relief="raised", bd=2)
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        menu_label = tk.Label(
            left_frame,
            text="MENU",
            font=("Arial", 18, "bold"),
            bg="#FF6B35",
            fg="white",
            pady=10
        )
        menu_label.pack(fill="x")
        
        menu_scroll_frame = tk.Frame(left_frame, bg="white")
        menu_scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        canvas = tk.Canvas(menu_scroll_frame, bg="white", highlightthickness=0)
        scrollbar = ttk.Scrollbar(menu_scroll_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="white")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        for item, price in self.menu.items():
            self.create_menu_item(scrollable_frame, item, price)
        
        right_frame = tk.Frame(main_frame, bg="white", relief="raised", bd=2)
        right_frame.pack(side="right", fill="both", expand=True)
        
        cart_label = tk.Label(
            right_frame,
            text="YOUR CART",
            font=("Arial", 18, "bold"),
            bg="#4ECDC4",
            fg="white",
            pady=10
        )
        cart_label.pack(fill="x")
        
        self.cart_frame = tk.Frame(right_frame, bg="white")
        self.cart_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        bottom_frame = tk.Frame(right_frame, bg="white")
        bottom_frame.pack(fill="x", padx=10, pady=10)
        
        self.total_label = tk.Label(
            bottom_frame,
            text="Total: $0.00",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#FF6B35"
        )
        self.total_label.pack(pady=10)
        
        checkout_btn = tk.Button(
            bottom_frame,
            text="CHECKOUT",
            font=("Arial", 14, "bold"),
            bg="#44AF69",
            fg="white",
            activebackground="#3A9B5C",
            activeforeground="white",
            cursor="hand2",
            relief="raised",
            bd=3,
            command=self.checkout,
            height=2
        )
        checkout_btn.pack(fill="x", pady=5)
        
        clear_btn = tk.Button(
            bottom_frame,
            text="Clear Cart",
            font=("Arial", 12),
            bg="#F25F5C",
            fg="white",
            activebackground="#D94F4C",
            activeforeground="white",
            cursor="hand2",
            command=self.clear_cart
        )
        clear_btn.pack(fill="x")
        
        self.update_cart_display()
    
    def create_menu_item(self, parent, item, price):
        item_frame = tk.Frame(parent, bg="white", relief="solid", bd=1)
        item_frame.pack(fill="x", pady=5, padx=5)
        
        info_frame = tk.Frame(item_frame, bg="white")
        info_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        emoji = self.emojis.get(item, "")
        name_label = tk.Label(
            info_frame,
            text=f"{emoji} {item}",
            font=("Arial", 12, "bold"),
            bg="white",
            anchor="w"
        )
        name_label.pack(anchor="w")
        
        price_label = tk.Label(
            info_frame,
            text=f"${price:.2f}",
            font=("Arial", 11),
            bg="white",
            fg="#FF6B35",
            anchor="w"
        )
        price_label.pack(anchor="w")
        
        add_btn = tk.Button(
            item_frame,
            text="Add",
            font=("Arial", 10, "bold"),
            bg="#FF6B35",
            fg="white",
            activebackground="#E55A2B",
            activeforeground="white",
            cursor="hand2",
            command=lambda: self.add_to_cart(item, price)
        )
        add_btn.pack(side="right", padx=10, pady=10)
    
    def add_to_cart(self, item, price):
        if item in self.cart:
            self.cart[item]["quantity"] += 1
        else:
            self.cart[item] = {"price": price, "quantity": 1}
        
        self.update_cart_display()
    
    def remove_from_cart(self, item):
        if item in self.cart:
            self.cart[item]["quantity"] -= 1
            if self.cart[item]["quantity"] <= 0:
                del self.cart[item]
        
        self.update_cart_display()
    
    def delete_from_cart(self, item):
        if item in self.cart:
            del self.cart[item]
        
        self.update_cart_display()
    
    def update_cart_display(self):
        for widget in self.cart_frame.winfo_children():
            widget.destroy()
        
        if not self.cart:
            empty_label = tk.Label(
                self.cart_frame,
                text="Your cart is empty",
                font=("Arial", 12),
                bg="white",
                fg="gray"
            )
            empty_label.pack(pady=50)
        else:
            for item, details in self.cart.items():
                cart_item_frame = tk.Frame(self.cart_frame, bg="#F8F9FA", relief="solid", bd=1)
                cart_item_frame.pack(fill="x", pady=5)
                
                emoji = self.emojis.get(item, "")
                info_label = tk.Label(
                    cart_item_frame,
                    text=f"{emoji} {item}\n${details['price']:.2f} x {details['quantity']}",
                    font=("Arial", 10),
                    bg="#F8F9FA",
                    anchor="w",
                    justify="left"
                )
                info_label.pack(side="left", padx=10, pady=5)
                
                btn_frame = tk.Frame(cart_item_frame, bg="#F8F9FA")
                btn_frame.pack(side="right", padx=5)
                
                minus_btn = tk.Button(
                    btn_frame,
                    text="-",
                    font=("Arial", 10, "bold"),
                    bg="#FFB84D",
                    fg="white",
                    width=3,
                    cursor="hand2",
                    command=lambda i=item: self.remove_from_cart(i)
                )
                minus_btn.pack(side="left", padx=2)
                
                plus_btn = tk.Button(
                    btn_frame,
                    text="+",
                    font=("Arial", 10, "bold"),
                    bg="#44AF69",
                    fg="white",
                    width=3,
                    cursor="hand2",
                    command=lambda i=item: self.add_to_cart(i, details['price'])
                )
                plus_btn.pack(side="left", padx=2)
                
                delete_btn = tk.Button(
                    btn_frame,
                    text="X",
                    font=("Arial", 10, "bold"),
                    bg="#F25F5C",
                    fg="white",
                    width=3,
                    cursor="hand2",
                    command=lambda i=item: self.delete_from_cart(i)
                )
                delete_btn.pack(side="left", padx=2)
        
        total = sum(details['price'] * details['quantity'] for details in self.cart.values())
        self.total_label.config(text=f"Total: ${total:.2f}")
    
    def clear_cart(self):
        if self.cart:
            self.cart = {}
            self.update_cart_display()
    
    def checkout(self):
        if not self.cart:
            messagebox.showwarning("Empty Cart", "Your cart is empty!\nPlease add items before checkout.")
            return
        
        total = sum(details['price'] * details['quantity'] for details in self.cart.values())
        item_count = sum(details['quantity'] for details in self.cart.values())
        order_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        order = {
            "time": order_time,
            "items": dict(self.cart),
            "total": total,
            "item_count": item_count
        }
        self.order_history.append(order)
        
        self.save_order_to_file(order)
        
        order_details = f"Order Confirmed!\n\n"
        order_details += f"Order Number: #{len(self.order_history)}\n"
        order_details += f"Time: {order_time}\n"
        order_details += f"Items: {item_count}\n"
        order_details += f"Total: ${total:.2f}\n\n"
        order_details += "Your order has been sent to the kitchen.\n"
        order_details += "Estimated time: 15-20 minutes.\n"
        order_details += "Thank you for your order!"
        
        messagebox.showinfo("Order Successful", order_details)
        
        self.cart = {}
        self.update_cart_display()
    
    def save_order_to_file(self, order):
        try:
            with open("orders.txt", "a", encoding="utf-8") as f:
                f.write(f"\n{'='*50}\n")
                f.write(f"Order #{len(self.order_history)}\n")
                f.write(f"Time: {order['time']}\n")
                f.write(f"{'='*50}\n")
                for item, details in order['items'].items():
                    emoji = self.emojis.get(item, "")
                    f.write(f"{emoji} {item} x{details['quantity']} = ${details['price'] * details['quantity']:.2f}\n")
                f.write(f"{'-'*50}\n")
                f.write(f"Total: ${order['total']:.2f}\n")
                f.write(f"{'='*50}\n\n")
        except Exception as e:
            print(f"Error saving order: {e}")
    
    def show_order_history(self):
        if not self.order_history:
            messagebox.showinfo("Order History", "No orders yet!")
            return
        
        history_window = tk.Toplevel(self.root)
        history_window.title("Order History")
        history_window.geometry("600x500")
        history_window.configure(bg="white")
        
        header = tk.Label(
            history_window,
            text="ORDER HISTORY",
            font=("Arial", 18, "bold"),
            bg="#FF6B35",
            fg="white",
            pady=10
        )
        header.pack(fill="x")
        
        canvas = tk.Canvas(history_window, bg="white")
        scrollbar = ttk.Scrollbar(history_window, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="white")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")
        
        for idx, order in enumerate(self.order_history, 1):
            order_frame = tk.Frame(scrollable_frame, bg="#F8F9FA", relief="solid", bd=2)
            order_frame.pack(fill="x", pady=10, padx=10)
            
            header_label = tk.Label(
                order_frame,
                text=f"Order #{idx} - {order['time']}",
                font=("Arial", 12, "bold"),
                bg="#4ECDC4",
                fg="white",
                anchor="w",
                padx=10,
                pady=5
            )
            header_label.pack(fill="x")
            
            items_frame = tk.Frame(order_frame, bg="#F8F9FA")
            items_frame.pack(fill="x", padx=10, pady=5)
            
            for item, details in order['items'].items():
                emoji = self.emojis.get(item, "")
                item_label = tk.Label(
                    items_frame,
                    text=f"{emoji} {item} x{details['quantity']} = ${details['price'] * details['quantity']:.2f}",
                    font=("Arial", 10),
                    bg="#F8F9FA",
                    anchor="w"
                )
                item_label.pack(anchor="w", pady=2)
            
            total_label = tk.Label(
                order_frame,
                text=f"Total: ${order['total']:.2f}",
                font=("Arial", 11, "bold"),
                bg="#F8F9FA",
                fg="#FF6B35",
                anchor="w",
                padx=10,
                pady=5
            )
            total_label.pack(anchor="w")

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()