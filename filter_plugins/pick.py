#!/usr/bin/python


def pick(obj, attributes):
    if isinstance(obj, dict):
        return pick_dict(obj, attributes)
    elif isinstance(obj, list):
        return pick_list(obj, attributes)

    raise TypeError('Given object is whether a dictionary nor a list.')


def pick_dict(obj_dict, attributes):
    result_obj = {}
    for key, value in obj_dict.items():
        if key in attributes:
            result_obj[key] = value
    return result_obj


def pick_list(obj_list, attributes):
    result_list = []
    for obj in obj_list:
        result_list.append(pick_dict(obj, attributes))
    return result_list


class FilterModule(object):

    def filters(self):
        return {
            'hetzner_vswitch_pick': pick
        }
