from utils.read_fs import read_local
from utils.read_s3 import read_cloud
from dotenv import load_dotenv
from utils.ai_img_report import ai_analyse
import os

load_dotenv() # load the .env variables
list_report = []
img_src=os.getenv("IMG_SRC")
if img_src == "LOCAL":
    list_img = read_local()
    for img in list_img:
        desc = ai_analyse(img)
        list_report.append(desc)
    print('report final: ', list_report)
    
elif img_src == "S3":
    read_cloud()