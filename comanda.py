class Comanda:
    def __init__(self, order, client, amount, delivery) -> None:
        self.order = order
        self.client = client.lower()
        self.amount = amount
        
        if (delivery in 'Ss'):
            self.delivery = True
        else:
            self.delivery = False

    def getAttributesAsDict (self):
        return {
            'order' : self.order,
            'client' : self.client,
            'amount' : self.amount,
            'delivery' : self.delivery
        }