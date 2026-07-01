import os, json, subprocess, sys

token = os.environ['GITHUB_TOKEN']

def curl(method, url, data=None):
    cmd = [
        'curl', '-s', '-X', method,
        '-H', f'Authorization: token {token}',
        '-H', 'Accept: application/vnd.github.v3+json',
        url
    ]
    if data is not None:
        cmd += ['-d', json.dumps(data)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(f'\n{method} {url}')
    print(f'stdout: {result.stdout[:500]}')
    if result.returncode != 0:
        print(f'stderr: {result.stderr}')
    return result

# Get user
r = curl('GET', 'https://api.github.com/user')
if r.returncode != 0:
    sys.exit(1)
user = json.loads(r.stdout)
login = user['login']
print(f'User: {login}')

# Create repo
repo_data = {
    'name': 'ritus-kitchen',
    'description': "Ritu's Kitchen home-cooked pre-order website",
    'private': False,
    'auto_init': False
}
r = curl('POST', 'https://api.github.com/user/repos', repo_data)
if r.returncode != 0:
    sys.exit(1)
repo_resp = json.loads(r.stdout)
if 'html_url' not in repo_resp:
    print('Repo creation failed or already exists:', repo_resp)
else:
    print(f'Repo: {repo_resp["html_url"]}')

# Init git and push
cmds = [
    'git init',
    'git add .',
    'git commit -m "Initial website"',
    f'git remote add origin https://{token}@github.com/{login}/ritus-kitchen.git',
    'git branch -M main',
    'git push -u origin main --force'
]
for c in cmds:
    print(f'\n> {c}')
    result = subprocess.run(c, shell=True, capture_output=True, text=True, cwd=r'C:\Users\Admin\Desktop\projects\ritus-kitchen')
    print(result.stdout[:500])
    if result.returncode != 0:
        print(f'ERROR: {result.stderr[:500]}')

# Enable Pages
pages_data = {
    'source': {'branch': 'main', 'path': '/'}
}
r = curl('POST', f'https://api.github.com/repos/{login}/ritus-kitchen/pages', pages_data)
print(f'Pages response: {r.stdout[:500]}')

print(f'\nLive URL will be: https://{login}.github.io/ritus-kitchen/')
print('(Allow 1-2 minutes for DNS)')
