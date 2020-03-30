import os
import json
from argparse import ArgumentParser
from gtts import gTTS


LANG = {
    "de": {
        "folder_name": "Sprachdateien",
        "time_without_minutes": "Es ist {} Uhr.",
        "time_with_minutes": "Es ist {} Uhr {}."
    },
    "en": {
        "folder_name": "language_files",
        "time_without_minutes": "It's {}.",
        "time_with_minutes": "It's {}:{}."
    }
}



def create_language_files(sprache):
    """
    Reads relevant information from the language file and
    uses google text to speech to create the language files.
    """

    minuten = [15, 30, 45]
    foldername = LANG[sprache]["folder_name"]
    folderpath = os.path.join(os.getcwd(), foldername) # folder for the output files
    time_without_minutes = LANG[sprache]["time_without_minutes"]
    time_with_minutes = LANG[sprache]["time_with_minutes"]

    if not os.path.exists(folderpath):
        os.mkdir(folderpath)

    for hour in range(25):
        ansage = time_without_minutes.format(hour)
        tts = gTTS(ansage, lang=sprache)
        filename = str(hour).zfill(2)+"_00.mp3"
        output_file = os.path.join(folderpath, filename)
        tts.save(output_file)

        for minute in minuten:
            ansage = time_with_minutes.format(hour, minute)
            tts = gTTS(ansage, lang=sprache)
            filename = str(hour).zfill(2)+"_"+str(minute)+".mp3"
            output_file = os.path.join(folderpath, filename)
            tts.save(output_file)


def create_script_file(sprache):
    """
    Creates the script which is later called via cron.
    """
    language_folder = LANG[sprache]["folder_name"]

    with open("tell_time.sh", 'w') as file_script:
        file_script.write("#!/bin/sh\n\n")
        file_script.write("hour=$(date +\"%H\")\n")
        file_script.write("minute=$(date +\"%M\")\n\n")
        file_script.write("file=${hour}_${minute}.mp3\n")
        file_script.write(f"language_folder={language_folder}\n")
        file_script.write("ffplay -nodisp -autoexit ${language_folder}/$file")



if __name__ == '__main__':
    PARSER = ArgumentParser()
    PARSER.add_argument("-l", "--language", dest="LANGUAGE", required=True,
                        help="your language, e.g. '-l en' for english")
    ARGS = PARSER.parse_args()

    create_script_file(ARGS.LANGUAGE)
    create_language_files(ARGS.LANGUAGE)
