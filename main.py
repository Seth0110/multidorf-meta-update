#!/usr/bin/env python3
from git import Repo
import shutil

META_REPO_URL = "https://github.com/multidorf/multidorf-meta" # TODO accept from command line arg
working_dir = "/tmp/multidorf-update/"
meta_path = working_dir + "meta/" # TODO accept working directory from command line arg

local = Repo.clone_from(META_REPO_URL, meta_path)

# create (if not exists) bay12 directory
# scrape bay12, parse, convert to JSON, store in bay12.json
# do same for dfhack

# do same for dwarf therapist (latest is all that's needed there)

shutil.rmtree(working_dir) # delete repo at the end
