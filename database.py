"""A database collections of near-Earth objects & their close approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.

"""
from extract import load_neos, load_approaches
from models import NearEarthObject, CloseApproach


class NEODatabase:
    """A database of near-Earth objects & close approaches.

    
    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """
    def __init__(self, neos: NearEarthObject, approaches: CloseApproach):
        """Create a new `NEODatabase`.

        As a precondition, this constructor assumes that
         the collections of NEOs and close approaches haven't
          yet been linked - that is, the `.approaches`
           attribute of each `NearEarthObject` resolves to an empty
            collection, and the `.neo` attribute of each `CloseApproach`
             is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO.
         This constructor modifies the supplied NEOs and close approaches
          to link them together - after it's done, the `.approaches`
           attribute of each NEO has a collection of that NEO's
            close approaches, and the `.neo` attribute of each
            close approach references the appropriate NEO.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """
        approaches_with_neo = []
        neo_with_approaches = []
        neo_approach_dict = dict()
        self._name_dict = dict()
        self._des_dict = dict()
        for neo in neos:
            self._name_dict[neo.name] = neo
            self._des_dict[neo.designation] = neo

        for approach in approaches:
            if approach.designation in self._des_dict:
                approach.neo = self._des_dict[approach.designation]
            else:
                approach.neo = None
            approaches_with_neo.append(approach)

        self._approaches = approaches_with_neo

        for approach in self._approaches:
            if approach.designation not in neo_approach_dict:
                neo_approach_dict[approach.designation] = set()

            neo_approach_dict[approach.designation].add(approach)

        for neo in neos:
            if neo.designation in neo_approach_dict:
                neo.approaches = list(neo_approach_dict[neo.designation])
            else:
                neo.designation = []

            neo_with_approaches.append(neo)

        self._neos = neo_with_approaches

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the
         NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation,
         or `None`.
        """
        if designation in self._des_dict:
            return self._des_dict[designation]
        else:
            return None

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """
        if name in self._name_dict:
            return self._name_dict[name]
        else:
            return None

    def query(self, filters=()):
        """Query close approaches to generate CloseApproaches.

         These CloseAprroaches match a collection of filters.

        This generates a stream of `CloseApproach` objects that match
         all of the provided filters.

        If no arguments are provided, generate all known close approaches.

        The `CloseApproach` objects are generated in internal order,
         which isn't guaranteed to be sorted meaninfully, although is
          often sorted by time.

        :param filters: A collection of filters capturing user-specified
         criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        for approach in self._approaches:
            flag: bool = True
            """ All the filters jointly form a giant and statemnt so
             if any condition is false, then that approach will not
              be considered and hence just considering to test even
               if one condition is false. """
            for filter in filters:
                if not filter(approach):
                    flag = False
                    break
            if flag:
                yield approach
