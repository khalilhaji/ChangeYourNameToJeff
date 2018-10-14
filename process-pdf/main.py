from google.cloud import storage
storage_client = storage.Client()
bucket_url = 'http://storage.googleapis.com/cyn-outputs/'

import os
import pdfrw
import re
import uuid

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

KEY_MATCH = re.compile('(.*)_\d+')

# Populate fields in template PDF form
def populate_fields(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    for page in template_pdf.pages:
        annotations = page[ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    key_main = KEY_MATCH.search(key).group(1) if KEY_MATCH.search(key) else key
                    print(key_main)
                    if key_main in data_dict.keys():
                        annotation.update(
                            pdfrw.PdfDict(V='{}'.format(data_dict[key_main]))
                        )
            pdfrw.PdfWriter().write(output_pdf_path, template_pdf)

# Handle incoming requests and returns filled form
def process_pdfs(request):
    content_type = request.headers['content-type']
    if content_type == 'application/json':
        data = request.json
        template = data['template']
        form_values = data['form_values']

        storage_client.get_bucket('cyn-templates').blob(template).download_to_filename('/tmp/input.pdf')
        populate_fields('/tmp/input.pdf', '/tmp/output.pdf', form_values)
        output_name = str(uuid.uuid4())+'.pdf'
        storage_client.get_bucket('cyn-outputs').blob(output_name).upload_from_filename('/tmp/output.pdf')
        return bucket_url+output_name
