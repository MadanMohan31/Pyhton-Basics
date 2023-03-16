# dictionaries are used to convert a small word to its meaningful word
# dictionaries are represented in {}

monthconversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# convert the 3 letter word to full word.
print(monthconversions["Nov"])

# .get will print the full word if found.
print(monthconversions.get("Dec"))
print(monthconversions.get("Oct", "Not a valid key"))

# .get will print NONE or message typed, if not found.
print(monthconversions.get("Luv"))
print(monthconversions.get("Luv", "Not a valid key"))
