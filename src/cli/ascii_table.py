from tabulate import tabulate
# from faker import Faker
from src.generators.datatypes import get_generators_map
import inspect

generators_map = get_generators_map()

dataSet = {
        "NameSpace": [],
        "Type": [],
        "Sample": [],
        "Parameters": []}


def asciiTable_print():
    for datatype_name, datatype in generators_map.items():
        typeName = datatype_name
        dataSet['Type'].append(typeName)
        gen = datatype['type']
        namespace = gen.namespace
        dataSet['NameSpace'].append(namespace)
        sample = str(gen.sample())[:15] + "..."
        dataSet['Sample'].append(sample)
        arguments = inspect.getfullargspec(gen).annotations
        parsed_args = []
        for arg, dtype in arguments.items():
            parsed_args.append((arg, dtype.__name__))
        dataSet['Parameters'].append(parsed_args)

    print("   ")
    print("   ")
    print("Available generators")
    print("   ")
    print(tabulate(dataSet, headers=("keys"), tablefmt="grid"))
    print("   ")
    print("   ")
