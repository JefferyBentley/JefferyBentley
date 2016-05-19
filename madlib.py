"""PDX Code Guild Curriculum, Hello world. """

__author__ = "Jeffery Bentley"
__copyright__ = "Copyright 2016, PDX Code Guild"
__version__ = "0.1"

#madlib.py

#print('Now is the time for all good men to come to the aid of their country, all those who wander are not'
#'lost. It was the best of times it was the worst of times and it and we are definitely in hard times '
#

input_one = input("Enter a noun: ")
print()
#print(
#' A three dimensional square is called a cube'
#

input_two = input("Enter an adverb: ")
print()
#print(
#' Sometimes the phenomonon that we are experiencing is distorted by our preconceptions of the '
#' phenomonon observed '
#
input_three = input("Enter a verb: ")
print()
#print(
#' When She said that we don''t never do this she was using a double negative')

my_mad_lib = ''' Now is the time for all good men to {one} to the aid of their country,
all {three} who wander are not lost. It was the best of times it {two} the worst of times
and it and we are definitely in hard times
This is the {one} I am using. It is the {two} text, ever.
If you do not like my {three}, you can make it your own. '''

my_transformed_mad_lib = my_mad_lib.format(
one = input_one,
two = input_two,
three = input_three
#plural_pronoun = input_plural_pronoun

)
print(my_mad_lib)
print()
print(my_transformed_mad_lib)
