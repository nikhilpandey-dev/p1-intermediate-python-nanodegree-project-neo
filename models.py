"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

"""
from helpers import cd_to_datetime, datetime_to_str
import math


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic
    and physical parameters about the object, such
    as its primary designation (required, unique),
    IAU name (optional), diameter in kilometers (optional - sometimes unknown),
    and whether it's marked as potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation, name=None,
                 diameter=float("nan"), hazardous='N',
                 approaches=[]):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments
         supplied to the constructor.
        """
        self.designation = designation
        if name == '':
            self.name = None
        else:
            self.name = name
        if diameter == '':
            self.diameter = float('nan')
        else:
            self.diameter = float(diameter)
        if hazardous == 'Y':
            self.hazardous = True
        else:
            self.hazardous = False

        # Create an empty initial collection of linked approaches.
        self.approaches = approaches

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        return f"{self.designation} {self.name}"

    def __str__(self):
        """Return `str(self)`."""
        is_hazardous = "is not"
        if self.hazardous is True:
            is_hazardous = "is"
        else:
            is_hazardous = "is not"
        return (f"Neo {self.fullname} has a diameter of {self.diameter: .3f} "
                f"km and {is_hazardous} potentially hazardous.")

    def __repr__(self):
        """Return `repr(self)`.

        a computer-readable string representation of this object.
        """
        return (f"NearEarthObject(designation={self.designation!r}, "
                f"name={self.name!r}, diameter={self.diameter:.3f}, "
                f"hazardous={self.hazardous!r})")


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach
     to Earth, such as the date and time (in UTC) of closest approach,
     the nominal approach distance in astronomical units,
     and the relative approach velocity in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation, time=None, distance=0.0,
                 velocity=0.0, neo=None):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments
         supplied to the constructor.
        """
        self.designation = designation
        self.time = cd_to_datetime(time)
        if distance == '':
            self.distance = float('nan')
        else:
            self.distance = float(distance)
        if velocity == '':
            self.velocity = float('nan')
        else:
            self.velocity = float(velocity)

        # Create an attribute for the referenced NEO, originally None.
        self.neo = neo

    @property
    def time_str(self):
        """Return formatted representation of approach time of `CloseApproach`.

        The value in `self.time` should be a Python `datetime` object.
         While a `datetime` object has a string representation,
         the default representation includes seconds - significant
         figures that don't exist in our input data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        time_str = datetime_to_str(self.time)
        if self.neo is not None:
            return (f"A CloseApproach ...\n{self.neo.fullname} is "
                    f"{self.distance: .3f} AU away from  Earth as on "
                    f"{time_str}")
        else:
            return (f"A CloseApproach ...\n{self.designation} "
                    f"is {self.distance: .3f} AU away from  Earth "
                    f"as on {time_str}")

    def __repr__(self):
        """Return `repr(self)`.

        a computer-readable string representation of this object.
        """
        return (f"CloseApproach(time={self.time_str!r}, distance= "
                f"{self.distance:.2f}, velocity={self.velocity:.2f}, "
                f"neo={self.neo!r})")
