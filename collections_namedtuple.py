from collections import namedtuple

Std = namedtuple('Student', 'ID MARKS NAME CLASS')

xyz = Std(ID=1, MARKS=97, NAME='Raymond', CLASS=7)
xyz = Std(ID=2, MARKS=50, NAME='Steven', CLASS=6)
xyz = Std(ID=3, MARKS=91, NAME='Adrian', CLASS=5)
xyz = Std(ID=4, MARKS=72, NAME='Stewart', CLASS=4)
xyz = Std(ID=5, MARKS=80, NAME='Peter', CLASS=3)

print(xyz)