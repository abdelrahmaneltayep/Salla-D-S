#!/usr/bin/env python3
"""Upload a finished video (the 1080p preview) to the Mennatullah Google Drive folder.

Usage: python3 upload_drive.py <file.mp4> [folder_id]
Default folder: "Mennatullah"  https://drive.google.com/drive/folders/1K_kdbWRYsrqFZ95Gz4v7vnR5XigQQb4B

Credentials come from environment variables only (never written to disk or printed):
  GDRIVE_CLIENT_ID, GDRIVE_CLIENT_SECRET  - a Google OAuth client (Web application, redirect https://developers.google.com/oauthplayground)
  GDRIVE_REFRESH_TOKEN                    - refresh token for that client, scope https://www.googleapis.com/auth/drive
Uses the Drive v3 resumable upload; prints the file's Drive link when done.
"""
import json, os, subprocess, sys

FOLDER = "1K_kdbWRYsrqFZ95Gz4v7vnR5XigQQb4B"


def curl(args, data=None):
    r = subprocess.run(["curl", "-sS", "--fail-with-body", *args], input=data, capture_output=True)
    if r.returncode:
        sys.exit(f"Drive request failed: {(r.stdout or r.stderr)[:400].decode(errors='replace')}")
    return r.stdout


def main():
    path = sys.argv[1]; folder = sys.argv[2] if len(sys.argv) > 2 else FOLDER
    need = ["GDRIVE_CLIENT_ID", "GDRIVE_CLIENT_SECRET", "GDRIVE_REFRESH_TOKEN"]
    missing = [k for k in need if not os.environ.get(k)]
    if missing:
        sys.exit("Missing environment variables: " + ", ".join(missing))
    tok = json.loads(curl(["https://oauth2.googleapis.com/token",
        "-d", f"client_id={os.environ['GDRIVE_CLIENT_ID']}", "-d", f"client_secret={os.environ['GDRIVE_CLIENT_SECRET']}",
        "-d", f"refresh_token={os.environ['GDRIVE_REFRESH_TOKEN']}", "-d", "grant_type=refresh_token"]))["access_token"]
    meta = json.dumps({"name": os.path.basename(path), "parents": [folder]}).encode()
    head = subprocess.run(["curl", "-sS", "-D", "-", "-o", "/dev/null", "-X", "POST",
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=resumable&supportsAllDrives=true",
        "-H", f"Authorization: Bearer {tok}", "-H", "Content-Type: application/json; charset=UTF-8",
        "-H", "X-Upload-Content-Type: video/mp4", "--data-binary", "@-"], input=meta, capture_output=True).stdout.decode()
    loc = next((l.split(":", 1)[1].strip() for l in head.splitlines() if l.lower().startswith("location:")), None)
    if not loc:
        sys.exit("Could not start the upload: " + head.splitlines()[0] if head else "no response")
    f = json.loads(curl(["-X", "PUT", loc, "-H", "Content-Type: video/mp4", "--data-binary", f"@{path}"]))
    print(f"Uploaded {f['name']} -> https://drive.google.com/file/d/{f['id']}/view")


if __name__ == "__main__":
    main()
