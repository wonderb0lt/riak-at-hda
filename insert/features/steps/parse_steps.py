from behave import *
from hamcrest import *
import sys
import os.path
import riakparse

sys.path.append('../../') # Still haven't found the solution for that B[

@given('testfile "{f}"')
def read_testfile(ctx, f):
	ctx.txt = open(os.path.join('testfiles', f), 'r').read()

@when('parsing')
def parse_from_txt(ctx):
	ctx.parsed = riakparse.parse(ctx.txt)

@then('field "{key}" should be "{value}"')
def check_field(ctx, key, value):
	assert_that(ctx.parsed, has_key(key))
	assert_that(ctx.parsed[key], is_(value))

@then('passengers should include {name} ({persontype})')
def check_passenger(ctx, name, persontype):
	assert_that(ctx.parsed, has_key('passengers'))
	assert_that({name: int(persontype)}, is_in(ctx.parsed['passengers']))