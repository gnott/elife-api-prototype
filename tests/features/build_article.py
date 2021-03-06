from lettuce import *
import os
import log
import settings
from article import article

test_xml_path = world.basedir + os.sep +  "sample-xml" + os.sep

world.a = {}

@step('And I set the article file location')
def set_the_article_file_location(step):
	world.article = article()
	world.article.set_file_location(test_xml_path, world.document)

@step('And I use the parser (\S+)') 
def i_use_the_parser(step, parser):
	assert world.article.pm.__name__ == parser, \
		"Got %s" % world.article.pm 

@step('I parse the document') 
def parse_the_document(step):
	world.article.parse_document()
	# Save the object in world for later, keyed by DOI
	world.a[world.article.doi] = world.article

@step('The article object has the doi (.*$)')
@step('And the article object has the doi (.*$)')
def the_article_object_has_the_doi(step, string):
	assert world.article.doi == string, \
		"Got %s" % world.article.doi

@step('Given I have an article object with the doi (.*$)')
def i_have_an_article_object_with_the_doi_doi(step, doi):
	try:
	  world.article = world.a[doi]
	except KeyError:
		assert False, \
			"No object with doi %s" % doi
	
@step('And the article has parsed an XML document')
def the_article_has_parsed_an_XML_document(step):
	assert world.article.parsed == True

@step('And the article object has the property (.*$)')
def the_article_object_has_the_property_value(step, property):
	world.property = property
	
@step('Then the article object property has the value (.*$)')
def the_article_object_property_has_the_value(step, value):
	property = eval('world.article.' + world.property)
	if (value == 'None'):
	  value = None
	if (value == 'True'):
	  value = True
	if (value == 'False'):
	  value = False
	try:
		assert int(property) == int(value), \
		"Got %s" % property
	except (ValueError, TypeError):
		assert property == value, \
		"Got %s" % property
	
@step('Then the article object property has the total length (.*$)')
def the_article_object_property_has_the_total_length(step, length):
	property = eval('world.article.' + world.property)
	if(type(property) == list):
		property_length = len(property)
	elif(property != None):
		property_length = 1
	else:
		property_length = 0

	assert property_length == int(length), \
		"Got %s" % property_length
	
