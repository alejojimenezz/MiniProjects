# Over the Wire

## Level 0

`ssh bandit0@bandit.labs.overthewire.org -p 2220`

Password: `bandit0`

## Lavel 1

Find file called readme in home directory

`ls`: List contents of directory
`cd`: Change the directory
`cat`: Concatenate files and print on standard output
`file`: Determine file type
`du`: Estimate file space usage
`find`: Search files in directory

`cat readme`

`ssh bandit1@bandit.labs.overthewire.org -p 2220`

Password: `ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If`

## Level 2

`cat ./-`

`ssh bandit2@bandit.labs.overthewire.org -p 2220`

Password: `263JGJPfgU6LtdEvgfWU1XP5yac29mFx`

## Level 3

`cat "./--spaces in this filename--"`

`ssh bandit3@bandit.labs.overthewire.org -p 2220`

Password: `MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx`

## Level 4

`cd inhere`
`find`
`cat "./...Hiding-From-You"`

`ssh bandit4@bandit.labs.overthewire.org -p 2220`

Password: `2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ`

## Level 5

`cd inhere`
`cat ./-file07`

All other files aren't human readable.

`ssh bandit5@bandit.labs.overthewire.org -p 2220`

Password: `4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw`

## Level 6

Requirements:
- Human-readable
- 1033 bytes
- not executable

`cd inhere`
Directory names: "maybehere##" from 00 to 19

`ls -la maybehere##` - To search in each individual directory

`ls -la ./*` - For every directory

Result: ./maybehere17/-file1 (CHECK)



