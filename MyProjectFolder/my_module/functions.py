"""A collection of function for doing my project."""

def caesar_decrypt(crypto, key = 3): 
    """Converts Caesar cryptogram input string into string containing the decoded message.

    Parameters
    ----------
    crypto : string
        String to convert into the message
    key : integer
        The amount of times to shift the alphabet to find the message's letter

    Returns
    -------
    message : string
        String containing the decoded message
    """

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    crypto = crypto.upper()
    message = ''

    # Caesar cipher replaces message with letters in the alphabet that is a constant number away
    # Decodes cipher by using the key to know where in the alphabet retrieve the message's letter
    # Using this key, A decodes as X, B decodes as Y, C decodes as Z
    for letter in crypto:
        if letter in alpha:
            # Loops around to the end of alphabet if the index goes below 0 after substracting key
            letter_index = (alpha.find(letter) - key) % len(alpha)
            message = message + alpha[letter_index]
        else:
            message = message + letter

    return message

def a1z26_decrypt(crypto):
    """Converts A1Z26 cryptogram input list into string containing the decoded message.

    Parameters
    ----------
    crypto : list
        list of integers and strings for spaces and punctuation to convert into  message

    Returns
    -------
    message : string
        String containing the decoded message
    """

    message = ''

    # A1Z26 cipher replaces letter in message with the number of its position in the alphabet
    # A encodes as 1, Z encodes as 26
    for num in crypto:
        if type(num) == int:
            # The letters are the output of chr()
            # Starting from A's input as 65 and ending with Z's input as 90
            letter = chr(num + 64)
            message += letter
        else:
            message = message + num

    return message

def atbash_decrypt(crypto):
    """Converts Atbash cryptogram input string into string containing the decoded message.

    Parameters
    ----------
    crypto : string
        String to convert into the message

    Returns
    -------
    message : string
        String containing the decoded message
    """

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse_alpha = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    crypto = crypto.upper()
    message = ''

    # Atbash cipher maps alphabet to the same position in a reversed alphabet
    # A in the message becomes Z in the cipher
    for letter in crypto:
        if letter in reverse_alpha:
            # Finds index of letter within reversed alphabet
            # Finds that index in the alphabet to decode the message
            letter_index = reverse_alpha.find(letter)
            message = message + alpha[letter_index]
        else:
            message = message + letter

    return message

def search(message):
    """Look through list "episodes" using a message to find facts from the episode.

    Parameters
    ----------
    message : string
        String that is searched for in the "episodes" list

    Returns
    -------
    facts : dictionary
        Contains title, message, cryptogram, where cryptogram is located, and type of cipher.
    """

    facts = next((item
        for item in episodes
            if item['message'] == message), None)

    return facts

def find_caesar(crypto):
    """Decodes cryptogram using Caesar decoder and uses message to find facts from the list "episodes".

    Parameters
    ----------
    crypto : string
        String that converts into the string message, which is searched for in the list.

    Returns
    -------
    facts : dictionary
        Contains title, message, cryptogram, where cryptogram is located, and type of cipher.
    """

    message = caesar_decrypt(crypto, key = 3)
    facts = search(message)

    return facts

def find_atbash(crypto):
    """Decodes cryptogram using Atbash decoder and uses message to find facts from list "episodes".

    Parameters
    ----------
    crypto : string
        String that converts into the string message, which is searched for in the list.

    Returns
    -------
    facts : dictionary
        Contains title, message, cryptogram, where cryptogram is located, and type of cipher.
    """

    message = atbash_decrypt(crypto)
    facts = search(message)

    return facts

def find_a1z26(crypto):
    """Decodes cryptogram using A1Z26 decoder and uses message to find facts from list "episodes".

    Parameters
    ----------
    crypto : list
        List that converts into the string message, which is searched for in the list.

    Returns
    -------
    facts : dictionary
        Contains title, message, cryptogram, where cryptogram is located, and type of cipher.
    """

    message = a1z26_decrypt(crypto)
    facts = search(message)

    return facts

