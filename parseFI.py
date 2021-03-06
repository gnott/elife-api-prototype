from fom.session import Fluid
from fom.mapping import Namespace, Tag
from fom.mapping import Object, tag_value, readonly_tag_value
import settings
import time
import calendar
import article
import json

# Fluidinfo parser

session = Fluid()

class fi_article(Object):
	about = readonly_tag_value(u'fluiddb/about')
	doi = tag_value(settings.namespace + '/article/doi')
	doi_url = tag_value(settings.namespace + '/article/doi_url')
	pmid = tag_value(settings.namespace + '/article/pmid')
	journal_id = tag_value(settings.namespace + '/article/journal_id')
	journal_title = tag_value(settings.namespace + '/article/journal_title')
	journal_issn_ppub = tag_value(settings.namespace + '/article/journal_issn_ppub')
	journal_issn_epub = tag_value(settings.namespace + '/article/journal_issn_epub')
	publisher = tag_value(settings.namespace + '/article/publisher')
	article_title = tag_value(settings.namespace + '/article/article_title')
	abstract = tag_value(settings.namespace + '/article/abstract')
	article_type = tag_value(settings.namespace + '/article/article_type')
	article_institution = tag_value(settings.namespace + '/article/article_institution')
	article_country = tag_value(settings.namespace + '/article/article_country')
	subject_area = tag_value(settings.namespace + '/article/subject_area')
	research_organism = tag_value(settings.namespace + '/article/research_organism')
	correspondence = tag_value(settings.namespace + '/article/correspondence')
	author_notes = tag_value(settings.namespace + '/article/author_notes')
	keywords = tag_value(settings.namespace + '/article/keywords')
	pub_date_date = tag_value(settings.namespace + '/article/pub_date_date')
	pub_date_day = tag_value(settings.namespace + '/article/pub_date_day')
	pub_date_month = tag_value(settings.namespace + '/article/pub_date_month')
	pub_date_year = tag_value(settings.namespace + '/article/pub_date_year')
	pub_date_timestamp = tag_value(settings.namespace + '/article/pub_date_timestamp')
	received_date_date = tag_value(settings.namespace + '/article/received_date_date')
	received_date_day = tag_value(settings.namespace + '/article/received_date_day')
	received_date_month = tag_value(settings.namespace + '/article/received_date_month')
	received_date_year = tag_value(settings.namespace + '/article/received_date_year')
	received_date_timestamp = tag_value(settings.namespace + '/article/received_date_timestamp')
	accepted_date_date = tag_value(settings.namespace + '/article/accepted_date_date')
	accepted_date_day = tag_value(settings.namespace + '/article/accepted_date_day')
	accepted_date_month = tag_value(settings.namespace + '/article/accepted_date_month')
	accepted_date_year = tag_value(settings.namespace + '/article/accepted_date_year')
	accepted_date_timestamp = tag_value(settings.namespace + '/article/accepted_date_timestamp')
	award_group_funding_source = tag_value(settings.namespace + '/article/award_group_funding_source')
	award_group_award_id = tag_value(settings.namespace + '/article/award_group_award_id')
	award_group_principle_award_recipient = tag_value(settings.namespace + '/article/award_group_principle_award_recipient')
	funding_statement = tag_value(settings.namespace + '/article/funding_statement')
	copyright_statement = tag_value(settings.namespace + '/article/copyright_statement')
	copyright_year = tag_value(settings.namespace + '/article/copyright_year')
	copyright_holder = tag_value(settings.namespace + '/article/copyright_holder')
	license = tag_value(settings.namespace + '/article/license')
	license_type = tag_value(settings.namespace + '/article/license_type')
	license_url = tag_value(settings.namespace + '/article/license_url')
	ack = tag_value(settings.namespace + '/article/ack')
	conflict = tag_value(settings.namespace + '/article/conflict')
	authors = tag_value(settings.namespace + '/article/authors')
	refs = tag_value(settings.namespace + '/article/refs')
	components = tag_value(settings.namespace + '/article/components')

class fi_ref(Object):
	about = readonly_tag_value(u'fluiddb/about')
	ref = tag_value(settings.namespace + '/ref/ref')
	article_doi = tag_value(settings.namespace + '/ref/article_doi')
	article_title = tag_value(settings.namespace + '/ref/article_title')
	publication_type = tag_value(settings.namespace + '/ref/publication_type')
	doi = tag_value(settings.namespace + '/ref/doi')
	doi_url = tag_value(settings.namespace + '/ref/doi_url')
	pmid = tag_value(settings.namespace + '/ref/pmid')
	authors = tag_value(settings.namespace + '/ref/authors')
	year = tag_value(settings.namespace + '/ref/year')
	source = tag_value(settings.namespace + '/ref/source')
	volume = tag_value(settings.namespace + '/ref/volume')
	fpage = tag_value(settings.namespace + '/ref/fpage')
	lpage = tag_value(settings.namespace + '/ref/lpage')
	collab = tag_value(settings.namespace + '/ref/collab')
	publisher_loc = tag_value(settings.namespace + '/ref/publisher_loc')
	publisher_name = tag_value(settings.namespace + '/ref/publisher_name')
	position = tag_value(settings.namespace + '/ref/position')
	etal = tag_value(settings.namespace + '/ref/etal')

class fi_component(Object):
	about = readonly_tag_value(u'fluiddb/about')
	doi = tag_value(settings.namespace + '/component/doi')
	doi_url = tag_value(settings.namespace + '/component/doi_url')
	type = tag_value(settings.namespace + '/component/type')
	content = tag_value(settings.namespace + '/component/content')
	article_doi = tag_value(settings.namespace + '/component/article_doi')
	position = tag_value(settings.namespace + '/component/position')
	
