# Top Tips!


### Have loads of local git branches (that you've deleted via GitHub after merging)?

1. Use `git branch` or `git branch -a` to list all your current local branches (*`q` to exit*)
2. Delete them individually via `git branch -d "your-branch-name-here"` 

Or, there's an automated way, with grep (USE AT YOUR OWN RISK)

1. Use the following command `git branch --merged | egrep -v "(^\*|master|dev)" | xargs git branch -d`
2. Sit back and relax, but not too much. This command only deletes already merged branches, be careful with discrepancies etc.