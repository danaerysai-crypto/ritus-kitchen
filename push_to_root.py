import json
import urllib.request
import urllib.error
import base64
import os

TOKEN='***'
USER = 'danaerysai-crypto'
REPO = 'ritus-kitchen'

BASE_URL = f'https://api.github.com/repos/{USER}/{REPO}'

HEADERS = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': 'ritus-kitchen-deploy'
}

def api_call(method, path, data=None, extra_headers=None):
    url = f'{BASE_URL}{path}'
    req = urllib.request.Request(url, method=method)
    for k, v in HEADERS.items():
        req.add_header(k, v)
    if extra_headers:
        for k, v in extra_headers.items():
            req.add_header(k, v)
    body = None
    if data is not None:
        body = json.dumps(data).encode()
    try:
        with urllib.request.urlopen(req, data=body) as resp:
            code = resp.status
            text = resp.read().decode()
            return code, json.loads(text) if text else {}
    except urllib.error.HTTPError as e:
        text = e.read().decode()
        try:
            return e.code, json.loads(text)
        except Exception:
            return e.code, {'message': text}

# Test token
status, data = api_call('GET', '')
print('Auth test status:', status)
if status != 200:
    print('Auth failed:', data)
    raise SystemExit

# 1. List remote root
status, root_items = api_call('GET', '/contents/')
print('\nRemote root status:', status)
if status != 200:
    print('Error listing root:', root_items)
    raise SystemExit

print('Remote root items:')
for item in root_items:
    print(' ', item['name'], item['type'])

# 2. Check if nested ritus-kitchen/ folder exists
nested = [i for i in root_items if i['name'] == 'ritus-kitchen' and i['type'] == 'dir']
print('\nNested ritus-kitchen/ dir found:', bool(nested))

if not nested:
    print('No nested folder issue. Checking if order.html exists remotely...')
    has_order = any(i['name'] == 'order.html' for i in root_items)
    print('order.html remote:', has_order)
    if has_order:
        print('Everything already at root. Done.')
        raise SystemExit
    else:
        print('New files are missing on remote. Will create/update them via API.')

# 3. Get all files in nested dir if it exists
files_to_move = []
if nested:
    status, nested_items = api_call('GET', '/contents/ritus-kitchen')
    print('\nNested folder contents status:', status)
    if status != 200:
        print('Error:', nested_items)
        raise SystemExit
    for item in nested_items:
        files_to_move.append(item)

# 4. Move files from nested to root
def move_file(item):
    old_path = item['path']
    new_path = item['name']
    sha = item['sha']
    print(f'\nMoving {old_path} -> {new_path}')
    # For directories, we can't move via contents API; we'll recreate and delete
    if item['type'] == 'dir':
        print(f'  Skipping directory move for now: {old_path}')
        return
    # Get current content
    status, content = api_call('GET', f'/contents/{old_path}')
    if status != 200:
        print(f'  Error fetching content: {content}')
        return
    file_data = {
        'message': f'Move {old_path} to root',
        'content': content['content'],
        'sha': sha,
        'path': new_path,
        'branch': 'main'
    }
    # Create new file at root
    create_status, create_data = api_call('PUT', f'/contents/{new_path}', data=file_data)
    print(f'  Create status: {create_status}', create_data.get('message', ''))
    if create_status not in (200, 201):
        print(f'  Failed to create {new_path}:', create_data)
        return
    # Delete old file
    delete_status, delete_data = api_call('DELETE', f'/contents/{old_path}', data={
        'message': f'Remove nested {old_path}',
        'sha': sha,
        'branch': 'main'
    })
    print(f'  Delete status: {delete_status}', delete_data.get('message', ''))

# Move files
for item in files_to_move:
    move_file(item)

# 5. Delete empty nested directory
if nested:
    # GitHub API doesn't directly delete empty dirs; commit empty tree
    # We can update a file inside to force tree rebuild, but simpler: leave it if empty
    print('\nNote: Empty directory removal requires additional git tree manipulation.')

# 6. Ensure new files exist locally and push them
print('\nDone with API moves.')
