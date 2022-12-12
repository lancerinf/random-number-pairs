import random


PHONE_NUMBER_LIST = {"Friend 0", "Friend 1", "Friend 2", "Friend 3", "Friend 4", "Friend 5"}


def valid_pairs(pairs: list[tuple[str, str]]) -> bool:
    valid = True

    if len(pairs) == 0:
        return False

    for pair in pairs:
        if pair[0] == pair[1]:
            valid = False
    return valid


def create_pairs() -> list[tuple[str, str]]:
    used_numbers = set()
    number_pairs: list[tuple[str, str]] = []

    for entry in PHONE_NUMBER_LIST:
        possible_pairs = PHONE_NUMBER_LIST.copy()
        possible_list = []

        possible_pairs.remove(entry)
        possible_pairs.difference_update(used_numbers)

        if len(possible_pairs) == 0:
            # add invalid entry to trigger a re-do
            list.append(number_pairs, (entry, entry))
            return number_pairs

        for num in possible_pairs:
            list.append(possible_list, num)

        selected_num = possible_list[random.randint(0, len(possible_list) -1)]

        used_numbers.add(selected_num)
        list.append(number_pairs, (entry, selected_num))

    return number_pairs


if __name__ == '__main__':
    pairs = []

    while not valid_pairs(pairs):
        pairs = create_pairs()

    for pair in pairs:
        print(pair)
