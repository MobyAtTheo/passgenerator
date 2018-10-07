#!/usr/bin/env python3


class passdata:
    import types

    def __init__(self):

        self.x = 100

        self.ppass_available = [100, 200, 300]

        self.ppass_used = [500]

        self.unit_dict = {10: (100, 200), 20: (300, 400), 30: (800)}

        self.owner_names = {10: "Bob Smith", 20: "Mike Smith", 30: "Alice Smith"}


def get_unit_data(unit_dict):
    if unit_dict is None:
        unit_dict = {}

    return unit_dict


def get_ppass_used(ppass_used):
    if ppass_used is None:
        ppass_used

    return ppass_used


def update_unit_dict(unit_dict, unit_number, updated_pass):
    """update the unit dictionary with the new parking pass info"""

    unit_dict[unit_number] = updated_pass

    return unit_dict


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

    update_unit_dict(pd.unit_dict, 10, [90, 92])

    # print(get_unit_data(pd.unit_dict))
    # print(get_ppass_used(pd.ppass_used))
    print("used: {}".format(get_ppass_used(pd.ppass_used)))

    print("available: {}".format(get_ppass_used(pd.ppass_available)))

    print("=" * 90)
    list_pass_assignments(pd.owner_names, pd.unit_dict)
