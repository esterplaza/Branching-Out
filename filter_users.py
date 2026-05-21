import json


def print_filtered_users(filtered_users):
    """prints the users that have been found through the filter"""
    if len(filtered_users) == 0:
        print("No user has been found")
    else:
        for user in filtered_users:
            print(user)


def open_file(filename):
    """opens filname and returns the opened file to work with"""
    with open(filename, "r") as file:
        return json.load(file)


def filter_users_by_email(email, users):
    """returns a list of users with a given email"""
    return [user for user in users if user["email"] == email]


def filter_users_by_age(age, users):
    """returns a list of users with a given age"""
    return [user for user in users if user["age"] == int(age)]


def filter_users_by_name(name, users):
    """returns a list of users with a given name"""
    return [user for user in users if user["name"].lower() == name.lower()]


def get_users_choice():
    """asks the user what filter does he wants to use and returns his choice"""
    filter_option = (
        input(
            "What would you like to filter by? (Valid input: 'name', "
            "'age' and 'email'): "
        )
        .strip()
        .lower()
    )
    return filter_option


def is_item_to_search_valid(filter_option, item_to_search):
    """checks if the item to search is valid"""
    if filter_option == "age" and not item_to_search.isdigit():
        return False, "The age should be a number"
    if (
            filter_option == "email"
            and "@" not in item_to_search
            and "." not in item_to_search
    ):
        return False, "The email should contain an @ and a ."
    if filter_option == "name" and item_to_search.isdigit():
        return False, "The name should not be a number"
    return True, ""


FILTER_ACTIONS = {
    "name": filter_users_by_name,
    "age": filter_users_by_age,
    "email": filter_users_by_email,
}


def main():
    users = open_file("users.json")
    users_filter_option = get_users_choice()
    if users_filter_option in FILTER_ACTIONS:
        action = FILTER_ACTIONS.get(users_filter_option)
        while True:
            item_to_search = input(
                f"Enter {users_filter_option} to filter users: "
            ).strip()
            valid, user_message = is_item_to_search_valid(
                users_filter_option, item_to_search
            )
            if valid:
                filtered_users = action(item_to_search, users)
                print_filtered_users(filtered_users)
                break
            else:
                print(f"The input data is not valid. {user_message}")
    else:
        print("Filtering by that option is not supported.")


if __name__ == "__main__":
    main()
