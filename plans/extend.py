#!/usr/bin/env python3

from six.moves import xmlrpc_client as xmlrpclib
import xml.etree.ElementTree  as xml
import requests
import os

lab_controller_url = os.getenv('BEAKER_LAB_CONTROLLER_URL')
recipe_id = os.getenv('BEAKER_RECIPE_ID')

r = requests.get(f"{lab_controller_url}recipes/{recipe_id}")
tree = xml.fromstring(r.text)
task_id = tree.findall("./recipeSet/recipe/task/[@status='Running']")[0].attrib["id"]
print(task_id)

server = xmlrpclib.ServerProxy(lab_controller_url)
print(server.extend_watchdog(task_id, 86400))


