After turning up empty handed for a tool to extract the .cat/.dat files, I wrote a quick Python script to extract the data. This script makes a few assumptions, one of which I'm sure is not correct (that files which exist in multiple archives should not be handled..I imagine these are patched assets? not quite sure how to handle them).

Feel free to improve upon this script. To use it, just chuck it into the X Rebirth directory (the one that contains all of the .cat and .dat files), and run it. It will create a new directory called 'out', which will contain all of the extracted assets in their original directory structure.
