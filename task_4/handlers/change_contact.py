from decorators.input_error_decorator import input_error


@input_error
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError
