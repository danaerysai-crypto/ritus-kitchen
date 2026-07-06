import os, json, subprocess, sys

token = os.environ.get('GITHUB_TOKEN', '')
if not token:
    print('GITHUB_TOKEN not set')
    sys.exit(1)

user = 'danaerysai-crypto'
repo = 'ritus-kitchen'
base_url = f'https://api.github.com/repos/{user}/{repo}/contents'
auth_header = f'Authorization: token {token}'

# Files to delete from root (duplicates already in images/)
files_to_delete = [
    'deploy.py',
    'push_root.py',
    'alex-morgan-jazz-corporate-background-music-556245.mp3',
    'ritu-aloo-bhaaji.jpg',
    'ritu-avocado-toast.jpg',
    'ritu-broccoli-almond-soup.jpg',
    'ritu-cheese-garlic-bread.jpg',
    'ritu-dal-tadka.jpg',
    'ritu-empty-thali.jpg',
    'ritu-evening-kitchen.jpg',
    'ritu-hero-dawn-chai.jpg',
    'ritu-hero-filter-coffee.jpg',
    'ritu-honey-chilli-potato.jpg',
    'ritu-idli-sambar.jpg',
    'ritu-jeera-rice.jpg',
    'ritu-jowar-roti.jpg',
    'ritu-kadha-prashad.jpg',
    'ritu-muesli-bowl.jpg',
    'ritu-mushroom-soup.jpg',
    'ritu-omelet-bread.jpg',
    'ritu-paneer-tikka.jpg',
    'ritu-paysum.jpg',
    'ritu-poori-frying.jpg',
    'ritu-popcorn.jpg',
    'ritu-pumpkin-soup.jpg',
    'ritu-seasonal-sabji.jpg',
    'ritu-sindhi-gujarati-breakfast.jpg',
    'ritu-spice-explosion.jpg',
    'ritu-thali-salad.jpg',
    'ritu-tiffin-lunchbox.jpg',
]

def get_sha(path):
    cmd = [
        'curl', '-s',
        '-H', auth_header,
        '-H', 'Accept: application/vnd.github.v3+json',
        f'{base_url}/{path}'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return None
    try:
        data = json.loads(result.stdout)
        return data.get('sha')
    except Exception:
        return None

deleted = []
failed = []

for filename in files_to_delete:
    sha = get_sha(filename)
    if not sha:
        failed.append(f'{filename}: not found')
        continue

    data = {
        'message': f'Remove duplicate file {filename}',
        'sha': sha
    }
    cmd = [
        'curl', '-s', '-X', 'DELETE',
        '-H', auth_header,
        '-H', 'Accept: application/vnd.github.v3+json',
        f'{base_url}/{filename}',
        '-d', json.dumps(data)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        deleted.append(filename)
        print(f'Deleted: {filename}')
    else:
        failed.append(f'{filename}: {result.stdout[:200]} {result.stderr[:200]}')

print(f'\nDeleted: {len(deleted)}')
if failed:
    print(f'Failed: {len(failed)}')
    for f in failed:
        print(f)
