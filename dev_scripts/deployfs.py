# Builds and uploads static files in data directory
# Usage: pio run -t deploy_fs

Import("env")
import sys
import os

def deploy_filesystem(source, target, env):
    # Build frontend
    result = env.Execute("npm --prefix frontend run build")
    if result != 0:
        print("Filesystem build failed. Exiting.")
        sys.exit(result)

    # Upload filesystem
    result = env.Execute("pio run -t uploadfs")
    if result != 0:
        print("Filesystem upload failed. Exiting.")
        sys.exit(result)

# Register the custom target "deploy_fs"
env.AddTarget("deployfs", None, deploy_filesystem)
