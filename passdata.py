#!/usr/bin/env python3


class passdata:
    import types

    def __init__(self):

        self.x = 100

        self.ppass_available = [1000, 2000, 3000]

        self.ppass_used = [500]

        self.unit_dict = {10: (100, 200), 20: (300, 400), 30: (800)}

        self.owner_names = {10: "Bob Smith", 20: "Mike Smith", 30: "Alice Smith"}

        self.ppass_to_add = [1111, 2222]


def get_unit_data(unit_dict):
    """Read the unit to passes dictionary and output the
    passes assigned to a unit"""

    if unit_dict is None:
        unit_dict = {}

    return unit_dict


def get_ppass_used(ppass_used):
    """read the used p pass list and output the used ppasses"""
    if ppass_used is None:
        ppass_used

    return ppass_used


def update_unit_dict(unit_dict, unit_number, updated_pass):
    """update the unit dictionary with the new parking pass info"""

    unit_dict[unit_number] = updated_pass

    return unit_dict


def reclaim_pass_from_pool():
    """reclaim the pass from the pool"""
    pass


def destroy_pass_from_pool():
    """permanently remove passes from pool"""
    pass


def add_new_passes_to_pool(ppass_available=[], ppass_to_add=[]):
    """add new passes to pool

    input:
    ppass_available list, current pass list
    ppass_to_add, list, numbers to add to list

    return: ppass_available list with additions
    """
    if ppass_to_add is None:
        ppass_to_add = []

    if ppass_available is None:
        ppass_available = []

    ppass_available = [ppass_available.append(passid) for passid in ppass_to_add]

    return ppass_available


def check_if_pass_exists():
    """check the assinged pool(s) to see if the pass exists

    returns bool
    """
    pass


def populate_and_dedup_pass(ppass_used, unit_dict, ppass_available):
    """populate the in use passes and de-dupe

    opportunity for set use here"""
    # TODO:

    if ppass_available is None:
        ppass_available = []
    if ppass_used is None:
        ppass_used = []
    if unit_dict is None:
        unit_dict = []

    comparelist = []
    comparetuple = ()
    uk = [i for i in unit_dict.keys() if type(unit_dict[i]) is not type(comparelist)]
    # z = [i for i in unit_dict[uk]]
    # z = [i for i in uk for q in unit_dict[i] if i is not None]

    z = [i for i in unit_dict.keys() if unit_dict[i] is not None]  # works gets keys

    print("[*] zee printing")
    print("[*] z: {}".format(z))
    pass


def assign_pass_from_pool(ppass_available):
    """reads the open pool and assigns next passes"""
    if ppass_available is None:
        ppass_available = []

    # needs some logic about max pass number 2 and what to do if pool is empty

    return ppass_available.pop()


def print_header(sp_val=30):
    print("{0:30} {1:30} {2:30}".format("Unit", "Owner", "Pass"))  # header
    print("=" * 90)


def list_pass_assignments(owner_names, unit_dict):
    """list the pass assignments by unit / owner_name / passes"""

    sp_val = 30  # separator value
    if unit_dict is None:
        unit_dict = {}

    print_header()
    comparelist = [1, 1]
    comparetuple = (1, 1)
    for x in unit_dict.keys():
        if type(unit_dict[x]) != type(comparelist) and type(unit_dict[x]) != type(
            comparetuple
        ):
            print(
                "{0:30} {1:30} {2:30}".format(
                    str(x), str(owner_names[x]), str(unit_dict[x])
                )
            )
        else:
            if len(unit_dict[x]) > 1:
                for num_pass in unit_dict[x]:
                    print(
                        "{0:30} {1:30} {2:30}".format(
                            str(x), str(owner_names[x]), str(num_pass)
                        )
                    )


if __name__ == "__main__":

    pd = passdata()

    populate_and_dedup_pass(pd.ppass_used, pd.unit_dict, pd.ppass_available)

    update_unit_dict(pd.unit_dict, 10, [90, 92])

    # print(get_unit_data(pd.unit_dict))
    # print(get_ppass_used(pd.ppass_used))
    print("used: {}".format(get_ppass_used(pd.ppass_used)))

    print("available: {}".format(get_ppass_used(pd.ppass_available)))

    print("=" * 90)
    list_pass_assignments(pd.owner_names, pd.unit_dict)

    # add new pass example
    ppass_available = add_new_passes_to_pool(
        ppass_available=pd.ppass_available, ppass_to_add=pd.ppass_to_add
    )
    print("ppass_available: {}".format(pd.ppass_available))
