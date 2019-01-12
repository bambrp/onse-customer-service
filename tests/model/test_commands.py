import pytest

from customer_service.model import commands
from customer_service.model.customer import Customer
from customer_service.model.errors import CustomerNotFound


def test_get_customer_when_customer_does_not_exist(customer_repository):
    with pytest.raises(CustomerNotFound):
        commands.get_customer(customer_id=99999,
                              customer_repository=customer_repository)


def test_get_customer(customer_repository):
    customer = Customer(customer_id=1234, first_name='Gene', surname='Kim')
    customer_repository.store(customer)

    result = commands.get_customer(customer_id=1234,
                                   customer_repository=customer_repository)

    assert result is customer
