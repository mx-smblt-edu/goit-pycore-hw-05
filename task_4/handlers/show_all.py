def show_all(contacts: dict[str, str]) -> str:
    if contacts:
        return "\n".join(format_contacts(contacts))
    else:
        return "No contacts found."


def format_contacts(contacts: dict[str, str]) -> list[str]:
    return [f"{name}: {phone}" for name, phone in contacts.items()]
