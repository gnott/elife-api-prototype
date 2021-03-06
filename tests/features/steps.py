from lettuce import *
import parseNLM as pm
import os

import logging
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler(os.getcwd() + os.sep + 'test.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)

test_xml_path = world.basedir + os.sep +  "sample-xml" + os.sep

@step('I have the document (\S+)')
def have_the_document(step, document):
	world.document = document
	file_location = set_file_location(document)
	world.filecontent = pm.parse_document(file_location)

@step('I get the title') 
def get_the_title(step):
	world.title = pm.title(world.filecontent)

@step('Then I see the string (.*$)')
def then_i_see_the_string(step, string):
	assert world.title == string, \
		"Got %s" % world.title 

@step('I get the doi')
def get_the_doi(step):
	world.doi = pm.doi(world.filecontent)

@step(u'Then I see the identifier (.*$)')
def then_i_see_the_identifier(step, string):
	assert world.doi == string, \
		"Got %s" % world.doi
	
@step('I get the pmid')
def get_the_pmid(step):
	world.pmid = pm.pmid(world.filecontent)

@step(u'Then I see the number (.*$)')
def then_i_see_the_number(step, number):
	if (number == 'None'):
	  number = None
	assert world.pmid == number, \
		"Got %d" % int(world.pmid)

@step('I count the number of authors')
def count_the_number_of_authors(step):
	world.authors_count = len(pm.authors(world.filecontent))

@step(u'Then I count the total authors as (\d+)')
def then_i_count_the_total_authors_as(step, number):
	number = int(number)
	assert world.authors_count == number, \
		"Got %d" % world.authors_count
	
@step('I count the number of references')
def count_the_number_of_references(step):
	world.references_count = len(pm.references(world.filecontent))

@step(u'Then I get the total number of references as (\d+)')
def then_i_get_the_total_number_of_references_as(step, number):
	number = int(number)
	assert world.references_count == number, \
		"Got %d" % world.references_count

@step('When I count references from the year (\d+)')
def count_referneces_from_the_year(step, year):
	world.references_count = 0
	references = pm.refs(world.filecontent)
	for ref in references:
		try:
			if int(ref['year']) == int(year):
				world.references_count += 1
		except(KeyError):
			continue

@step('When I count the number of references from the journal (.*$)')
def count_the_number_of_references_from_the_journal(step, journal):
	if (journal == 'None'):
	  journal = None
	world.references_count = 0
	references = pm.refs(world.filecontent)
	for ref in references:
		try:
			if ref['source'] == journal:
				world.references_count += 1
		except(KeyError):
			if journal == None:
				world.references_count += 1

def set_file_location(doc):
	document = doc.lstrip('"').rstrip('"')
	file_location = test_xml_path + document
	return file_location

	