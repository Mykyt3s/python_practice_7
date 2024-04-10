from app.io import input, output


def main():
    pass


if __name__ == "__main__":
    text_input_1 = input.console_input()
    output.file_output_builtin("./console_output.txt", text_input_1)
    output.console_output(text_input_1)

    text_input_2 = input.read_file_builtin("./builtin_input.txt")
    output.file_output_builtin("./builtin_output.txt", text_input_2)
    output.console_output(text_input_2)

    text_input_3 = input.read_file_pandas("./pandas_input.txt")
    output.file_output_builtin("./pandas_output.txt", text_input_3)
    output.console_output(text_input_3)
