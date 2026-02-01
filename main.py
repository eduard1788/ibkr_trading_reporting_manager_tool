import customtkinter
from widgets import MainFrame
from behavior import IBKROrders
import ib_insync


if __name__ == "__main__":
    #########################################
    ## Request number of columns to client ##
    #########################################

    root = customtkinter.CTk()
    root.geometry("500x800")

    input_dialog = customtkinter.CTkInputDialog(text="Enter the number of columns for the grid layout", title="Grid")
    column_number = input_dialog.get_input()

    if column_number is None or not column_number.isdigit() or int(column_number) < 1:
        raise ValueError("Invalid number of columns entered.")
    column_number = int(column_number)

    frame = MainFrame(master=root, columns=column_number)
    orders = IBKROrders(frame)

    frame.callbacks = {
        "stop": orders.stop,
        "limit": orders.limit,
        "market": orders.market,
        "modify": orders.modify,
        "cancel": orders.cancel,
    }

    root.mainloop()