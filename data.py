# -*- coding: utf-8 -*-

"""
Name: Santhosh Soundararajan
Indiana University
Start date: 24th April, 2016
End date: 26th April, 2016
Objective: To fetch 20newsgroups data 
"""

from sklearn.datasets import fetch_20newsgroups

def load_training_data(categories_list = None):
    """
    This function helps to load the
    training data from the twenty news group data
    and returns them.

    Arguments:
        1. categories_list: Defaulted to None, when given
        retrieves only mentioned categories.
    """

    train_data = fetch_20newsgroups(subset = 'train', shuffle = True,
                                    categories = categories_list)
    # load the training data set
    return train_data

def load_test_data(categories_list = None):
    """
    This function helps to load the
    test data from the twenty news group data
    and returns them.

    Arguments:
        1. categories_list: Defaulted to None, when given
        retrieves only mentioned categories.
    """

    test_data = fetch_20newsgroups(subset = 'test', shuffle = True,
                                    categories = categories_list)
    # load the training data set
    return test_data