class fi_author(Object):
	about = readonly_tag_value(u'fluiddb/about')
	author = tag_value(settings.namespace + '/author/author')
	person_id = tag_value(settings.namespace + '/author/person_id')
	equal_contrib = tag_value(settings.namespace + '/author/equal_contrib')
	article_doi = tag_value(settings.namespace + '/author/article_doi')
	surname = tag_value(settings.namespace + '/author/surname')
	given_names = tag_value(settings.namespace + '/author/given_names')
	department = tag_value(settings.namespace + '/author/department')
	institution = tag_value(settings.namespace + '/author/institution')
	city = tag_value(settings.namespace + '/author/city')
	country = tag_value(settings.namespace + '/author/country')
	corresponding = tag_value(settings.namespace + '/author/corresponding')
	position = tag_value(settings.namespace + '/author/position')
	notes_correspondence = tag_value(settings.namespace + '/author/notes_correspondence')
	notes_footnotes = tag_value(settings.namespace + '/author/notes_footnotes')
	notes_other = tag_value(settings.namespace + '/author/notes_other')

class fi_alm(Object):
	about = readonly_tag_value(u'fluiddb/about')
	doi = tag_value(settings.namespace + '/alm/doi')
	alm_source = tag_value(settings.namespace + '/alm/alm_source')
	type = tag_value(settings.namespace + '/alm/type')
	value = tag_value(settings.namespace + '/alm/value')
	timespan = tag_value(settings.namespace + '/alm/timespan')
	date_date = tag_value(settings.namespace + '/alm/date_date')
	date_day = tag_value(settings.namespace + '/alm/date_day')
	date_month = tag_value(settings.namespace + '/alm/date_month')
	date_year = tag_value(settings.namespace + '/alm/date_year')
	date_timestamp = tag_value(settings.namespace + '/alm/date_timestamp')
	complete = tag_value(settings.namespace + '/alm/complete')

class fi_alm_source(Object):
	about = readonly_tag_value(u'fluiddb/about')
	source = tag_value(settings.namespace + '/alm_source/source')
	url = tag_value(settings.namespace + '/alm_source/url')
	name = tag_value(settings.namespace + '/alm_source/name')
	trusted = tag_value(settings.namespace + '/alm_source/trusted')

def bind_fluidinfo_session():
	session.login(settings.username, settings.password)
	session.bind()

def get_uid_and_initial(key, value):
	"""
	Covert content returned from fom values get query
	to uid and initial values to populate a fom object
	Used by bulk load of values for a single object
	or bulk load of many objects, for example find all references
	of an article in one HTTP get, and build them without doing additional
	HTTP
	"""
	uid = None
	about = None
	initial = {}

	uid = key
	for k, v in value.items():
		if(k == 'fluiddb/about'):
			about = v['value']
		initial[k] = {"value": v['value']}
	return about, uid, initial

def get_uid_from_query(query, obj = None):
	"""
	Refactored method to get the fluidinfo id (uid) and
	existing initial values for an object based on a query
	and optionally constrain the tag list returned based on
	a fom object properties
	"""
	uid = None
	about = None
	initial = {}
	# If a fom Object was supplied, get the tag list from its _path_map
	#  otherwise, use the tag wildcard
	if(obj != None):
		tag_list = []
		for k, v in obj._path_map.items():
			tag_list.append(k)
	else:
		tag_list = ["*"]
	objects = values_get(query, tag_list)
	if(objects.content):
		# Parse content returned, only handling one object at once
		# at the moment
		# Parse content returned with json library to convert null values, etc.
		i = json.loads(objects.content)
		if(type(i) == dict):
			# Only handle one object at a time
			for key, value in i["results"]['id'].items():
				(about, uid, initial) = get_uid_and_initial(key, value)
		
	return about, uid, initial

def values_get(query, tag_list):
	"""
	Pass-through values get function, to allow external libraries
	to use fom without directly importing
	"""
	if not hasattr(Fluid, 'bound'):
		bind_fluidinfo_session()
	return Fluid.bound.values.get(query, tag_list)

def get_article_initial(doi_url, obj = None):
	"""
	Bulk load initial values from an existing article object
	Return the fluiddb/id (uid) object value, and
	tag values (in initial) to populate a fom Object
	"""
	uid = None
	initial = {}
	query = 'fluiddb/about = "' + doi_url + '"'
	return get_uid_from_query(query, obj)

def get_ref_initial(article_doi, position, obj = None):
	"""
	Bulk load initial values from an existing ref object
	Uniquely keyed by the article_doi and the position of the ref in that article
	Return the fluiddb/id (uid) object value, and
	tag values (in initial) to populate a fom Object
	"""
	uid = None
	initial = {}
	query = 'fluiddb/about = "' + 'ref' + '_' + str(position) + '_' + article_doi + '"'
	return get_uid_from_query(query, obj)
	
def get_component_initial(article_doi, doi, obj = None):
	"""
	Bulk load initial values from an existing component object
	Uniquely keyed by the article_doi and the doi of the component itself
	Return the fluiddb/id (uid) object value, and
	tag values (in initial) to populate a fom Object
	"""
	uid = None
	initial = {}
	query = 'fluiddb/about = "' + doi + '"'
	return get_uid_from_query(query, obj)

def get_author_initial(article_doi, position, obj = None):
	"""
	Bulk load initial values from an existing author object
	Uniquely keyed by the article_doi and the position of the author in the article
	Return the fluiddb/id (uid) object value, and
	tag values (in initial) to populate a fom Object
	"""
	uid = None
	initial = {}
	query = 'fluiddb/about = "' + 'author' + '_' + str(position) + '_' + article_doi + '"'
	return get_uid_from_query(query, obj)

def main():
	# Basic testing / debug during development
	# moved to load_article.py
	pass

if __name__ == "__main__":
	main()