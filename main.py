import tkinter as tk

todo_list = []

root = tk.Tk()
root.geometry("600x400")

listbox = tk.Listbox(root)
listbox.pack()
listbox.config(height=10)
listbox.pack(fill="both", expand=True)


def add_item():
    item = entry.get()
    item = " - " + item
    todo_list.append(item)
    listbox.insert("end", item)
    entry.delete(0, "end")

    with open("todo_list.txt", "w") as f:
        for item in todo_list:
            f.write(item + "\n")

add_button = tk.Button(root, text="Add", command=add_item, relief="groove", bg="light green", font=("Arial", 13))
add_button.pack()

entry = tk.Entry(root)
entry.pack()

root.bind("<Return>", add_item)

def delete_item():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        item = todo_list[index]
        todo_list.remove(item)
        listbox.delete(index)

    with open("todo_list.txt", "w") as f:
        for item in todo_list:
            f.write(item + "\n")

root.bind("<Delete>", delete_item)

delete_button = tk.Button(root, text="Delete", command=delete_item, relief="groove", bg="red", font=("Arial", 13))
delete_button.pack()

def main():
    try:
        with open("todo_list.txt", "r") as f:
            for item in f:
                item = item.strip()
                todo_list.append(item)
                listbox.insert("end", item)
    except FileNotFoundError:
        pass

    root.mainloop()

if __name__ == "__main__":
    main()

root.mainloop()
