import os
import json
from argparse import ArgumentParser
from gtts import gTTS

def create_language_files(sprache):
    """
    Reads relevant information from the language file and
    uses google text to speech to create the language files.
    """
    language_file = os.path.join("languages", sprache+".json")

    with open(language_file, 'r') as json_file:
        json_object = json.loads(json_file.read())

    minuten = [15, 30, 45]
    foldername = json_object["folder_name"]
    folderpath = os.path.join(os.getcwd(), foldername) # folder for the output files
    time_without_minutes = json_object["time_without_minute"]
    time_with_minutes = json_object["time_with_minute"]

    if not os.path.exists(folderpath):
        os.mkdir(folderpath)

    for hour in range(25):
        ansage = time_without_minutes.format(hour)
        tts = gTTS(ansage, lang=sprache)
        filename = str(hour)+"_00.mp3"
        output_file = os.path.join(folderpath, filename)
        tts.save(output_file)

        for minute in minuten:
            ansage = time_with_minutes.format(hour, minute)
            tts = gTTS(ansage, lang=sprache)
            filename = str(hour)+"_"+str(minute)+".mp3"
            output_file = os.path.join(folderpath, filename)
            tts.save(output_file)


def create_script_file(sprache):
    """
    Creates the script which is later called via cron.
    """
    language_file = os.path.join("languages", sprache+".json")

    with open(language_file, 'r') as json_file:
        json_object = json.loads(json_file.read())

    language_folder = json_object["folder_name"]

    with open("tell_time.sh", 'w') as file_script:
        file_script.write("#!/bin/sh\n\n")
        file_script.write("hour=$(date +\"%H\")\n")
        file_script.write("minute=$(date +\"%M\")\n\n")
        file_script.write("file=${hour}_${minute}.mp3\n")
        file_script.write(f"language_folder={language_folder}\n")
        file_script.write("ffplay -nodisp -autoexit Sprachdateien/$file")



if __name__ == '__main__':
    PARSER = ArgumentParser()
    PARSER.add_argument("-l", "--language", dest="LANGUAGE", required=True,
                        help="your language, e.g. '-l en' for english")
    ARGS = PARSER.parse_args()

    create_script_file(ARGS.LANGUAGE)
    #create_language_files(ARGS.LANGUAGE)
