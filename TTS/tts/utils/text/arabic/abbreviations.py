import re

# List of (regular expression, replacement) pairs for abbreviations in english:
abbreviations_ar = [
    (re.compile("\\b%s\\." % x[0], re.IGNORECASE), x[1])
    for x in [
        ("أ.د", "الأستاذ الدكتور"),
        ("أ.م", "الأستاذ المهندس"),
        ("أ.د.م", "الأستاذ الدكتور المهندس"),
        ("أ", "الأستاذ"),
        ("ا", "الأستاذ"),
        ("د", "الدكتور"),
        ("م", "المهندس"),
    ]
]