class Comanda:
    def __init__(self, order, client, amount, delivery) -> None:
        self.order = order
        self.client = client
        self.amount = int(amount)
        
        if (str(delivery) in 'Sisi' or (type(delivery) is bool and delivery)):
            self.delivery = True
        else:
            self.delivery = False

    def applyDiscount (self):
        if (self.amount >= 6000):
            if (self.delivery):
                self.amount = int(self.amount * 0.95)
            else:
                self.amount = int(self.amount * 0.9)

    def getAttributesAsDict (self):
        return {
            'order' : self.order,
            'client' : self.client,
            'amount' : self.amount,
            'delivery' : self.delivery
        }