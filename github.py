# -*- coding: utf-8 -*-
from apiclient.discovery import build
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()
pro = "positive-notch-114016"

bigquery_service = build('bigquery', 'v2', credentials=credentials)
query_req = bigquery_service.jobs()


def git_hub_get_repositories(language):
    """ Get git hub repositories according to specified language and the following filters:
        1. repository_size
	2. repository_watchers
	3. public
        4. repository_has_downloads
        5. number of forks?
    """
    query = 'SELECT repository_url'
     run_query(query)


def run_query(query):
    query_data = {
    'query': (
	#'SELECT repository_language FROM [githubarchive:year.2014] LIMIT 1000;'
	query
        )
    }

    q = query_req.query(projectId=pro, body=query_data)
    query_resp = q.execute()

    print('Query Results:')
    for row in query_resp['rows']:
        if all(f['v'] for f in row['f']):
    	    print('\t'.join(field['v'] for field in row['f']))

    return query_resp

