import datetime

import pytest

from contacts.models import Address, Contacts
from employees.models import Employees
from esn.models import ObjectModel
from products.models import Product

@pytest.fixture
def new_address_factory():
    def create_add(
            country: str,
            city: str,
            street: str,
            house_number: int,
    ):
        address = Address.objects.create(
            country=country,
            city=city,
            street=street,
            house_number=house_number
        )
        return address
    return create_add

@pytest.fixture
def new_contacts_factory(new_address):
    def create_add(
            email: str,
            address_id: new_address.id
    ):
        contacts = Contacts.objects.create(
            email=email,
            address_id=address_id,
        )
        return contacts
    return create_add

@pytest.fixture
def new_employee_factory(new_contacts):
    def create_add(
            name: str,
            address_id: new_contacts.id,
            created_at: datetime,
    ):
        employee = Employees.objects.create(
            name=name,
            address_id=address_id,
            created_at=created_at,
        )
        return employee
    return create_add

@pytest.fixture
def new_product_factory():
    def create_add(
            name: str,
            product_model: str,
            created_at: datetime,
    ):
        product = Product.objects.create(
            name=name,
            product_model=product_model,
            created_at=created_at,
        )
        return product
    return create_add

@pytest.fixture
def new_object_factory(new_contacts, new_product, new_employee):
    def create_add(
            name: str,
            debt: float,
            contacts_id: new_contacts.id,
            type: str,
            created_at: datetime
    ):
        object_model = ObjectModel.objects.create(
            name=name,
            debt=debt,
            contacts_id=contacts_id,
            type=type,
            created_at=created_at,
        )
        return object_model
    return create_add
@pytest.fixture()
def new_address(db, new_address_factory):
    return new_address_factory("BY", "Lox", "Loxovskay", 12)

@pytest.fixture()
def new_contacts(db, new_contacts_factory, new_address):
    return new_contacts_factory("test5@cpagen.biz", new_address.id)

@pytest.fixture()
def new_employee(db, new_employee_factory, new_contacts):
    return new_employee_factory("Den", new_contacts.id, datetime.datetime.now())

@pytest.fixture()
def new_product(db, new_product_factory):
    return new_product_factory("Test_product", "Snickers", datetime.datetime.now())

@pytest.fixture()
def new_object(db, new_object_factory, new_contacts, new_product, new_employee):
    return new_object_factory("Test_object", 400.0, new_contacts.id, "FA", datetime.datetime.now())

@pytest.mark.django_db
def test_new_address(new_address):
    print(new_address)
    assert  new_address.country == "BY"


@pytest.mark.django_db
def test_new_contacts(new_contacts):
    print(new_contacts)
    assert  new_contacts.email == "test5@cpagen.biz"

@pytest.mark.django_db
def test_new_employee(new_employee):
    print(new_employee)
    assert  new_employee.name == "Den"

@pytest.mark.django_db
def test_new_product(new_product):
    print(new_product)
    assert  new_product.name == "Test_product"

@pytest.mark.django_db
def test_new_object(new_object):
    print(new_object)
    assert  new_object.type == "FA"