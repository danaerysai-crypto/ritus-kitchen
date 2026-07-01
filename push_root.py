import os, subprocess, sys, time

token = os.environ.get('GITHUB_TOKEN', '')
if not token:
    print('GITHUB_TOKEN not set')
    sys.exit(1)

project = r'C:\Users\Admin\Desktop\projects\ritus-kitchen'
user = 'danaerysai-crypto'
repo = 'ritus-kitchen'
remote_url = f'https://{token}@github.com/{user}/{repo}.git'

commands = [
    'git init',
    'git add .',
    'git commit -m "Move website files to root"',
    f'git remote add origin {remote_url}',
    'git branch -M main',
    'git push -u origin main --force'
]

for cmd in commands:
    print(f'\n> {cmd}')
    result = subprocess.run(cmd, shell=True, cwd=project, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout[:500])
    if result.returncode != 0:
        print(f'ERROR: {result.stderr[:500]}')
        sys.exit(1)

print('\nPushed. Waiting 30s for GitHub Pages...')
time.sleep(30)

# Check URL
url = f'https://{user}.github.io/{repo}/'
check = subprocess.run(['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', url], capture_output=True, text=True)
print(f'URL: {url}')
print(f'HTTP status: {check.stdout.strip()}')
