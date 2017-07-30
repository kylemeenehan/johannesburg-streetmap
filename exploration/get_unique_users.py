#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re

def get_user(element):
    return element.attrib['uid']


def get_unique_users(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if 'uid' in element.attrib:
            user = get_user(element)
            if user not in users:
                users.add(user)

    return users