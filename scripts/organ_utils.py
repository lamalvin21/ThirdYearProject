import os
import re
import json

##########################################################
#
# filenames and identifiers
#

def constructOrganID(part, filename):
    return part + '_' + filename.replace(' ','').replace('.docx','').replace("'",'')

def getPartFromID(organid):
    part = organid[:6]
    if organid == 'Part01_103KROMM':
        part = 'Part02'
    return part

##########################################################
#
# Load all data
#

def loadOrganData(sets = 'all'):

    organdata = {}

    if sets == 'all':
        sets = [
            'organids',
            'base',
            'history_base',
            'history_projects',
            'dispositions',
            'compoundstops',
            'tech',
            'texts_hist',
            'texts_fulltexts',
            'texts_tech',
            'texts_bijzonderheden',
            'texts_offsets'
        ]

    for setname in sets:
        with open(f'../output/{setname}.json', 'r') as f:
            organdata[setname] = json.load(f)
    
    return organdata


##########################################################
#
# for docx2python:
#

def isTable(block):
    if len(block) > 0:
        if len(block[0]) > 1:
            return True
    return False

def isEmptyBlock(block):
    if len(block) > 0:
        if len(block[0]) > 0:
            if len(block[0][0]) > 0:
                return False
    return True

# return last non empty line of block
def get_last_text_line(body_element):
    last_line = '' #or should this be None?
    if len(body_element) != 0:
        if len(body_element[-1]) != 0:
            if len(body_element[-1][-1]) != 0:
                ix = -1
                for ix in range(len(body_element[-1][-1])):
                    if body_element[-1][-1][ix] != '':
                        last_line = body_element[-1][-1][ix]
    return last_line



##########################################################
#
# Preprocessing of the raw text
#
# Repair encodings, replace some characters, remove markup
#

# convention:
thin_arrow = "→"
thick_arrow = "◂"

charmap = {
    '\xa0': ' ', #unbreakable space
    '¹': '1',
    '²': '2',
    '³': '3',
    '<\\->': '-',
    '<\\#136>': 'à',
    '<\\#138>': 'ä',
    '<\\#141>': 'ç',
    '<\\#142>': 'é',
    '<\\#143>': 'è',
    '<\\#145>': 'ë',
    '<\\#149>': 'ï',
    '<\\#151>': 'ó',
    '<\\#154>': 'ö',
    '<\\#158>': 'û',    
    '<\\#159>': 'ü',
    '<\\b>': '',
    '<+>': '',
    '<P>': '',
}

def transpose_encoding_line(line):
    for char_in, char_out in charmap.items():
        line = line.replace(char_in, char_out)
    return line

def transpose_encoding_block(lines):
    for ix, line in enumerate(lines):
        lines[ix] = transpose_encoding_line(line)
    return lines

def replace_arrows_line(line, part_path):
    #First thick arrow
    if part_path in ['Part01']:
        line = line.replace(' # ', thick_arrow)
    if part_path in ['Part02', 'Part03', 'Part04', 'Part05']:
        line = line.replace('◂→', thick_arrow)
    if part_path in ['Part06', 'Part07', 'Part08', 'Part09', 'Part10', 'Part11', 'Part12', 'Part13', 'Part14', 'Part15']:
        line = line.replace('$', thick_arrow)
    if part_path in ['Part06']:
        line = line.replace('<span style=font-family:Wingdings>&#x00D7;</span><span style=font-family:Symbol>&#x00AE;</span>', thick_arrow)
    if part_path in ['Part08']:
        line = line.replace('<span style=font-family:Symbol>&#x00AE;</span>', thick_arrow)
    
    #Now thin arrow
    if part_path in ['Part01']:
        line = line.replace('  ', thin_arrow)
    if part_path in ['Part01', 'Part02', 'Part03', 'Part04', 'Part05', 'Part06', 'Part09', 'Part10', 'Part12', 'Part13']:
        line = line.replace('→', thin_arrow)
    if part_path in ['Part06', 'Part07', 'Part08']:
        line = line.replace('<span style=font-family:Symbol>&#x00AE;</span>', thin_arrow)
    
    return line

def replace_arrows_block(lines, part_path):
    for ix, line in enumerate(lines):
        lines[ix] = replace_arrows_line(line, part_path)
    return lines

#remove markup (e.g. @T1:, @K2:, [T1], [x2], etc., <I>, <h150>, <h100>)
def remove_markup_line(line, part_path):
    return re.sub('@[a-zA-Z][0-9]:|\[[a-zA-Z][0-9]\]|<I>|<h1[50]0>','',line)

def remove_markup_block(lines, part_path):
    if part_path in ['Part01', 'Part02']:
        lines = [remove_markup_line(line, part_path) for line in lines]
    return lines

#########################
#for external use

def preprocess_line(line, part_path):
    """Convert the line into utf8, remove markup commands, harmonize arrow styles among volumes
    line: string
    part_path: identifier for the part of the encyclopaedia. E.g. 'Part03', 'Part14', etc.
    Returns: converted line.
    """
    line = remove_markup_line(line, part_path)
    line = transpose_encoding_line(line)
    return replace_arrows_line(line, part_path)
    
def preprocess_block(lines, part_path):
    """Convert the lines into utf8, remove markup commands, harmonize arrow styles among volumes
    line: list of strings
    part_path: identifier for the part of the encyclopaedia. E.g. 'Part03', 'Part14', etc.
    Returns: converted lines.
    """
    lines = remove_markup_block(lines, part_path)
    lines = transpose_encoding_block(lines)
    return replace_arrows_block(lines, part_path)

# repair encoding and remove markup. docbody is doc.body where doc is a docx2python object
def preprocess_doc(docbody, part_path):
    for part0 in docbody:
        for part1 in part0:
            for ix, part2 in enumerate(part1):
                part1[ix] = remove_markup_block(part1[ix], part_path)
                part1[ix] = transpose_encoding_block(part1[ix])
                part1[ix] = replace_arrows_block(part1[ix], part_path)
    return docbody


