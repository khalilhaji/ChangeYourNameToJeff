from google.cloud import storage

storage_client = storage.Client()



def process_pdfs(request):
    storage_client.get_bucket('cyn-templates').blob('california.pdf').download_to_filename('/tmp/test.pdf')
    storage_client.get_bucket('cyn-outputs').blob('test.pdf').upload_from_filename('/tmp/test.pdf')
    return 'PDF ready to download!'
