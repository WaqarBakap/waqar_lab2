import xml.etree.ElementTree as ET


tree = ET.parse("currency.xml")
root = tree.getroot()


names = []
values = []


for valute in root.findall("Valute"):
    name = valute.find("Name").text
    value = valute.find("Value").text


    value = float(value.replace(",", "."))

    names.append(name)
    values.append(value)


print("Names:", names)
print("Values:", values)
