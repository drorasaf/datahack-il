# -*- coding: utf-8 -*-
import os
import zipfile
import wget
import fnmatch
from apiclient.discovery import build
from oauth2client.client import GoogleCredentials

extensions = {'Java': '.java'}

credentials = GoogleCredentials.get_application_default()
pro = "positive-notch-114016"

bigquery_service = build('bigquery', 'v2', credentials=credentials)
query_req = bigquery_service.jobs()

def rep_exists(url):
    """ verifies that the zipfile of the repo exists  """
    suffix = url.split('/')
    zip_filename = suffix[-1] + '-master.zip'
    if os.path.isfile(zip_filename):
         return True
    return False


def filter_by_extension(dirname, ext):
    """ Get a directory and list all files with a specified extension """
    curr_file_list = []    
    for root, dirs, filenames in os.walk(dirname):
	for filename in fnmatch.filter(filenames, "*" + ext):	
	    curr_file_list.append(os.path.join(root, filename))

    return curr_file_list


def github_get_repositories(language):
    """ Get git hub repositories according to specified language and the following filters:
        1. repository_size < 160K <10M
	2. repository_watchers > 1000
	3. public
        4. repository_has_downloads
        5. number of forks?
        returns list of file list filtered by extension related to their language
    """
    files = []
    get_zip_file_ext = '/archive/master.zip'
    query = 'SELECT repository_url FROM [githubarchive:year.2014] WHERE' \
	    ' repository_size > 160 AND repository_size < 10000 AND repository_watchers > 1000 AND' \
            ' public=True AND repository_has_downloads=True AND repository_language="Java" ORDER BY repository_watchers LIMIT 50;'
    res = run_query(query)

    for row in res['rows']:
        if all(f['v'] for f in row['f']):
	    rep_url = row['f'][0]['v']
	    if not rep_exists(rep_url):
		filename = wget.download(rep_url + get_zip_file_ext)
                try:
                    with zipfile.ZipFile(filename) as zf:
			zf.extractall()
		except zipfile.BadZipfile:
		    continue
	    suffix = rep_url.split('/')
            name = suffix[-1] + '-master'
            files.append(filter_by_extension(name, extensions[language]))

    return files


def run_query(query):
    """ executes arbitrary query in google big query """
    query_data = {
    'query': (
	query
        )
    }

    q = query_req.query(projectId=pro, body=query_data)
    return q.execute()

