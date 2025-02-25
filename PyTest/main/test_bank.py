import pytest
from bank import BankAccount


@pytest.fixture
def account():
    return BankAccount("John Doe", 1000)


@pytest.fixture
def recipient_account():
    return BankAccount("Alice Smith", 500)


def test_deposit(account):
    account.deposit(500)
    assert account.get_balance() == 1500


def test_withdraw(account):
    account.withdraw(400)
    assert account.get_balance() == 600


def test_overdraft_not_allowed(account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(2000)


def test_negative_deposit(account):
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        account.deposit(-100)


def test_negative_withdraw(account):
    with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
        account.withdraw(-50)


def test_transfer(account ,recipient_account):
    account.transfer(300, recipient_account)
    assert account.get_balance() == 700
    assert recipient_account.get_balance() == 800


def test_insufficient_funds_transfer(account, recipient_account):
    with pytest.raises(ValueError, match="Insufficient funds for transfer"):
        account.transfer(5000, recipient_account)
