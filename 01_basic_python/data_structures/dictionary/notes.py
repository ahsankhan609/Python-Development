"""
- dictionary is a list of key:value pairs
"""
from psutil import users

# create empty dictionary
people: dict = {}

# user dictionary:
user: dict[str, int | str] = {
    'name': 'ahmed',
    'age': 22,
    'city': 'NY',
    'country': 'USA',
}

if __name__ == '__main__':
    # accessing user with name key
    user_name = user['name']
    print(user_name)

    # display all keys in dictionary
    print(user.keys())

    # display all values in dictionary
    print(user.values())

    # updating value in dictionary
    user['city'] = 'New York'
    print(user['city'])

    # update dictionary with new key:value
    user.update({'zip_code': 54789})
    print(user)

    # set default message if no key exists in dictionary
    print(user.setdefault('XXX', 'No Key available'))
