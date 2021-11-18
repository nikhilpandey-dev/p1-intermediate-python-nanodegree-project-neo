"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
from models import NearEarthObject, CloseApproach
from helpers import datetime_to_str
def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    # TODO: Write the results to a CSV file, following the specification in the instructions.

    with open(filename, 'w') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=list(fieldnames))
        writer.writeheader()
        for element in results:
            output_row_dict = dict()
            output_row_dict['datetime_utc'] = datetime_to_str(element.time)
            output_row_dict['distance_au'] = element.distance
            output_row_dict['velocity_km_s'] = element.velocity
            output_row_dict['designation'] = element.designation
            if element.neo.name is None:
                output_row_dict['name'] = ''
            else:
                output_row_dict['name'] = element.neo.name
            if element.neo.diameter:
                output_row_dict['diameter_km'] = element.neo.diameter
            else:
                output_row_dict['diameter_km'] = 'nan'
            if element.neo.hazardous:
                output_row_dict['potentially_hazardous'] = 'True'
            else:
                output_row_dict['potentially_hazardous'] = 'False'
            writer.writerow(output_row_dict)



def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    output_rows_list = list()
    with open(filename, 'w') as outfile:
        output_row_dict = dict()
        for element in results:
            output_row_dict = dict()
            output_row_dict['datetime_utc'] = datetime_to_str(element.time)
            output_row_dict['distance_au'] = element.distance
            output_row_dict['velocity_km_s'] = element.velocity
            output_neo_dict = dict()
            output_neo_dict['designation'] = element.neo.designation
            if element.neo.name is None:
                output_neo_dict['name'] = ''
            else:
                output_row_dict['name'] = element.neo.name
            output_neo_dict['diameter_km'] = element.neo.diameter
            output_neo_dict['potentially_hazardous'] = element.neo.hazardous
            output_row_dict['neo'] = output_neo_dict
            output_rows_list.append(output_row_dict)
        
        json.dump(output_rows_list, outfile, allow_nan=True)



