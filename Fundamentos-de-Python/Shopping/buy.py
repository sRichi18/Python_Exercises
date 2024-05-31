path = "Buy.txt"

def file(parameter_function):

    def run_function(**kwargs):
        with open(path, "a+") as fl:
            return parameter_function(fl, **kwargs)

    return run_function

@file
def Add_Buy(obj_fl, **kwargs):
    name = kwargs["name_item"]
    amnt = kwargs["amount"]
    prec_unit = kwargs["prec_unit"]
    total = kwargs["amount"] * kwargs["prec_unit"]
    row = "{},{},{},{}\n".format(name,amnt,prec_unit,total)
    obj_fl.write(row)

#data = {"name_item": "Rags", "amount": 7, "prec_unit": 2}
#Add_Buy(**data)

@file
def Items_List(obj_fl):
    obj_fl.seek(0, 0)
    print(obj_fl.read())

Items_List()

@file
def Get_Items(obj_fl):
    obj_fl.seek(0, 0)
    return obj_fl.readlines()

#result = Get_Items()
#print(result)


def Total_Sales():
    total_sales = 0
    for item in Get_Items():
        item = item.strip("\n")
        total_item = item.split(",")[3]
        total_sales = total_sales + int(total_item)

    print("The total sales for the day is: " + str(total_sales))
    
#Total_Sales()

def Total_Items_Sold():
    total_amount = 0
    for item in Get_Items():
        item = item.strip("\n")
        total_item = item.split(",")[1]
        total_amount = total_amount + int(total_item)

    print(str(total_amount) + " items were sold")

Total_Items_Sold()