# List of episode titles, messages, cryptograms, where cryptogram is located, and type of cipher
episodes = [{"title": "Gravity Falls Title Theme",
             "message": "STAN IS NOT WHAT HE SEEMS",
             "crypt": "VWDQ LV QRW ZKDW KH VHHPV",
             "where": "End of title sequence",
             "type": "Caesar"},
            {"title": "Tourist Trapped",
             "message": "WELCOME TO GRAVITY FALLS",
             "crypt": "ZHOFRPH WR JUDYLWB IDOOV",
             "where": "End Credits",
             "type": "Caesar"},
            {"title": "The Legend of the Gobblewonker",
             "message": "NEXT WEEK: RETURN TO BUTT ISLAND",
             "crypt": "QHAW ZHHN: UHWXUQ WR EXWW LVODQG",
             "where": " End Credits",
             "type": "Caesar"},
            {"title": "Headhunters",
             "message": "HE'S STILL IN THE VENTS",
             "crypt": "KH'V VWLOO LQ WKH YHQWV",
             "where": "End Credits",
             "type": "Caesar"},
            {"title": "Dipper vs. Manliness",
             "message": "MR. CAESARIAN WILL BE OUT NEXT WEEK. MR. ATBASH WILL SUBSTITUTE",
             "crypt": "PU. FDHVDULDQ ZLOO EH RXW QHAW ZHHN. PU. DWEDVK ZLOO VXEVWLWXWH",
             "where": "End Credits",
             "type": "Caesar"},
            {"title": "Carpet Diem",
             "message": "PUBERTY IS THE GREATEST MYSTERY OF ALL. ALSO: GO OUTSIDE AND MAKE FRIENDS",
             "crypt": "SXEHUWB LV WKH JUHDWHVW PBVWHUB RI DOO. DOVR: JR RXWVLGH DQG PDNH IULHQGV",
             "where": "Bottom of 'Why Am I Sweaty' page",
             "type": "Caesar"},
            {"title": "The Hand That Rocks the Mabel",
             "message": "CARLA, WHY WON'T YOU CALL ME?",
             "crypt": "FDUOD, ZKB ZRQ'W BRX FDOO PH?",
             "where": "End Credits",
             "type": "Caesar"},
            {"title": "The Inconveniencing",
             "message": "ONWARDS AOSHIMA!",
             "crypt": "RQZDUGV DRVKLPD!",
             "where": "End Credits",
             "type": "Caesar"},
            {"title": "Land Before Swine",
             "message": "LIES",
             "crypt": "OLHV",
             "where": "Grunkle Stan's back tattoo",
             "type": "Caesar"},
            {"title": "Dreamscaperers",
             "message": "MYSTERY SHACK",
             "crypt": "PBVWHUB VKDFN",
             "where": "Mindscape version of Mystery Shack sign",
             "type": "Caesar"},
            {"title": "Gideon Rises",
             "message": "BILL IS WATCHING",
             "crypt": "ELOO LV ZDWFKLQJ",
             "where": "In pipes of Mystery Shack",
             "type": "Caesar"},
            {"title": "Double Dipper",
             "message": "PAPER JAM DIPPER SAYS: 'AUUGHWXQHGADSADSADUH!'",
             "crypt": "KZKVI QZN WRKKVI HZBH: 'ZFFTSDCJSTZWHZWHZWFS!'",
             "where": "End Credits",
             "type": "Atbash"},
            {"title": "Irrational Treasure",
             "message": "E. PLURIBUS TREMBLEY",
             "crypt": "V. KOFIRYFH GIVNYOVB",
             "where": "End Credits",
             "type": "Atbash"},
            {"title": "The Time Traveler's Pig",
             "message": "NOT H.G. WELLS APPROVED",
             "crypt": "MLG S.T. DVOOH ZKKILEVW",
             "where": "End Credits",
             "type": "Atbash"},
            {"title": "Fight Fighters",
             "message": "SORRY DIPPER, BUT YOUR WENDY IS IN ANOTHER CASTLE",
             "crypt": "HLIIB WRKKVI, YFG BLFI DVMWB RH RM ZMLGSVI XZHGOV",
             "where": "End Credits",
             "type": "Atbash"},
            {"title": "Little Dipper",
             "message": "THE INVISIBLE WIZARD IS WATCHING",
             "crypt": "GSV RMERHRYOV DRAZIW RH DZGXSRMT",
             "where": "End Credits",
             "type": "Atbash"},
            {"title": "Summerween",
             "message": "BROUGHT TO YOU BY HOMEWORK: THE CANDY",
             "crypt": "YILFTSG GL BLF YB SLNVDLIP: GSV XZMWB",
             "where": "End Credits",
             "type": "Atbash"},
            {"title": "Boss Mabel",
             "message": "HEAVY IS THE HEAD THAT WEARS THE FEZ",
             "crypt": "SVZEB RH GSV SVZW GSZG DVZIH GSV UVA",
             "where": "End Credits",
             "type": "Atbash"},
            {"title": "Bottomless Pit!",
             "message": "NEXT UP: FOOTBOT TWO: GRUNKLE'S GREVENGE",
             "crypt": [14, 5, 24, 20, " ", 21, 16, ": ", 6, 15, 15, 20, 2, 15, 20, " ", 20, 23,
                       15, ": ", 7, 18, 21, 14, 11, 12, 5, "'", 19, " ", 7, 18, 5, 22, 5, 14, 7, 5],
             "where": "End Credits",
             "type": "A1Z26"},
            {"title": "The Deep End",
             "message": "VIVAN LOS PATOS DE LA PISCINA",
             "crypt": [22, 9, 22, 1, 14, " ", 12, 15, 19, " ", 16, 1, 20, 15, 19, " ", 4, 5,
                       " ", 12, 1, " ", 16, 9, 19, 3, 9, 14, 1],
             "where": "End Credits",
             "type": "A1Z26"},
            {"title": "Carpet Diem",
             "message": "BUT WHO STOLE THE CAPERS?",
             "crypt": [2, 21, 20, " ", 23, 8, 15, " ", 19, 20, 15, 12, 5, " ", 20, 8, 5, " ", 3,
                       1, 16, 5, 18, 19, "?"],
             "where": "End Credits",
             "type": "A1Z26"},
            {"title": "Boyz Crazy",
             "message": "HAPPY NOW, ARIEL?",
             "crypt": [8, 1, 16, 16, 25, " ", 14, 15, 23, ", ", 1, 18, 9, 5, 12, "?"],
             "where": "End Credits",
             "type": "A1Z26"},
            {"title": "Land Before Swine",
             "message": "IT WORKS FOR PIIIIIIIIIIIIIIIIIGS!",
             "crypt": [9, 20, " ", 23, 15, 18, 11, 19, " ", 6, 15, 18, " ", 16,
                       9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 7, 19, "!"],
             "where": "End Credits",
             "type": "A1Z26"},
            {"title": "Dreamscaperers",
             "message": "TO BE CONTINUED",
             "crypt": [20, 15, " ", 2, 5, " ", 3, 15, 14, 20, 9, 14, 21, 5, 4],
             "where": "End Credits",
             "type": "A1Z26"},
            {"title": "Gideon Rises",
             "message": "REVERSE THE CIPHERS",
             "crypt": [18, 5, 22, 5, 18, 19, 5, " ", 20, 8, 5, " ", 3, 9, 16, 8, 5, 18, 19],
             "where": "End Credits",
             "type": "A1Z26"}]