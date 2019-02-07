from customer_service.model.errors import CustomerNotFound


class MockCustomerRepository:
    def __init__(self):
        self.customers = {}
        self.last_id = 0

    def store(self, customer):
        if customer.customer_id is None:
            self.last_id = self.last_id + 1
            customer.customer_id = self.last_id

        self.customers[customer.customer_id] = customer

    def update_surname(self, customer_id, new_surname):
        self.customers[customer_id].surname = new_surname

    def fetch_by_id(self, id):
        if id not in self.customers:
            raise CustomerNotFound()

        return self.customers[id]
