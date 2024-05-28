# import requests
# import os
# from django.core.files import File

# OCR_API_TOKEN_HEADER=os.environ.get('OCR_API_TOKEN_HEADER')
# OCR_API_ENDPOINT=os.environ.get('OCR_API_ENDPOINT')

# def extract_text_via_ocr_services(file_obj:File):
#     data = {}
#     if OCR_API_ENDPOINT is None:
#         return data
#     if OCR_API_TOKEN_HEADER is None:
#         return data
#     if file_obj is None:
#         return data
    
#     headers = {
#         "Authorization": f"Bearer {OCR_API_TOKEN_HEADER}"
#     }
    
#     with file_obj.open('rb') as f:
#         r = requests.post(OCR_API_ENDPOINT, files={'filename': file_obj}, headers=headers)
#         if r.status_code in range(200,299):
#             if r.headers.get("Content-Type") == "application/json":
#                 data = r.json()
#     return data