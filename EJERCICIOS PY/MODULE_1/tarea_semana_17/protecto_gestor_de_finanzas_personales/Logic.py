class Category():
    def __init__(self, name):
        self.name=name


class Transaction():
    def __init__(self, category, title, amount, type):
        self.category=category
        self.title=title
        self.amount=amount
        self.type=type


class FinanceController():
    def __init__(self):
        self.category=[]
        self.transaction=[]

    def get_all_movements_for_gui(self):
        list_to_gui=[]
        for trans in self.transaction:
            current_list=[]
            current_list.append(trans.category.name)
            current_list.append(trans.title)
            current_list.append(trans.amount)
            current_list.append(trans.type)
            list_to_gui.append(current_list)
        return list_to_gui

    def get_category_names(self):
        categories_name_for_gui=[]
        for cat in self.category:
            categories_name_for_gui.append(cat.name)
        return categories_name_for_gui

    def add_category(self, name):
        for cat in self.category:
            if cat.name == name:
                raise ValueError ("The category already exists")
        new_category=Category(name)
        self.category.append(new_category)
        

    def add_transaction(self, category_name, title, amount, type ):
        if amount<=0:
            raise ValueError ("amount most be a positive number")
        
        if type not in ("expense", "income"):
            raise ValueError("type most be expenses or income")
        
        found_category=None
        for cat in self.category:
            if cat.name==category_name:
                found_category=cat
                break
        if not found_category:
            raise ValueError ("category not found")
        else:
            my_transaction=Transaction(found_category, title, amount, type)
            self.transaction.append(my_transaction)
            
    def to_dict(self):
        categories_list=[
            {"name":cat.name}
            for cat in self.category 
        ]

        transaction_list=[
            {
                "category_name":trans.category.name,
                "title":trans.title,
                "amount":trans.amount,
                "type":trans.type,
            }
            for trans in self.transaction
        ]
        return {
            "categories":categories_list,
            "transactions":transaction_list
        }

    def get_total_balance(self):
        net_balance=0
        for trans in self.transaction:
            if trans.type== "expense":
                net_balance-=trans.amount
            elif trans.type=="income":
                net_balance+=trans.amount
        return net_balance