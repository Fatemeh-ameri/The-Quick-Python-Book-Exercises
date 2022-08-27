"""LAB 6: PREPROCESSING TEXT In processing raw text, it’s quite often necessary
to clean and normalize the text before doing anything else. If you want to
find the frequency of words in text, for example, you can make the job easier
if, before you start counting, you make sure that everything is lowercase (or
uppercase, if you prefer) and that all punctuation has been removed. You can
also make things easier by breaking the text into a series of words. In this lab,
the task is to read the first part of the first chapter of Moby Dick (found in the
book's source code), make sure that everything is one case, remove all punc-
tuation, and write the words one per line to a second file. Because I haven’t
yet covered reading and writing files, here’s the code for those operations:
with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
for line in infile:
# make all one case
# remove punctuation
# split into words
# write all words for line
outfile.write(cleaned_words)"""


import re

with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        # make all one case
        line=line.lower()

        # remove punctuation
        line = re.sub(r'[^\w\s]', ' ', line)

        # split into words
        line = line.split()

        # write all words for line
        if len(line) > 0:
            line = "\n".join(line)
            print(line)
            outfile.write(line)

"""call
me
ishmael
some
years
ago
never
mind
how
long
precisely
having
little
or
no
money
in
my
purse
and
nothing
particular
to
interest
me
on
shore
i
thought
i
would
sail
about
a
little
and
see
the
watery
part
of
the
world
it
is
a
way
i
have
of
driving
off
the
spleen
and
regulating
the
circulation
whenever
i
find
myself
growing
grim
about
the
mouth
whenever
it
is
a
damp
drizzly
november
in
my
soul
whenever
i
find
myself
involuntarily
pausing
before
coffin
warehouses
and
bringing
up
the
rear
of
every
funeral
i
meet
and
especially
whenever
my
hypos
get
such
an
upper
hand
of
me
that
it
requires
a
strong
moral
principle
to
prevent
me
from
deliberately
stepping
into
the
street
and
methodically
knocking
people
s
hats
off
then
i
account
it
high
time
to
get
to
sea
as
soon
as
i
can
this
is
my
substitute
for
pistol
and
ball
with
a
philosophical
flourish
cato
throws
himself
upon
his
sword
i
quietly
take
to
the
ship
there
is
nothing
surprising
in
this
if
they
but
knew
it
almost
all
men
in
their
degree
some
time
or
other
cherish
very
nearly
the
same
feelings
towards
the
ocean
with
me

there
now
is
your
insular
city
of
the
manhattoes
belted
round
by
wharves
as
indian
isles
by
coral
reefs
commerce
surrounds
it
with
her
surf
right
and
left
the
streets
take
you
waterward
its
extreme
downtown
is
the
battery
where
that
noble
mole
is
washed
by
waves
and
cooled
by
breezes
which
a
few
hours
previous
were
out
of
sight
of
land
look
at
the
crowds
of
water
gazers
there"""        
        