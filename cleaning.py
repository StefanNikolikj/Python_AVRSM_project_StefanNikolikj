from cleanco import basename
import requests
import json
import re


def parentheses_check(name):
    """
    Clearing the string from all parentheses and text within them as required

    :param name: the string which the function works with
    :return: returns the string after formatting
    """
    name = re.sub("\(.*?\)", "()", name)
    name = name.replace('(', '').replace(')', '')
    return name


def quotation_marks_check(name):
    """
    Clearing the text from all quotation marks as required

    :param name: the string which the function works with
    :return: returns the string after formatting
    """
    return name.replace('"', '')


def lowering_letters(name):
    """
    Editing a string so that all first letters of each word are capital letters and all other letters are lowered
    this also makes all acronyms that are made with dots and ampersands into required format (all letters are capital)

    :param name: the string which the function works with
    :return: returns the string after formatting
    """
    return name.title()


def get_data():
    """
    Requesting the needed data from a specific API

    :return: returns the data (as a json list)
    """
    companies = requests.get("http://127.0.0.1:5000/getName").json()
    return companies


def post_data(companies):
    """
    Posting the data with a specific API

    param companies: list of the companies that are being posted in MongoDB
    :return:
    """
    for i in range(1, 20000):
        x = (companies[i])
        x[1] = parentheses_check(x[1])
        x[1] = quotation_marks_check(x[1])
        x[1] = basename(x[1])
        x[1] = lowering_letters(x[1])
        dict = {"_id": x[1], "country": x[2], "city": x[3], "nace": x[4], "website": x[5]}
        requests.post("http://127.0.0.1:5000/postName", data=json.dumps(dict))


companies = get_data()
post_data(companies)
