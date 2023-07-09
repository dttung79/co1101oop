from tkinter import *
from tkinter import messagebox
from product import Product, Store
from db import load_products
#### CREATE WINDOW ####
window = Tk()
window.title("Week 7 HW 1")
window.geometry("600x200")
fpt_store = Store()
curr_index = 0
#### HANDLE EVENTS ####
def btn_next_clicked():
    global curr_index   # refer to the global variable curr_index
    # increase curr_index by 1, using modulo to go back to 0 if curr_index is at the end
    curr_index = (curr_index + 1) % lst_products.size()
    # update form fields with product at curr_index
    update_form(curr_index)

def btn_prev_clicked():
    messagebox.showinfo("Not implemented", "You have to implement this function")
    # TODO: similar to btn_next_clicked, decrease curr_index and update form fields

def btn_first_clicked():
    messagebox.showinfo("Not implemented", "You have to implement this function")
    # TODO: set curr_index to 0 and update form fields

def btn_last_clicked():
    messagebox.showinfo("Not implemented", "You have to implement this function")
    # TODO: set curr_index to len(fpt_store.products) - 1 and update form fields


def btn_add_clicked():
    global curr_index   # refer to the global variable curr_index
    # create product from form fields
    p = Product(txt_name.get(), float(txt_price.get()), int(txt_stock.get()))
    # add product to fpt_store
    fpt_store.add(p)
    # add product to listbox
    lst_products.insert(END, p.name)
    # set current index to the newly added product
    curr_index = lst_products.size() - 1
    # update form fields with product at curr_index
    update_form(curr_index)
    # show message box to inform user that the product has been added
    messagebox.showinfo("Added", f"Product {p.name} has been added.")

def btn_delete_clicked():
    global curr_index   # refer to the global variable curr_index
    # get the product at curr_index
    p = fpt_store[curr_index]
    # remove the product from fpt_store
    fpt_store.remove(p.name)
    # remove the product from listbox
    lst_products.delete(curr_index)
    # if curr_index is at the end of the list, decrease curr_index by 1
    if curr_index == lst_products.size():
        curr_index -= 1
    # TODO: update form fields with product at curr_index
    
    # TODO: show message box to inform user that the product has been deleted

def btn_edit_clicked():
    global curr_index   # refer to the global variable curr_index
    # get the product at curr_index
    p = fpt_store[curr_index]
    # update product with form fields
    p.name = txt_name.get()
    p.price = float(txt_price.get())
    p.stock = int(txt_stock.get())
    # update listbox with the new product name
    lst_products.delete(curr_index)
    lst_products.insert(curr_index, p.name)
    # TODO: show message box to inform user that the product has been updated

def update_form(curr_index):
    # get product at curr_index
    p = fpt_store[curr_index]
    # update text of txt_name
    txt_name.delete(0, END)
    txt_name.insert(0, p.name)
    # TODO: update text of txt_price
    
    
    # TODO: update text of txt_stock
    

    # update selected text of lst_products
    lst_products.selection_clear(0, END)
    lst_products.selection_set(curr_index)
    lst_products.activate(curr_index)
    lst_products.see(curr_index)

def lst_products_clicked(event):
    global curr_index   # refer to the global variable curr_index
    # get the index of the clicked item
    curr_index = lst_products.curselection()[0]
    # update form fields with product at index
    update_form(curr_index)

#### CREATE WIDGETS ####
# Create label with text 'Product Management', center aligned
lbl_title = Label(window, text="Product Management", justify=CENTER)
lbl_title.grid(row=0, column=0, columnspan=10)

# Create a listbox with, height 5, width 30, left aligned
lst_products = Listbox(window, height=5, width=30, justify=LEFT, selectmode=SINGLE)
lst_products.grid(row=1, column=0, rowspan=4, columnspan=4, padx=5, pady=5)
# Bind lst_products's <<ListboxSelect>> event to lst_products_clicked
lst_products.bind("<<ListboxSelect>>", lst_products_clicked)

for p in load_products():
    fpt_store.add(p)
    # add product to listbox
    lst_products.insert(END, p.name)

# Set listbox to select the first item
update_form(0)

# Create button 'First', width 2, left aligned
btn_first = Button(window, text="|<", width=2, command=btn_first_clicked)
btn_first.grid(row=5, column=0)
# Create button 'Previous', width 2, left aligned
btn_prev = Button(window, text="<", width=2, command=btn_prev_clicked)
btn_prev.grid(row=5, column=1)
# Create button 'Next', width 2, left aligned
btn_next = Button(window, text=">", width=2, command=btn_next_clicked)
btn_next.grid(row=5, column=2)
# Create button 'Last', width 2, left aligned
btn_last = Button(window, text=">|", width=2, command=btn_last_clicked)
btn_last.grid(row=5, column=3)
# Create lable with text 'Product name', left aligned
lbl_name = Label(window, text="Product name", anchor=W)
lbl_name.grid(row=1, column=4)
# Create text entry for product name
txt_name = Entry(window)
txt_name.grid(row=1, column=5, columnspan=3)
# Create lable with text 'Price', left aligned
lbl_price = Label(window, text="Price", anchor=W)
lbl_price.grid(row=2, column=4)
# Create text entry for price
txt_price = Entry(window)
txt_price.grid(row=2, column=5, columnspan=3)
# Create lable with text 'Stock', left aligned
lbl_stock = Label(window, text="Stock", anchor=W)
lbl_stock.grid(row=3, column=4)
# Create text entry for stock
txt_stock = Entry(window)
txt_stock.grid(row=3, column=5, columnspan=3)

# Create button 'Add'
btn_add = Button(window, text="Add", command=btn_add_clicked)
btn_add.grid(row=5, column=5)
# Create button 'Delete'
btn_delete = Button(window, text="Delete", command=btn_delete_clicked)
btn_delete.grid(row=5, column=6)
# Create button 'Edit'
btn_edit = Button(window, text="Edit", command=btn_edit_clicked)
btn_edit.grid(row=5, column=7)

#### MAIN PROGRAM ####
window.mainloop()