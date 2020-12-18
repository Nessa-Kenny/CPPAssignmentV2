import os

from flask import Flask, render_template, request, redirect, send_file, url_for
from s3_files import list_files, download_file, upload_file

upload_file(f"copy", "nkrecipe1234")
redirect("/index")

        