#!/usr/bin/python


def group_by(lefts, rights, attr='name'):
    results = []
    rights_dict = array_to_dict(rights, attr)
    for left in lefts:
        key = left.get(attr)
        result = {attr: key, 'group': [left]}
        right = rights_dict.get(key)
        if right:
            result['group'].append(right)
            results.append(result)
    return results


def array_to_dict(obj_array, attr='name'):
    obj_dict = {}

    for obj in obj_array:
        key = obj.get(attr)
        obj_dict[key] = obj

    return obj_dict


class FilterModule(object):

    def filters(self):
        return {
            'hetzner_vswitch_group_by': group_by
        }
