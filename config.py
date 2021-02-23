from configparser import ConfigParser

def sefaria_urls(filename='manuscripts.ini', section='links'):
    """
    Get the url for the respective manuscript
    """

    parser = ConfigParser()
    parser.read(filename)
    links = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            links[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} is not found')
    return links

def dirs(filename='manuscripts.ini', section='directories'):
    """
    Get the path for the manuscript directory
    """

    parser = ConfigParser()
    parser.read(filename)
    links = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            links[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} is not found')
    return links