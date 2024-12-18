def create_an_empty_list():
    return []

def create_a_list():
    return ['banana', 'apple', 'orange', 'kiwi']


def add_element_to_end_of_list(l, element):
    
    if l is None:
        l = []
    l.append(element)
    return l

    


def add_element_to_start_of_list(l, element):
    if l is None:
        l = []
    l.insert(0, element)
    return l
def remove_element_from_end_of_list(l):
    if l:
        l.pop()
    return l 

def remove_element_from_start_of_list(l):
    if l:
        del l [0]
    return l

def retrieve_first_element_from_list(l):
    return l [0] if l else none

def retrieve_element_from_index(l, index):
    return l [index] if l and 0 <= index < len(l) else None
def retrieve_last_element_from_list(l):
    return l[-1] if l else none 
