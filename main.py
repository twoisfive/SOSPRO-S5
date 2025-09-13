from flask import Flask, render_template, send_from_directory, request, send_file
import os
import requests

app = Flask(__name__)

styles_folder = "templates/styles"
styles_files = sorted(f for f in os.listdir(styles_folder) if f.endswith(".css"))

scripts_folder = "templates/scripts"
scripts_files = sorted(f for f in os.listdir(scripts_folder) if f.endswith(".js"))

@app.route("/")
def home():
    main_section_folder = "templates/sections/main_sections"
    main_section_files = sorted(f for f in os.listdir(main_section_folder) if f.endswith(".html"))
    return render_template("main.html", main_section_files=main_section_files, styles_files=styles_files, scripts_files=scripts_files)

@app.route("/about-us")
def about_us():
    section_folder = "templates/sections/about_us_sections"
    section_files = sorted(f for f in os.listdir(section_folder) if f.endswith(".html"))
    return render_template("about_us.html", about_us_section_files=section_files, styles_files=styles_files, scripts_files=scripts_files)

@app.route("/event")
def event():
    section_folder = "templates/sections/event_sections"
    section_files = sorted(f for f in os.listdir(section_folder) if f.endswith(".html"))
    return render_template("event.html", event_section_files=section_files, styles_files=styles_files, scripts_files=scripts_files)

@app.route("/pacil")
def pacil():
    section_folder = "templates/sections/pacil_sections"
    section_files = sorted(f for f in os.listdir(section_folder) if f.endswith(".html"))
    return render_template("pacil.html", pacil_section_files=section_files, styles_files=styles_files, scripts_files=scripts_files)


BASE_DIR = os.path.dirname(__file__)

@app.route("/video/<path:filename>")
def serve_files(filename):
    return send_from_directory(os.path.join(BASE_DIR, "video"), filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7004)