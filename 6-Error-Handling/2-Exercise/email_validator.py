import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MustContainOnlyOneAtSymbolError(Exception):
    pass


class NameInvalidSymbolsError(Exception):
    pass


class NameMustStartWithLetter(Exception):
    pass


valid_domains = [".com", ".bg", ".org", ".net"]
username_pattern = r"(^[\w+\.]+)"
domain_pattern = r"(\.[a-z]+)$"

email = input()

while email != "End":
    try:
        provided_username = email.split("@")[0]
        current_domain = re.search(domain_pattern, email)
        current_name = re.search(username_pattern, email)

        if current_name.group() != provided_username:
            raise NameInvalidSymbolsError("The name must contain only letters, numbers and an underscore")

        if not provided_username[0].isalpha():
            raise NameMustStartWithLetter("The name must start with a letter!")

        if len(current_name.group()) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")

        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")

        if email.count("@") > 1:
            raise MustContainOnlyOneAtSymbolError("Email must contain only one '@' symbol!")

        if current_domain.group() not in valid_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    except (IndexError, AttributeError):    # in case we are out of indexes or when there is no group() found with regex
        print("Invalid email")

    else:
        print("Email is valid")

    email = input()