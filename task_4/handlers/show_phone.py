from decorators.input_error_decorator import input_error


@input_error
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    name = args[0]
    return contacts[name]
