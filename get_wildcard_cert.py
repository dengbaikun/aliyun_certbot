#!/usr/bin/env python
from pathlib import Path
import subprocess
from utils.config import global_config


def get_wildcard_cert(domain):
    try:
        project_root = Path(__file__).resolve().parent
        # Run Certbot command to obtain wildcard certificate
        command = [
            'certbot',
            'certonly',
            '--manual',
            '--preferred-challenges=dns',
            '-d', f'{domain}',
            '-d', f'*.{domain}',
            '--server', 'https://acme-v02.api.letsencrypt.org/directory',  # Use ACME v2 API endpoint
            '--manual-auth-hook', str(project_root / 'certbot_dns' / 'auth_hook.sh'),
            # Script to automate DNS challenge
            '--manual-cleanup-hook', str(project_root / 'certbot_dns' / 'cleanup_hook.sh'),
            # Script to clean up DNS challenge
            '--config', str(project_root / 'cli.ini'),
        ]
        print(" ".join(command))
        subprocess.run(command, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    domain_name = global_config.getRaw('aliyun', 'domain_name')  # Replace with your domain
    get_wildcard_cert(domain_name)
