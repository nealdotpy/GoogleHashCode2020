'''
GOOGLE HASH CODE
SHA-nel Team Solution
ROUND 1 Problem
'''

import numpy as np
import itertools as it
import pandas as pd
from functools import wraps
import time

'''
Wrapper function to time these calculations. Mainly for testing and curiosity.
'''
def timer(func):
    # Prints runtime of function 
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        print(f'Finished {func.__name__} in {round(end-start, 4)} seconds.')
        return value
    return wrapper_timer

def open_data(dataset):
    with open('datasets/{}'.format(dataset), 'r') as file:
        # read data and remove new line characters and map to integer values
        total_books, num_libs, total_days = list(map(int, file.readline()[:-1].split(' ')))
        book_scores = list(map(int, file.readline()[:-1].split(' '))) # map these to tuples with book id?
        library_data = {}
        for i in range(num_libs):
            num_books, signup, books_per_day = list(map(int, file.readline()[:-1].split(' ')))
            books = list(map(int, file.readline()[:-1].split(' '))) # list of book ids available in that library
            library_data['{}'.format(i)] = {'num_books' : num_books,
                                            'signup' : signup,
                                            'books_per_day' : books_per_day,
                                            'books' : books,
                                            'opt_days' : signup + (books / books_per_day)
                                            }

        return {'total_books' : total_books, 
                'num_libs' : num_libs, 
                'total_days' : total_days, 
                'book_scores' : book_scores, 
                'library_data': library_data}


def solution_naive(dataset):
    data = open_data(dataset)
    library_data = data['library_data']
    print(data)


solution_naive('dataset_A.txt')