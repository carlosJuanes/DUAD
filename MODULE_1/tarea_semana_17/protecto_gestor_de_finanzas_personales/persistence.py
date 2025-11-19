import json
from Logic import FinanceController, Category, Transaction 

def save_data(controller, filename):
    data_to_save=controller.to_dict()

    try:
        with open(filename, "w") as file:
            json.dump(data_to_save, file, indent=4)
    except IOError as e:
        print("Error writing to data {file}:{e}")


def load_data(filename):
    try:
        with open(filename, "r") as file:
            python_data=json.load(file)
            controller=FinanceController()
            for cat in python_data["categories"]:
                name=cat["name"]
                category=Category(name)
                controller.category.append(category)
            for trans in python_data["transactions"]:
                for cate in controller.category:
                    if trans["category_name"]==cate.name:
                        new_transaction=Transaction(
                            cate,
                            trans["title"],
                            float(trans["amount"]),
                            trans["type"]
                        )
                        controller.transaction.append(new_transaction)
                        break
            return controller
    except FileNotFoundError:
        return FinanceController()

