from flask import Flask, request, abort
import boto3, botocore


app = Flask(__name__)



s3 = boto3.client(
   "s3",
   aws_access_key_id=app.config['S3_KEY'],
   aws_secret_access_key=app.config['S3_SECRET']
)

def send_to_storage(file, bucket_name, acl="public-read"):
    """
    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    """
    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type    #Set appropriate content type as per the file
            }
        )
    except Exception as e:
        print("Something Happened: ", e)
        return e
    return "{}{}".format(app.config["S3_LOCATION"], file.filename)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/upload", methods=["POST"])
def upload_file():
    if request.method == "POST":
        if "user_file" not in request.files:
            return abort(400)
        
        file = request.files["user_file"]

        if file.filename == "":
            return abort(400)

        if file:
            file.filename = secure_filename(file.filename)
            output = send_to_storage(file) 

        else: 
            return redirect("/")
    else:
        return abort(405)