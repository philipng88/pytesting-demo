import pytest 
from wallet import Wallet, InsufficientAmount

# def test_default_initial_amount(): 
#     wallet = Wallet()
#     assert wallet.balance == 0 

# def test_setting_initial_amount():
#     wallet = Wallet(100)
#     assert wallet.balance == 100 

# def test_wallet_add_cash():
#     wallet = Wallet(10)
#     wallet.add_cash(90)
#     assert wallet.balance == 100

# def test_wallet_spend_cash(): 
#     wallet = Wallet(20)
#     wallet.spend_cash(10)
#     assert wallet.balance == 10 

# def test_wallet_spend_cash_raise_exception():
#     wallet = Wallet()
#     with pytest.raises(InsufficientAmount):
#         wallet.spend_cash(100) 

# @pytest.fixture
# def empty_wallet():
#     # Returns a wallet instance with a zero balance
#     return Wallet()

# @pytest.fixture
# def wallet():
#     # Returns a wallet instance with a balance of twenty dollars
#     return Wallet(20) 

# def test_default_initial_amount(empty_wallet):
#     assert empty_wallet.balance == 0

# def test_setting_initial_amount(wallet):
#     assert wallet.balance == 20 

# def test_wallet_add_cash(wallet):
#     wallet.add_cash(80)
#     assert wallet.balance == 100 

# def test_wallet_spend_cash(wallet):
#     wallet.spend_cash(10)
#     assert wallet.balance == 10 

@pytest.fixture
def my_wallet():
    return Wallet()

@pytest.mark.parametrize("earned, spent, expected", [
    (30, 10, 20),
    (20, 2, 18)
])

def test_transactions(my_wallet, earned, spent, expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected 