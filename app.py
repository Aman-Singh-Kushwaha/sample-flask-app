from flask import Flask, request, render_template
# from google.cloud import storage

app = Flask(__name__)
# storage_client = storage.Client()

@app.route('/')
def index():
    return 'Alright It worked'

# @app.route('/upload', methods=['POST'])
# def upload():
#     uploaded_files = request.files.getlist('file')
#     bucket_name = 'your-gcs-bucket-name'

#     for file in uploaded_files:
#         blob = storage_client.bucket(bucket_name).blob(file.filename)
#         blob.upload_from_file(file.stream)

#     return 'File(s) uploaded successfully to GCS'



if __name__ == "__main__":
    app.run(debug=True)
