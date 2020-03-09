from tabulate import tabulate


def print_asciiTable(dataSet):
    for key in dataSet.keys():
        # id = key
        nameSpace = dataSet[key].get('fields')
        type = dataSet[key].get('size')
        sample = dataSet[key].get('format')
        parameters = dataSet[key].get('serializers')

        newDict = {
            "NameSpace": nameSpace,
            "Type": type,
            "Sample": sample,
            "Parameters": parameters}
    print(tabulate(newDict, headers=("keys")))
