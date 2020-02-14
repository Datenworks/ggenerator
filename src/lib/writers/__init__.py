def valid_dataframe(dataframe):
    """Validates if dataframe contain records

    Parameters:
     - dataframe - pandas.DataFrame: dataframe containing the records
    """
    return dataframe.shape[0] > 0
