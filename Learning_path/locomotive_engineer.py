"""Functions which helps the locomotive engineer to keep track of the train."""
def get_list_of_wagons(*argvs):
    list = []
    for i in argvs:
        list.append(i)
    return list

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    x, y, *rest = each_wagons_id
    one = rest[0]
    remaining = rest[1:]
    return [one] + missing_wagons + remaining + [x, y]


def add_missing_stops(route, **stops):
    route["stops"] = list(stops.values())
    return route
