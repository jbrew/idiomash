********* IDIOMASH *********

Create idioms by mashing up old ones! Nothing new under the weather.

Input: text file with each candidate on a separate line

Output: `mashups_for_seq_with_lines` returns a set

Usage:
`lines = lines_from_path('some/save/path/here.txt')`
`mashups = mashups_for_seq_with_lines('and', lines)`

You can run `prompt_loop(9)` to start a user input loop
in which you select a candidate sequence and see up to 9 (or
any #) randomly chosen mashups pivoting on that sequence.