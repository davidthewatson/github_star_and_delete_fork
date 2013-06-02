github_star_and_delete_fork
===========================

I had a large number of forks in my github account that were unedited and
should be starred, not forked. This script achieves that be looping through
all my repositories having parents, starring them, and deleting them, leaving
only repositories that I have originated myself.

git clone https://github.com/davidthewatson/github_star_and_delete_fork.git
cd github_star_and_delete_fork
virtualenv --no-site-packages
pip install requirements.txt
export GITHUB_USERNAME=your_username
export GITHUB_PASSWORD=your_password
python sdf.py
