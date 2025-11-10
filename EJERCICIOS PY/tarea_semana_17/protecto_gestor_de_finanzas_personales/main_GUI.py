import FreeSimpleGUI as sg
from Logic import Category, Transaction, FinanceController
from persistence import save_data, load_data

class FinanceApp():
    def __init__(self):
        self.controller=load_data("finance.json")
        balance_frame = [
        [sg.Text("TOTAL BALANCE", font=("Helvetica", 12))],
        [sg.Text(f"${self.controller.get_total_balance():.2f}", 
                key='-BALANCE-', 
                font=("Helvetica", 20, "bold"), 
                text_color='dark green')]
    ]
        button_row=[sg.Button("ADD CATEGORY", key="-ADD_CAT_BTN-", size=(18, 1)),
            sg.Button("ADD INCOME", key="-ADD_INCOME_BTN-", size=(18, 1)),
            sg.Button("ADD EXPENSE", key="-ADD_EXPENSE_BTN-", size=(18, 1))]
        table_headings=["category", "title", "amount", "type"]
        movements_table=[
            [
                sg.Table(
                    values=[],
                    headings=table_headings,
                    key="-TABLE-",
                    auto_size_columns=True,
                    num_rows=15,
                )
            ]
        ]
        self.layout=[
            [sg.Frame("SUMMARY", balance_frame, relief=sg.RELIEF_GROOVE, border_width=2)],
            [sg.Frame("MOVEMENTS", movements_table, relief=sg.RELIEF_FLAT)],
            [sg.HorizontalSeparator()],
            [sg.Frame("ACTIONS", [button_row], relief=sg.RELIEF_FLAT)],
        ]
        self.window=sg.Window("PERSONAL FINANCE", self.layout, finalize=True)
        self.update_main_display()

    
    def run(self):
        while True:
            event, values =self.window.read()
            if event=="-ADD_CAT_BTN-":
                self.handle_add_category()
            elif event=="-ADD_INCOME_BTN-":
                self.handle_add_transaction("income")
            elif event=="-ADD_EXPENSE_BTN-":
                self.handle_add_transaction("expense")

            elif event==sg.WIN_CLOSED:
                save_data(self.controller, "finance.json")
                break
        self.window.close()


    def handle_add_transaction(self, transaction_type):
        list_categories=self.controller.get_category_names()
        if not list_categories:
            sg.popup_error("You must add at least one category", title="category error")
        new_transaction_layout=[
            [sg.Text(f"ADD {transaction_type.capitalize()}", font=("Helvetica", 16, "bold"))],
            [sg.Text('CATEGORY', size=(10, 1)),
             sg.Combo(list_categories, key='-CATEGORY-', default_value=list_categories[0] if list_categories else '', size=(25, 1))],
             [sg.Text("TITLE", size=(10, 1)),
              sg.Input(key="-TITLE-", size=(25, 1))],
              [sg.Text("monto", size=(10, 1)),
              sg.Input(key="-AMOUNT-", size=(25, 1))],
              [sg.Button("ADD", key="-ADD_TRANSACTION_OK-", size=(15, 1)),
               sg.Button("CANCEL", size=(15, 1))]
        ]
        transaction_window=sg.Window("NEW TRANSACTION", new_transaction_layout, finalize=True)
        while True:
            event, values =transaction_window.read()
            if event==sg.WIN_CLOSED or event=="CANCEL":
                break
            if event=="-ADD_TRANSACTION_OK-":
                category_name= values['-CATEGORY-']
                title = values['-TITLE-'].strip()
                amount_str = values['-AMOUNT-'].strip()
                if not category_name or not title or not amount_str:
                    sg.popup_error("All spaces must be completed.")
                    continue
                try:
                    amount=float(amount_str)
                except ValueError:
                    sg.popup_error ("The amount must be a valid number")
                    continue
                try:
                    self.controller.add_transaction(category_name, title, amount, transaction_type)
                    save_data(self.controller, "finance.json")
                    self.update_main_display() 
                    sg.popup_ok(f"{transaction_type.capitalize()} añadido con éxito!")
                    break 
                except ValueError as e:
                    sg.popup_error(f"Error al añadir transacción: {e}")
        
        
        transaction_window.close()







    def handle_add_category(self):
        category_name=sg.popup_get_text("Enter the name of the new category", title= "NEW CATEGORY")
        if category_name and category_name.strip():
            try:
                self.controller.add_category(category_name)
                save_data(self.controller, "finance.json")
                self.update_main_display()
            except ValueError as e:
                sg.popup_error(f"Error: {e}")

    def update_main_display(self):
        self.window['-BALANCE-'].update(value=f"${self.controller.get_total_balance():.2f}")
        self.window["-TABLE-"].update(values= self.controller.get_all_movements_for_gui())






if __name__ =="__main__":
    app=FinanceApp()
    app.run()
    

