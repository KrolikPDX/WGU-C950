class Package:
    def __str__(self):
        return "Package #" + self.id

    def __init__(self, package_id, delivery_address, weight, deadline):
        self.id = package_id
        self.delivery_address = delivery_address
        self.weight = weight
        self.deadline = deadline
        self.priority = None
        self.left_hub = None
        self.delivered_at = None
        self.truck = None

    def __hash__(self):
        return hash(self.id)

