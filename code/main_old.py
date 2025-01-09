"""
	!! ALTE DATEI -- siehe jetzt main.py!!
"""

import inspect

# Fail and Pass
def code_fail():
	print("CodeIsNotValid") 
	exit()

def code_pass():
	print("CodeIsValid")

# Klassen laden
from dataset import DataSetItem
from implementation import DataSet

# Attribute pruefen
d1 = DataSet()
if not all(hasattr(d1, a) for a in [
		"iterate_sorted", "iterate_reversed", "iterate_key",
		"ITERATE_SORT_BY_NAME", "ITERATE_SORT_BY_ID"
	]):
		code_fail()

# Einfuegen prüfen
d2_items = []
d2 = DataSet()
for i in range(20):
	item = DataSetItem(chr(i+65), 20-i, chr(i+97))
	d2_items.append(item)
	d2 += item 

if len(d2) != 20:
	code_fail()
if d2["A"].content != "a":
	code_fail()

d2["Z"] = (0, "zz")
if len(d2) != 21:
	code_fail()
if isinstance(d2["Z"], DataSetItem) and d2["Z"].id == 0:
	d2_items.append(d2["Z"])
else:
	code_fail()

# Iteration
for item, check in zip(d2, d2_items):
	if item != check:
		code_fail()

d2.set_iteration(sort=False)
for item, check in zip(d2, d2_items):
	if item != check:
		code_fail()

d2.set_iteration(sort=True, reverse=True)
d2_items.reverse()
for item, check in zip(d2, d2_items):
	if item != check:
		code_fail()

code_pass()