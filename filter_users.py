import json


def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"] == email]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == int(age)]

    for user in filtered_users:
        print(user)


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if
                      user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def get_users_choice():
    filter_option = (
        input(
            "What would you like to filter by? (Valid input: 'name', "
            "'age' and 'email'): "
        )
        .strip()
        .lower()
    )
    return filter_option


FILTER_ACTIONS = {
    "name": filter_users_by_name,
    "age": filter_users_by_age,
    "email": filter_users_by_email,
}


def main():
    users_filter_option = get_users_choice()
    if users_filter_option in FILTER_ACTIONS:
        action = FILTER_ACTIONS.get(users_filter_option)
        item_to_search = input(
            f"Enter {users_filter_option} to filter users: " f""
        ).strip()
        action(item_to_search)
    else:
        print("Filtering by that option is not supported.")


if __name__ == "__main__":
    main()
