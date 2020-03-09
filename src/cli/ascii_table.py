from tabulate import tabulate
from faker import Faker
from src.generators.datatypes import basic_generators, primitive_generators


def print_asciiTable():

    dataSet = {"datasets": {
        "NameSpace": [],
        "Type": [],
        "Sample": [],
        "Parameters": []}}
    # faking data
    fake = Faker('pt_BR')

    # creating the lists
    nameSpace_list = []
    type_list = []
    sample_list = []
    parameters_list = []
    # appending
    for x in primitive_generators:
        nameSpace_list.append("PrimitiveType")
        type_list.append(x)
        sample_list.append(fake.name())
    for x in basic_generators:
        nameSpace_list.append("BasicType")
        type_list.append(x)
    # setting values
    dataSet['datasets']["NameSpace"] = nameSpace_list
    dataSet['datasets']["Type"] = type_list
    dataSet['datasets']["Sample"] = sample_list

    nameSpace = dataSet["datasets"].get('NameSpace')
    type = dataSet["datasets"].get('Type')
    sample = dataSet["datasets"].get('Sample')
    parameters = dataSet["datasets"].get('Parameters')

    newDict = {
        "NameSpace": nameSpace,
        "Type": type,
        "Sample": sample,
        "Parameters": parameters}
    print("   ")
    print("   ")
    print("Available generators")
    print("   ")
    print(tabulate(newDict, headers=("keys"), tablefmt="grid"))
    print("   ")
    print("   ")
