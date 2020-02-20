'''
GOOGLE HASH CODE
SHA-nel Team Solution
ROUND 1 Problem
'''

import numpy as np
import math
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
        library_data = []

        def book_score(book_id):
            return book_scores[book_id]

        def score_lib(books, scores):
            score = 0
            for book in books: # O(B), where b is total number of books
                score += scores[book]

            return score


        for i in range(num_libs):
            num_books, signup, books_per_day = list(map(int, file.readline()[:-1].split(' ')))
            books = sorted(list(map(int, file.readline()[:-1].split(' '))), key=book_score, reverse=True) # list of book ids available in that library
            worth = score_lib(books, book_scores)
            library_data.append({'lib_id' : i,
                                'num_books' : num_books,
                                'signup' : signup,
                                'books_per_day' : books_per_day,
                                'books' : books,
                                'days_to_finish' : signup + math.ceil((num_books / books_per_day)),
                                'worth' : worth,
                                'score' : round(books_per_day / signup, 6)
                                })

        return {'total_books' : total_books, 
                'num_libs' : num_libs, 
                'total_days' : total_days, 
                'book_scores' : book_scores, 
                'library_data': library_data}


def solution_naive(dataset):
    #file = open('solutionA.txt', 'a');

    def score(elem):
        return elem['score']


    '''
    if you're reading this... this code sucks i know... but i was 2 hours late to start :(
    '''


    output = []
    data = open_data(dataset)
    #df = pd.DataFrame(data)
    library_data = sorted(data['library_data'], key=score, reverse=True) # sorted by score (a ratio)
    #print(data)
    days_left = data['total_days']
    #print('DTF: {}, DL: {}'.format(library_data[55]['days_to_finish'], days_left))
    libs_to_use = 0
    i = 0
    FACTOR = 4
    delta = (library_data[0]['days_to_finish'] - ((library_data[0]['num_books']//FACTOR) // library_data[0]['books_per_day']))
    while (days_left - delta > 0 or i < len(library_data)-2):
        num_books = library_data[i]['num_books']
        print('sign up library<{}>'.format(library_data[i]['lib_id']))
        print('sending books: {}'.format(library_data[i]['books'][:(num_books//FACTOR)]))

        if (num_books // FACTOR > 0):
            output.append('{} {}\n{}'.format(library_data[i]['lib_id'], 
                                            num_books // FACTOR,
                                            ' '.join(map(str, library_data[i]['books'][:(num_books//FACTOR)]))
                                            ))
        else:
            libs_to_use -= 1

        # CONTROLS
        days_left -= delta
        i += 1
        delta = (library_data[i]['days_to_finish'] - ((num_books//FACTOR) // library_data[i]['books_per_day']))
        print(days_left)
        libs_to_use += 1

    print(output)

    with open('solution_{}.txt'.format(dataset[-5]), 'w') as file:
            file.write('')

    with open('solution_{}.txt'.format(dataset[-5]), 'a') as file:
            file.write('{}\n'.format(libs_to_use))
    for data in output:
        with open('solution_{}.txt'.format(dataset[-5]), 'a') as file:
            file.write(data)
            file.write('\n')

solution_naive('dataset_D.txt')