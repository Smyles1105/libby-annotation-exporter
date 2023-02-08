import json

def create_dictionary_of_annotations(book_name):
    """
    This function loads the json data of the book book_name into a dictionary.
    This dictionary then gets returned.
    The dictionary of annotations will look something like the following:
    {Annotation1:
        {color: "#FFFFFF",
         chapter: "Chapter Name",
          quote: "quote text",
           note: "user's notes on quote"},
     Annotation2: {...},
      ...}
    :param book_name: The name of the book that has json data to be processed.
    :return: dictionary from file, file name and directory determined by parameter.
    """
    try:
        with open("quotesinjson/" + book_name + ".json", "r", encoding="UTF-8") as qfile:
            qfile = json.load(qfile)
        quote_dictionary = qfile["highlights"]
        return quote_dictionary
    except:
        print("No such file!")

def reverse_dictionary_items(dict):
    """
    This function takes a dictionary and reverses it by inserting each item into the first index
    of the new ordered dictionary.
    :param dict: the dictionary being reversed
    :return: the new dictionary with the reversed items list.
    """
    ordered_dict = []
    for item in dict:
        ordered_dict.insert(0, item)
    return ordered_dict

def write_quote(annotation, file, quote_count):
    """
    This function extracts the quote from the dictionary and then formats it to be
    written to the file.
    :param annotation: The dictionary that contains all of the annotation data
                        (color, chapter, quote, any notes written by the user)
    :param file: the note .txt file the quote is being written to.
    :param quote_count: the # of the quote in the given chapter.
    :return: since quote_count gets edited, it needs to be returned so the value gets updated
    """
    q = annotation["quote"].replace("\n", "")
    try:
        if len(q.strip()) < 3:
            raise ValueError
        file.write(str(quote_count) + ". \"" + q + "\"\n")
        quote_count += 1
    except ValueError as e:
        print("Exception: Quote does not meet character length standards (3 minimum)")
    return quote_count

def write_note(note_file, annotation):
    """
    This function checks to see if there is a note in the annotation and then writes it to the note file,
    formatted to create readability.
    See write_annotation() for a view of the new notes file format.
    :param note_file: the .txt file that the annotations are being written to in order to create book notes.
    :param annotation: the dictionary that contains the current annotation's data.
    :return:
    """
    try:
        annotation["note"].replace("\n", "")
        if len(annotation["note"].strip()) < 3:
            raise ValueError
        note_file.write("\t-\t" + annotation["note"] + "\n")
    except KeyError:
        print("Exception: Note not found")
    except ValueError:
        print("Exception: Note does not meet character length standards (3 minimum)")

def write_current_chapter(quote_count, annotation, note_file, current_chapter):
    """
    This function writes the current chapter as a line into the notes file.
    It checks to see if the new annotation being processed is in a new chapter,
    and if it is it will write it ot the notes file. This way all the annotations
    in a given chapter will be under a chapter heading in the notes file.
    :param annotation: dictionary of annotation data.
    :param note_file: file that annotation notes are being written to
    :param current_chapter: the current chapter in the dictionary of annotations being processed.
    :return: returns the current_chapter, and the quote_count because they may be different between function calls.
    """
    if annotation["chapter"] != current_chapter:
        note_file.write("\nChapter: " + annotation["chapter"] + "\n")
        current_chapter = annotation["chapter"]
        quote_count = 1

    return current_chapter, quote_count

def write_annotation(note_file, dict):
    """
    This function loops through all the annotations in the dictionary,
    writing the chapter headings and then the quotes and notes from the json data
    underneath their respective chapter headings.
    The formatting of the new notes file is the following:
    Chapter: Chapter Name 1
    1. Chapter 1 Quote 1
        -Quote 1 user notes (optional)
    2. Chapter 1 Quote 2
    3. Chapter 1 Quote 3
        -Quote 3 user notes (optional)
    Chapter: Chapter Name 2
    1. Chapter 2 Quote 1
    2. Chapter 2 Quote 2
    3. Chapter 3 Quote 3
    :param note_file: The file all the annotations are being written to for reading notes.
    :param dict: The dictionary of annotations that gets looped through
    :return: No return since it is taking the params given to write all necessary annotation info for the format I want.
    """
    current_chapter = ""
    quote_count = 0
    for annotation in dict:
        current_chapter, quote_count = write_current_chapter(quote_count, annotation, note_file, current_chapter)
        quote_count = write_quote(annotation, note_file, quote_count)
        write_note(note_file, annotation)


def main():
    """
    main will request the name of the book the user will want the script to process
    which will take the json data of the given book for them and spit out a new notes
    file that contains all of their annotations in a neat, spaced out format
    underneath their respective chapter headings.
    :return: no return
    """
    book_name = input("Enter file name of json file:\n")

    dictionary_of_annotations = create_dictionary_of_annotations(book_name)
    ordered_highlight_dict = reverse_dictionary_items(dictionary_of_annotations)
    try:
        with open("formattedbookquotes/" + book_name + ".txt", "w") as note_file:
            write_annotation(note_file, ordered_highlight_dict)
    except FileNotFoundError:
        print("Exception: File not found")





main()
