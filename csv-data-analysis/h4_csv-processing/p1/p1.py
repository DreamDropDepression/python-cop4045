# -*- coding: utf-8 -*-
'''Top Movies and Cast'''

import csv


def print_directors(title, value, lst):
    print('-'*80)
    d = '-'*20
    c = '-'*5
    print('{:<20s} | {:<5s}'.format(title, value))
    print('{:<20s} | {:<5s}'.format(d, c))
    for i, row in enumerate(lst):
        print('{:<20s} | {:<5d}'.format(row[1], row[0]))
        if i == 5:
            break
    print('\n\n')


def print_actors(title, value, lst):
    print('-'*80)
    d = '-'*20
    c = '-'*20
    print('{:<20s} | {:<5s}'.format(title, value))
    if value == 'Count':
        print('{:<20s} | {:<5s}'.format(d, c))
    else:
        print('{:<20s} | {:<20s}'.format(d, c))
    for i, row in enumerate(lst):
        if value == 'Count':
            print('{:<20s} | {:<5d}'.format(row[1], row[0]))
        else:
            print('{:<20s} | {:<20.2f}'.format(row[1], row[0]))
        if i == 5:
            break
    print('\n\n')


def prdict(dct):
    print('\n'*2)
    for i, (k, v) in enumerate(dct.items()):
        print(k, ' : ', v)
        if i == 9:
            print('\n'*2)
            break


def get_lists():
    '''Returns 3 lists in this order: top-rated, top-gross, top-casts'''
    # File Parsing: read_ranks() handles both top-gross and top-rated
    def read_casts(afile):
        data = csv.reader(afile)
        return [tuple(row) for row in data]

    def read_ranks(afile):
        '''types: int, str, int, float. Header is skipped.'''
        def parse_row(p):
            '''p = position'''
            return int(p[0]), p[1], int(p[2]), float(p[3])

        data = csv.reader(afile)
        next(data)
        return [tuple(parse_row(row)) for row in data]

    file_top_rated = 'imdb-top-rated.csv'
    file_top_gross = 'imdb-top-grossing.csv'
    file_top_casts = 'imdb-top-casts.csv'

    with open(file_top_rated, 'r', encoding='utf-8') as fobj:
        rank_ls = read_ranks(fobj)
    with open(file_top_gross, 'r', encoding='utf-8') as fobj:
        gross_ls = read_ranks(fobj)
    with open(file_top_casts, 'r', encoding='utf-8') as fobj:
        cast_ls = read_casts(fobj)
    return rank_ls, gross_ls, cast_ls


def get_dicts(ls1, ls2, ls3):
    def get_rank_dict(lst):
        return {(p[1], p[2]): (p[0], p[3]) for p in lst}

    def get_cast_dict(lst):
        return {(p[0], int(p[1])): (p[2:]) for p in lst}

    def get_actors_dict(dct):
        '''Returns a dictionary: key='actorname' value=<list of tuples>'''
        ac_mvs = {}
        for movie, cast in dct.items():
            for actor in cast[1:]:
                if actor in ac_mvs:
                    ac_mvs[actor].append(movie)
                else:
                    ac_mvs[actor] = [movie]
        return ac_mvs

    rd = get_rank_dict(ls1)
    gd = get_rank_dict(ls2)
    cd = get_cast_dict(ls3)
    am = get_actors_dict(cd)
    return rd, gd, cd, am


def count_listings(cast_dct, rank_dct):
    count = {}
    rset = set(rank_dct.keys())
    for key in rset:
        name = cast_dct[key][0]
        count[name] = count.get(name, 0) + 1
    return sorted([(num, name) for name, num in count.items()], reverse=True)


def count_roles(actors_dct, rank_dct):
    '''Returns a list of (actors, #roles in top rated)'''
    count = {}
    rset = set(rank_dct.keys())
    for (act, mvs) in actors_dct.items():
        for mv in mvs:
            if mv in rset:
                count[act] = count.get(act, 0) + 1
    return sorted([(num, name) for name, num in count.items()], reverse=True)


def top_earners(gross_dct, cast_dct):
    a = {}

    def amt(n, i, s):
        return ((2**(n-i))*s) / 31

    for movie in gross_dct.keys():
        gross = gross_dct[movie][1]
        actors = cast_dct[movie][1:]
        n = len(actors)
        for i, actor in enumerate(actors):
            a[actor] = a.get(actor, 0) + amt(n, i+1, gross)
    return sorted([(v, k) for k, v in a.items()], reverse=True)


def main():
    rank_ls, gross_ls, cast_ls = get_lists()
    rank_dct, gross_dct, cast_dct, act_roles_dct = get_dicts(
        rank_ls, gross_ls, cast_ls)
    dir_in_top_rated = count_listings(cast_dct, rank_dct)
    dir_in_top_gross = count_listings(cast_dct, gross_dct)
    act_in_top_rated = count_roles(act_roles_dct, rank_dct)
    act_in_top_gross = top_earners(gross_dct, cast_dct)

    print('Directors with most movies in top-rated list')
    print_directors('Directors', 'Count', dir_in_top_rated)

    print('Directors with most movies in top-grossing list')
    print_directors('Directors', 'Count', dir_in_top_gross)

    print('Actors with most movies in top-rated list')
    print_actors('Actors', 'Count', act_in_top_rated)

    print('Actors with most money earned in top-grossing list')
    print_actors('Actors', 'Gross', act_in_top_gross)


if __name__ == '__main__':
    main()
