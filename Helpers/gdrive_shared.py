#!/usr/bin/env python

from __future__ import print_function
import time
import ast

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/drive.readonly.metadata'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
    creds = tools.run_flow(flow, store)

service = discovery.build('drive', 'v3', http=creds.authorize(Http()))
results = service.files().list(
        pageSize=1000,
        fields="nextPageToken, files(name, shared)").execute()
token = results.get('nextPageToken', None)
items = results.get('files', [])

while token is not None:
    results = service.files().list(
            pageSize=1000,
            pageToken=token,
            fields="nextPageToken, files(name, shared)").execute()
    # Store the new nextPageToken on each loop iteration
    token = results.get('nextPageToken', None)
    # Append the next set of results to the items variable
    items.extend(results.get('files', []))

# The Google Drive does not return valid JSON because the property
# names are not enclosed in double quotes, they are enclosed in
# single quotes. So, use Python AST to convert the string to an
# iterable list.
items_dict = ast.literal_eval(str(items))

print("You have", len(items_dict), "files in Google Drive\n")
print("The following files are shared:\n")

# Iterate through the items list and only show files that have
# shared set to True.
for i in range(len(items_dict)):
    if items_dict[i]['shared']:
        print(items_dict[i]['name'])
