# FSOP explorer
A tool to find and inspect File Stream Oriented Programming (FSOP) code paths. Heavily inspired by KyleBot's [angry-FSROP](https://github.com/Kyle-Kyle/angry-FSROP) repository.

# Why?
To find the conditions leading to an FSOP code path more easily and to learn more about [angr](https://docs.angr.io/). Read my [blog post](https://niftic.ca/posts/fsop/) on FSOP for more details.

# How to use
First, install [angr](https://docs.angr.io/) (use `requirements.txt` if you want to use the outputs I generated).
Then, generate some outputs using the `angry-fsrop.py` script, which takes a couple of hours. Alternatively, use the already generated outputs from GLIBC 2.35.
Finally, use `examine_paths.py` to inspect a specific output.
~~~sh
python examine_paths.py --file outputs/_IO_file_finish.pickle --mode best
~~~
