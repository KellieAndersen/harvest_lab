############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
 
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(
    "musk",
    1998,
    "green",
    True,
    True,
    "Muskmelon"
    )
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    casaba = MelonType(
    "cas",
    2003,
    "orange",
    False,
    False,
    "Casaba"
    )
    casaba.add_pairing("strawberries", "mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType(
    "cren",
    1996,
    "green",
    False,
    False,
    "Crenshaw"
    )
    crenshaw.add_pairing("proscuitto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType(
    "yw",
    2013,
    "yellow",
    False,
    True,
    "Yellow Watermelon"
    )
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon_type in melon_types:
        print(f'{melon_type.name} pairs with\n {melon_type.pairings}\n')
        
    return None

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTmypes and returns a dictionary of melon type by code."""
    
    melon_lookup = {}
    for melon_type in melon_types:
        if melon_type.code not in melon_lookup:
            melon_lookup[melon_type.code] = melon_type

    return melon_lookup


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, number, melon_type, shape_rating, color_rating, field_no, worker):
        self.number = number
        self.melon_type = melon_type 
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_no = field_no
        self.worker = worker

    def is_sellable(self, melon_number)
        if self.shape_rating > 5 & self.color_rating > 5 & self.field_no != 3:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



