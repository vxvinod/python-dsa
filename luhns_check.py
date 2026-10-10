
def luhn_valid(number):
    total = 0
    if not number.isdigit():
        return False
    
    for i, ch in enumerate(reversed(number)):
        d = int(ch)
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0

class CardProcessor:

    def __init__(self):
        self.cust_trans = {}

    def process(self, line):
        try:
            info = line.split(" ")
            action, name = info[0], info[1]
            if action.lower() == "add":
                print("inside add")
                self.add_card_to_customer(name, info[2], int(info[3].lstrip("$")))
            elif action.lower() == "charge":
                self.charge_to_customer(name, int(info[2].lstrip("$")))
            elif action.lower() == "credit":
                self.credit_to_customer(name, int(info[2].lstrip("$")))
            else:
                raise "unkown action"
        except Exception as e:
            print(f"Exception error occured - {e}")

    def add_card_to_customer(self, name, card_no, limit):
        if name is None or card_no is None or limit is None:
            raise "name or card no or limit is none"
        is_card_valid = luhn_valid(card_no)
        print("came down")
        if name not in self.cust_trans:
            self.cust_trans[name] = {"limit": limit, "valid_card": is_card_valid,
                                    "card_no": card_no, "balance": 0 }
            print(self.cust_trans)
        else:
            raise ValueError("card is already added")
        
    def charge_to_customer(self, name, amount):
        if name is None or amount is None:
            raise "name or amount is none"
        print(f"charge name-{name}")
        if name in self.cust_trans:
            if self.cust_trans[name]["valid_card"] == False:
                return
            balance = self.cust_trans[name]["balance"]
            limit = self.cust_trans[name]["limit"]
            print(f"{name}--balance-{balance}-limit-{limit}")
            if balance + amount <= limit:
                self.cust_trans[name]["balance"] += amount
            else:
                return
    
    def credit_to_customer(self, name, amount):
        if self.cust_trans[name]["valid_card"] == False:
                    return
        if name in self.cust_trans:
            balance = self.cust_trans[name]["balance"]
            self.cust_trans[name]["balance"] -= amount

    def summary(self):

        for name, info in self.cust_trans.items():
            print(f"#{name}: ${info["balance"]}")    

cp = CardProcessor()
cp.process("Add Tom 4111111111111111 $1000")
cp.process("Charge Tom $500")
cp.process("Credit Tom $100")
cp.summary()