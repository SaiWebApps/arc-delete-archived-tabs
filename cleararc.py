#!/usr/bin/env python3

# ==== Imports ==== #
import os
import shutil

# ==== Variables ==== #
HOME_DIR = os.path.expanduser('~')
ARC_ROOT_DIR = os.path.join(HOME_DIR, 'Library', 'Application Support', 'Arc')
ARC_USER_DATA_DIR = os.path.join(ARC_ROOT_DIR, 'User Data', 'Default')

# ==== Methods ==== #
def delete_resource(path: str) -> None:
    if os.path.isfile(path):
        print(f'Deleting file {path}.....')
        os.remove(path)
    else:
        print(f'Deleting directory {path}.....')
        shutil.rmtree(path)

def delete_resources(root_dir_path: str, target_filters: list, exclusive: bool = False) -> None:
    for resource_name in os.listdir(root_dir_path):
        matches = [
            match
            for match in target_filters
            if (exclusive and match.lower() not in resource_name.lower()) or
                (not exclusive and match.lower() in resource_name.lower())
        ]
        if matches:
            resource_path = os.path.join(root_dir_path, resource_name)
            delete_resource(resource_path)

# ==== Main / Driver ==== #
# First, clean up Arc's root directory.
delete_resources(
    ARC_ROOT_DIR,
    [
        'Cache',
        'StorableArchive',
        'StorableWindows',
        'StorableDownload',
        'StorableLiveData',
        'StorableSession',
        'StorableDefaultBrowserPrompts'
    ]
)

# Then, clean up Arc's user data directory.
# Delete everything in this directory that does not contain "Extension" in its name.
delete_resources(ARC_USER_DATA_DIR, ['Cookie', 'Favicon', 'History', 'Login', 'Site'])