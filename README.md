
This is a toy problem just demonstrating the basic usage of a map reduce problem.

In Bash to generate the fake data:
python -c "print 50 * 'this is an example document in a corpus\n'" > corpus.txt

after writing out my mappers, combiners, reducers, etc. I run it locally first with like this..

cat corpus.txt | python mapper.py | sort | python reducer.py