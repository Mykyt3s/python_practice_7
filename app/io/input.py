import pandas as pd


def console_input() -> str:
    """
    get input text from the console
    """
    text = input("Write some text: ")
    return text


def read_file_builtin(file_path) -> str:
    """
    Reads file using builtin utils
    :param file_path: path to the file
    :return: file content
    """
    with open(file_path, "r") as file:
        return file.read()


def read_file_pandas(file_path) -> str:
    """
    Reads file using pandas
    :param file_path: path to the file
    :return: file content
    """
    return pd.read_csv(file_path).to_string(index=False)
