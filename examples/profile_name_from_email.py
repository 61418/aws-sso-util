# Example formatter for aws-sso-util configure populate.
# Use with: aws-sso-util configure populate --profile-name-process "python3 profile_name_from_email.py"

import os
import re
import sys


account_name = sys.argv[1]

account_email = os.environ.get("AWS_SSO_UTIL_ACCOUNT_EMAIL", "")
email_local_part, separator, _ = account_email.partition("@")

name_source = email_local_part if separator else account_name
profile_name = re.sub(r"[^A-Za-z0-9._-]+", "-", name_source).strip("._-").lower()

print(profile_name)
