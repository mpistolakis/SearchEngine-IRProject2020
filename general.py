import os
import pickle

# Each website you crawl is a separate project
import shutil
from tld import get_tld


def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating project " + directory)
        os.makedirs(directory)


# Creates new file

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


def create_index_files(project):
    freqDict = project + '/freq_dictionary.pkl'
    tempIndex = project + '/invertedIndex.pkl'
    if not os.path.isfile(tempIndex):
        write_file(tempIndex, '')
    if not os.path.isfile(freqDict):
        write_file(freqDict, '')


# Create queue and crawled files

def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    dictionary = project_name + '/dictionary.pkl'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')
    if not os.path.isfile(dictionary):
        write_file(dictionary, '')


# Delete all previous entries in the crawler folder
def delete_data_files(project_name):
    if os.path.isdir(project_name):
        shutil.rmtree(project_name)


# Add data onto an existing file

def append_to_file(path, data):
    with open(path, 'a', encoding="utf-8", errors="ignore") as file:
        file.write(data)
        file.write("\n")


# Delete the contents of a file

def delete_file_contents(path):
    with open(path, 'w'):
        pass


# Read a file and convert each line to set item

def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt', encoding="UTF-8", errors="ignore") as f:
        for line in f:
            results.add(line.replace('\n', ''))
        return results


# Iterate through a set , each item will be a new line in the file


def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        res = get_tld(link, as_object=True, fail_silently=True)
        if res is not None:
            if res.fld is not None:
                append_to_file(file, link)


# Dumps the dictionary of text into file (using pickle)
def dict_to_file(textDict, file):
    with open(file, 'wb') as file:
        pickle.dump(textDict, file)
        file.close()


def file_to_dict(file):
    if os.path.getsize(file) > 0:
        with open(file, 'rb') as file:
            new_dict = pickle.load(file)
            file.close()
            return new_dict
    else:
        return dict()


def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
