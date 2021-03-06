"""Extract data on near-Earth objects & close approaches from CSV & JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided
 at the command line, and uses the resulting collections to
  build an `NEODatabase`.

"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path='./data/neos.csv'):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data
     about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    near_earth_objects_list = []
    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)
        for e in reader:
            neo = NearEarthObject(e['pdes'], e['name'],
                                  e['diameter'], e['pha'])
            near_earth_objects_list.append(neo)

    return near_earth_objects_list


def load_approaches(cad_json_path='./data/cad.json'):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data
     about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    close_approach_list = []
    with open(cad_json_path, 'r') as infile:
        contents = json.load(infile)
        json_data = [dict(zip(contents["fields"], data))
                     for data in contents["data"]]

    for data in json_data:
        close_approach = CloseApproach(data["des"], data["cd"],
                                       data["dist"], data["v_rel"])
        close_approach_list.append(close_approach)

    return close_approach_list
