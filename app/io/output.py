

def console_output(text):
    """
    Output text to the console
    :param text: given text
    """
    print(text)


def file_output_builtin(file_path, text):
    """
    Output text to the file using builtin utils
    :param text: given text
    :param file_path: the path to file
    """
    with open(file_path, "w") as file:
        file.write(text)
