import random


PHONE_NUMBER_LIST = {"Friend 0", "Friend 1", "Friend 2", "Friend 3", "Friend 4", "Friend 5"}


def valid_pairs(pairs_to_validate: list[tuple[str, str]]) -> bool:
    valid = True

    if len(pairs_to_validate) == 0:
        return False

    for pair_to_validate in pairs_to_validate:
        if pair_to_validate[0] == pair_to_validate[1]:
            valid = False
    return valid


def create_pairs() -> list[tuple[str, str]]:
    new_pairs: list[tuple[str, str]] = []
    used_numbers = set()

    for entry in PHONE_NUMBER_LIST:
        possible_pairs = PHONE_NUMBER_LIST.copy()
        possible_pairs.remove(entry)
        possible_pairs.difference_update(used_numbers)

        if len(possible_pairs) == 0:
            # return invalid list of pairs to trigger a re-pair. This might happen in the corner case where the one
            # remaining entry to pair hasn't been matched before and only has itself to match with.
            return []

        possible_matches = list(possible_pairs)
        selected_match = possible_matches[random.randint(0, len(possible_matches) -1)]

        used_numbers.add(selected_match)
        list.append(new_pairs, (entry, selected_match))

    return new_pairs


if __name__ == '__main__':
    pairs = []

    while not valid_pairs(pairs):
        pairs = create_pairs()

    for pair in pairs:
        print(pair)
