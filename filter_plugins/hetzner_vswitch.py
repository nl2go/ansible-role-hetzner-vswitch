
from ansible_filter import pick
from ansible_filter import change_set
from ansible_filter import form_urlencode
from ansible_filter import group_by
from ansible_filter import helpers


class FilterModule(object):

    def filters(self):
        return {
            'hetzner_vswitch_pick': pick.pick,
            'hetzner_vswitch_change_set': change_set.change_set,
            'hetzner_vswitch_form_urlencode': form_urlencode.form_urlencode,
            'hetzner_vswitch_group_by': group_by.group_by,
            'hetzner_vswitch_list_to_dict': helpers.array_to_dict,
        }
