'''
Hacked-up BibTeX parser, to be used for batch-renaming of entries.

Assumes entries are exported from Zotero, and handles accordingly. 

Your mileage may vary.


'''

def parse_line(line):
    '''
    Parse a line from a BibTeX bibliography and return as a tuple.
    '''
    line = line.strip()
    if line == '':
        return None

    if line[0] == '@':
        # Parse a new entry:
        line = line[1:-1] # Remove leading @ and training comma
        ref_type, ref_name = line.split("{")
        return {"ref_type": ref_type, "ref_name": ref_name}

    elif line[0] == "}":
        # End of entry
        return None

    else:
        key, data = line.split('=', 1)
        key = key.strip()
        data = data.strip()
        if data[-1] == ',': 
            data = data[:-1]
        return key, data


def load_file(path):
    '''
    Open the specified BibTeX file and read in.
    '''
    current_ref = None
    references = []
    f = open(path)
    for line in f:
        line_parsed = parse_line(line)
        if type(line_parsed) is dict:
            current_ref = line_parsed
        elif type(line_parsed) is tuple:
            current_ref[line_parsed[0]] = line_parsed[1]
        elif line_parsed is None and current_ref != None:
            references.append(current_ref)
            current_ref = None
    return references

def output(path, references):
    '''
    Write a Reference file out.
    '''

    f = open(path, "w")
    for ref in references:
        f.write("@" + ref["ref_type"] + "{" + ref["ref_name"] + ",\n")
        for attrib, value in ref.items():
            if attrib == 'ref_type' or attrib == 'ref_name': continue
            f.write(attrib + " = " + value + ",\n")
        f.write("},\n")
    f.close()

def rename(references):
    '''
    Rename all references to a firstauthor_year format
    '''
    new_references = []
    for ref in references:
        year = ref['year'][1:-1]

        if 'author' in ref:
            name_key = 'author'
        elif 'editor' in ref:
            name_key = 'editor'
        else:
            name_key = 'institution'
        
        first_author = ref[name_key][1:-1].split(',')[0]
        first_author = first_author.lower().replace(" ", "_")
        new_ref_name = first_author + "_" + year
        new_ref = {}
        for key, val in ref.items():
            new_ref[key] = val
        new_ref['ref_name'] = new_ref_name
        new_references.append(new_ref)
    return new_references

