#!/usr/bin/python


def list_to_dict(obj_array, attr='name'):
    obj_dict = {}

    for obj in obj_array:
        key = obj.get(attr)
        obj_dict[key] = obj

    return obj_dict


class FilterModule(object):

    def filters(self):
        return {
            'hetzner_vswitch_list_to_dict': list_to_dict
        }
