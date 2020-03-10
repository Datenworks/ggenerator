from tabulate import tabulate
# from faker import Faker
from src.generators.datatypes import basic_generators, primitive_generators
from src.generators.datatypes import generators_map
from src.cli.ascii_table_fixtures import typeSamples
import inspect

dataSet = {
        "NameSpace": [],
        "Type": [],
        "Sample": [],
        "Parameters": []}


def teste():
    for datatype_name, datatype in generators_map.items():
        typeName = datatype_name
        dataSet['Type'].append(typeName)
        gen = datatype['type']
        namespace = gen.namespace
        dataSet['NameSpace'].append(namespace)
        sample = gen.sample()
        dataSet['Sample'].append(sample)
        arguments = inspect.getfullargspec(gen).annotations
        parsed_args = []
        for arg, dtype in arguments.items():
            parsed_args.append((arg, dtype.__name__))
        dataSet['Parameters'].append(parsed_args)

    print(tabulate(dataSet, headers=("keys"), tablefmt="grid"))


def print_asciiTable():

    dataSet = {"datasets": {
        "NameSpace": [],
        "Type": [],
        "Sample": [],
        "Parameters": []}}
    # faking data
    # fake = Faker('pt_BR')

    # creating the lists
    nameSpace_list = []
    type_list = []
    sample_list = []
    parameters_list = []
    # appending
    for x in primitive_generators:
        nameSpace_list.append("PrimitiveType")
        type_list.append(x)
        sample_list.append(typeSamples(x))
        parameters_list.append(
            primitive_generators[x]['generator'].get('arguments'))
    for x in basic_generators:
        nameSpace_list.append("BasicType")
        type_list.append(x)
        sample_list.append(typeSamples(x))
        parameters_list.append(
            basic_generators[x]['generator'].get('arguments'))
    # setting values
    dataSet['datasets']["NameSpace"] = nameSpace_list
    dataSet['datasets']["Type"] = type_list
    dataSet['datasets']["Sample"] = sample_list
    dataSet['datasets']["Parameters"] = parameters_list

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
