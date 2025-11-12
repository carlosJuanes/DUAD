
import pytest
from Logic import Category, Transaction, FinanceController
@pytest.fixture
def controller():
    ctrl=FinanceController()
    ctrl.category=[]
    ctrl.transaction=[]
    return ctrl

def test_1_transaction_initialization():
    #Arrange
    category="rent"
    title="lease"
    amount=1200.00
    type="expense"
    #Act
    t=Transaction(category, title, amount, type)
    #Assert
    assert t.category==category
    assert t.title==title
    assert t.amount==amount
    assert t.type==type

def test_2_get_category_names(controller):
    #Arrange
    controller.add_category("fast food")
    controller.add_category("transport")
    controller.add_category("grocery")
    #Act
    expected_names=["fast food", "transport", "grocery"]
    categories_name=controller.get_category_names()
    #Assert
    assert expected_names==categories_name

def test_3_add_expense_updates_balance(controller):
    #Arrange
    controller.add_category("food")
    expense_amount=50.00
    #Act
    controller.add_transaction("food", "coffee and bread", expense_amount, "expense")
    expected_balance=-expense_amount
    #Assert
    actual_balance=controller.get_total_balance()
    assert actual_balance==expected_balance

def test_4_balance_mixed_transactions(controller):
    #Arrange
    controller.add_category("salary")
    controller.add_category("entertainment")
    income=100
    expense=40
    expected_balance=60.00
    #ct
    controller.add_transaction("salary", "wage", income, "income")
    controller.add_transaction("entertainment", "movie", expense, "expense")
    #Assert
    actual_balance=controller.get_total_balance()
    assert actual_balance==expected_balance

def test_5_add_transaction_nonexistent_category_error(controller):
    #Arrange
    non_existent_category="travel"
    #Act, Assert
    with pytest.raises(ValueError):
        controller.add_transaction(non_existent_category, "spain", 100.00, "expense")

def test_6_add_categories(controller):
    #Arrange
    controller.add_category("food")
    controller.add_category("transportation")
    #Act
    len_categories_expected=2
    number_of_categories=len(controller.category)
    #Assert
    assert len_categories_expected==number_of_categories

def test_7_add_transaction_with_negative_amount(controller):
    #Arrange
    controller.add_category("sales")
    negative_amount=-100
    #Act, Assert
    with pytest.raises(ValueError):
        controller.add_transaction("sales", "paint", negative_amount, "income")

def test_8_add_category_duplicate(controller):
    #Arrange
    controller.add_category("travel")
    #Act, Assert
    with pytest.raises(ValueError):
        controller.add_category("travel")