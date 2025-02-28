import pytest
from bank_account import BankAccount


@pytest.fixture
def account():
    return BankAccount("12345", 1000)


@pytest.fixture
def recipient_account():
    return BankAccount("67890", 2000)


def test_deposit(account):
    account.deposit(3000)
    assert account.get_balance() == 4000

    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        account.deposit(-1000)


def test_withdraw(account):
    account.withdraw(1000)
    assert account.get_balance() == 0

    with pytest.raises(ValueError, match="Insufficient balance."):
        account.withdraw(5000)

    with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
        account.withdraw(-100)


def test_transfer(account, recipient_account):
    account.transfer(500, recipient_account)
    assert account.get_balance() == 500
    assert recipient_account.get_balance() == 2500

    with pytest.raises(ValueError, match="Insufficient balance."):
        account.transfer(2000, recipient_account)

    with pytest.raises(TypeError, match="Recipient must be BankAccount instance"):
        account.transfer(100, "Not an account")


def test_get_balance(account):
    assert account.get_balance() == 1000
