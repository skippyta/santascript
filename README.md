#Ta Family SantaScript

##About
This script was originally written back in 2013 with the intent of simplifying my family's annual
Secret Santa drawing process. We used to use an actual hat and paper, which was occasionally prone
to error, so I decided to set the process in stone as a piece of code. Frankly, this code isn't very
general, and now its structure generally served as a way of familiarizing myself with features in Python
3. I think I sort of went overboard on type annotations, but I sort of couldn't help myself there.

Really, this is kind of my "EnterpriseFizzBuzz" submission for Secret Santa drawings. It's really
overdone for its incredibly niche purpose, but I had fun with it. Hopefully it won't age horribly.

##Assumptions and Constraints
* The configured number of gifts per person is the same for ALL recipients
* The configured number of gifts per person is less than the number of possible Secret Santas for an
individual (number of Secret Santas - 1)
* 
* A "Santa" represents one gift-giving entity. I could have created separate person rows for each member
of a couple, but decided that would be a data modeling headache that was well beyond the scope of what
we're trying to accomplish here.
* Nuclear relatives cannot been drawn together. This is just how our family works - Secret Santa is
for all of the extended family, and the nuclear family buys each other gifts by default with no need
for this madness.
* No Secret Santa will have duplicate names drawn. This will result in a redraw.
* The script requires you to pass in the path to the CSV and the number of gifts per recipient as
arguments. It doesn't really sanity check here, so just don't be a butt about it and be sure to specify.

##CSV Conventions
For the CSV input, note that the structure is:

`Person Name,Family Name,Person Type`

Person Type can be Santa, Santee, or Exempt. I added Exempt as a sort of halfhearted way of documenting
that someone should be kept track of, but shouldn't be included in the drawing in any way since they're
probably babies and are going to get presents from everyone regardless.

Santas are potential present givers; Santees are potential gift recipients; and Exempt people are not
included at all.

##Usage
Once you include all of the modules in your Python environment, running this is pretty straightforward.

`python santascript.py path_to_csv.csv 2`

##Afterthoughts
In most Secret Santa scenarios, all of the Santas are actually eligible to receive gifts. That isn't
the case here, but it should be relatively easy to change the data model around to allow for that.
Alternatively, you could just add extra rows in the CSV for those people to be represented as recipients
("Santees") to make it work in the current model.

This is a pretty heavy-handed way of approaching a shuffling problem, mostly because of the arbitrary
constraints I added around relatives and duplicity. Oh well, at least it was fun to write!
