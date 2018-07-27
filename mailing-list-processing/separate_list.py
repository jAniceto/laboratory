import csv
import pprint
from clean_list import get_list, save_list_as_csv


def divide_list(large_list, n):
    """ Yield successive n-sized chunks from large_list. """
    for i in range(0, len(large_list), n):
        yield large_list[i:i + n]


def save_all_lists(list_of_lists):
    for i, small_list in enumerate(list_of_lists):
        save_list_as_csv('divided/new_list_{}.csv'.format(i), small_list)


def main():
    # Load list
    the_list = get_list('contacts/new_list.txt')

    sm_lists = list(divide_list(the_list, 250))

    save_all_lists(sm_lists)
    


if __name__ == "__main__":
    main()
