github_star_and_delete_fork
===========================

I had a large number of forks in my github account that were unedited and
should be starred, not forked. This script achieves that by looping through
all my repositories having parents, starring them, and deleting them, leaving
only repositories that I have originated myself.

    git clone https://github.com/davidthewatson/github_star_and_delete_fork.git
    cd github_star_and_delete_fork
    virtualenv --no-site-packages venv
    source venv/bin/activate
    pip install -r requirements.txt
    export GITHUB_USERNAME=your_username
    export GITHUB_PASSWORD=your_password
    python sdf.py

<a href="http://davidwatson.org/">david watson</a>
