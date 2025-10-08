from decorators.input_error_decorator import input_error


@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    name, phone = args
    if name in contacts:
        return "Contact already exists. Using 'change' command to change it."
    contacts[name] = phone
    return "Contact added."
