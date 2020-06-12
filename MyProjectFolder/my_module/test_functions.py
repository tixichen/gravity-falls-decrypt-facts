from functions import caesar_decrypt
from functions import a1z26_decrypt
from functions import atbash_decrypt
from functions import search
from functions import episodes
from functions import find_caesar
from functions import find_atbash
from functions import find_a1z26

def test_caesar_decrypt():
    """ Tests that output is a string and that it decrypts"""

    assert callable(caesar_decrypt)
    assert isinstance(caesar_decrypt("SBWKRQ LV IXQ"), str)
    assert caesar_decrypt("SBWKRQ LV IXQ") == "PYTHON IS FUN"

def test_a1z26_decrypt():
    """ Tests that output is a string and that it decrypts"""

    assert callable(a1z26_decrypt)
    assert isinstance(a1z26_decrypt([8, 15, 23, " ", 4, 15, 5, 19, " ", 15,
                                     14, 5, " ", 16, 25, 20, 8, 15, 14, "?"]), str)
    assert a1z26_decrypt([8, 15, 23, " ", 4, 15, 5, 19, " ", 15,
                          14, 5, " ", 16, 25, 20, 8, 15, 14, "?"]) == "HOW DOES ONE PYTHON?"

def test_atbash_decrypt():
    """ Tests that output is a string and that it decrypts"""

    assert callable(atbash_decrypt)
    assert isinstance(atbash_decrypt("HMVZPB KBGSLM HMZPV"), str)
    assert atbash_decrypt("HMVZPB KBGSLM HMZPV") == "SNEAKY PYTHON SNAKE"

def test_search():
    """Tests that output is a dictionary that contains the message"""

    assert callable(search)
    assert isinstance(search("BILL IS WATCHING"), dict)
    assert search("BILL IS WATCHING") == {'title': 'Gideon Rises', 'message': 'BILL IS WATCHING',
                                          'crypt': 'ELOO LV ZDWFKLQJ',
                                          'where': 'In pipes of Mystery Shack', 'type': 'Caesar'}

def test_find_caesar():
    """Tests that output is a dictionary that contains the decoded message"""

    assert callable(find_caesar)
    assert isinstance(find_caesar("PBVWHUB VKDFN"), dict)
    assert find_caesar("PBVWHUB VKDFN") == {'title': 'Dreamscaperers', 'message': 'MYSTERY SHACK',
                                            'crypt': 'PBVWHUB VKDFN',
                                            'where': 'Mindscape version of Mystery Shack sign',
                                            'type': 'Caesar'}

def test_find_atbash():
    """Tests that output is a dictionary that contains the decoded message"""

    assert callable(find_atbash)
    assert isinstance(find_atbash("MLG S.T. DVOOH ZKKILEVW"), dict)
    assert find_atbash("MLG S.T. DVOOH ZKKILEVW") == {'title': "The Time Traveler's Pig",
                                                      'message': 'NOT H.G. WELLS APPROVED',
                                                      'crypt': 'MLG S.T. DVOOH ZKKILEVW',
                                                      'where': 'End Credits', 'type': 'Atbash'}

def test_find_a1z26():
    """Tests that output is a dictionary that contains the decoded message"""

    assert callable(find_a1z26)
    assert isinstance(find_a1z26([8, 1, 16, 16, 25, " ", 14, 15, 23, ", ",
                                  1, 18, 9, 5, 12, "?"]), dict)
    assert find_a1z26([8, 1, 16, 16, 25, " ", 14, 15, 23, ", ",
                       1, 18, 9, 5, 12, "?"]) == {'title': 'Boyz Crazy', 
                                                  'message': 'HAPPY NOW, ARIEL?',
                                                  'crypt': [8, 1, 16, 16, 25, ' ', 14, 15, 
                                                            23, ', ', 1, 18, 9, 5, 12, '?'],
                                                  'where': 'End Credits', 'type': 'A1Z26'} 