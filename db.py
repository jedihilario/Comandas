import json

class Query:
    def selectAll ():
        res = []

        with open('db.json') as db:
            data = json.load(db)

            for com in data:
                values = com.values()
                res.append(values)

        return res
    
    def insert (data):
        actual_data = Query.selectAll()

        actual_data.append(data)

        with open('db.json', 'w') as db:
            json.dump(actual_data, db, indent=4)

    def deleteDB():
        with open('db.json', 'w') as db:
            json.dump([], db, indent=4)

    def selectDelivery ():
        response = []

        with open('db.json') as db:
            data = json.load(db)

            for comanda in data:
                if (comanda['delivery']):
                    values = comanda.values()
                    response.append(values)

        return response
