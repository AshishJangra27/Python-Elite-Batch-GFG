import json
import time

fd = open("Record.json",'r')
js = fd.read()
fd.close()

dct = json.loads(js)

for i in dct.keys():
    print(i, dct[i])
    
print()

ui_prod = str(input("Enter Product ID   : "))
ui_qn   = int(input("Enter the Quantity : "))

if (ui_qn <= dct[ui_prod]['Qn']):
    print("-"*15)
    print("Name     :" , dct[ui_prod]['Name'])
    print("Price    :" , dct[ui_prod]['Price'])
    print("Quantity :" , ui_qn)
    print("-"*15)
    print("Total    :" ,dct[ui_prod]['Price'] * ui_qn)
    print("CGST     :" ,(dct[ui_prod]['Price'] * ui_qn)*.09)
    print("SGST     :" ,(dct[ui_prod]['Price'] * ui_qn)*.09)
    print("-"*15)
    print("Sub Total:" ,(dct[ui_prod]['Price'] * ui_qn) + (dct[ui_prod]['Price'] * ui_qn)*.18)
    print("-"*15)

    txn = dct[ui_prod]['Name']+","+str(dct[ui_prod]['Price'])+","+str(ui_qn)+","+str((dct[ui_prod]['Price'] * ui_qn) + (dct[ui_prod]['Price'] * ui_qn)*.18)+","+time.ctime()+"\n"


    dct[ui_prod]["Qn"] = dct[ui_prod]["Qn"] - ui_qn

else:
    print()
    print("We're only having",dct[ui_prod]['Qn'],"quantity so bill is generated for the same.")
    print("-"*15)
    print("Name     :" , dct[ui_prod]['Name'])
    print("Price    :" ,dct[ui_prod]['Price'])
    print("Quantity :" ,dct[ui_prod]['Qn'])
    print("-"*15)
    print("Total    :" ,dct[ui_prod]['Price'] * dct[ui_prod]['Qn'])
    print("CGST     :" ,(dct[ui_prod]['Price'] * dct[ui_prod]['Qn'])*.09)
    print("SGST     :" ,(dct[ui_prod]['Price'] * dct[ui_prod]['Qn'])*.09)
    print("-"*15)
    print("Sub Total:" ,(dct[ui_prod]['Price'] * dct[ui_prod]['Qn']) + (dct[ui_prod]['Price'] * dct[ui_prod]['Qn'])*.18)
    print("-"*15)

    txn = dct[ui_prod]['Name']+","+str(dct[ui_prod]['Price'])+","+str(dct[ui_prod]['Qn'])+","+str((dct[ui_prod]['Price'] * dct[ui_prod]['Qn']) + (dct[ui_prod]['Price'] * dct[ui_prod]['Qn'])*.18)+","+time.ctime()+"\n"

    dct[ui_prod]["Qn"] = 0



js = json.dumps(dct)

fd = open("Record.json",'w')
fd.write(js)
fd.close()


fd = open('Sales.txt','a')
fd.write(txn)
fd.close()




