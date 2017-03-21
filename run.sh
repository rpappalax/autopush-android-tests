
clear
#python -m pytest --driver Remote --host localhost --port 4723 --variables config.json --variables taskcluster.json  tests/test_bookmarks_tabs.py
#python -m pytest --driver Remote --host localhost --port 4723 --variables config.json --variables taskcluster_x86.json  tests/test_bookmarks_tabs.py
./venv/bin/python -m py.test --driver Remote --host localhost --port 4723 --variables config.json --variables taskcluster_x86.json  tests/test_bookmarks_tabs.py
