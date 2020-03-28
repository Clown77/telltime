# telltime
Outputs the time every quarter of an hour by voice output.


ENGLISH VERSION BELOW

## Beschreibung

   Gibt jede Viertelstunde die Uhrzeit, per Sprachausgabe, aus.

## Installationsvorraussetzungen
   
    - python3 (sudo apt-get install python3)
    - gTTS (pip3 install gTTS)

## Installation

    - git clone https://github.com/Clown77/telltime.git
    - python3 install.py -l de

#### Eintrag zu cron hinzufügen
	 
	- die Konfiguration für cronjob öffnen
	  - 'crontab -e'
	- folgende Zeilen hinzufügen
	  - XDG_RUNTIME_DIR=/run/user/1000
   	  - 0,15,30,45 * * * * cd <PATH_TO_FOLDER> && sh tell_time.sh
	- <PATH_TO_FOLDER> durch den Pfad zum Ordner ersetzen, welcher das
	  'tell_time.sh' Skript beinhaltet

	Die erste Zeile macht es möglich die Ausgabe auch dann an das Ausgabegerät
	weiterzuleiten wenn es durch eine andere Anwendung "blockiert" ist.

	Die zweite Zeile ruft das Skript jede Viertelstunde auf.

#### oder nutzt eine andere Möglichkeit das Skript aufzurufen

	 Every other solution to call the script is also possible, all it needs is
	 to call the 'tell_time.sh' script.

	 Es ist jedoch notwendig das Skript exakt jede Viertelstunde aufzurufen,
	 da nur dafür Sprachdateien erstellt wurden.

-------------------------------------

## description
   Outputs the time every quarter of an hour by voice output.

## install requirements
   
    - python3 (sudo apt-get install python3)
    - gTTS (pip3 install gTTS)

## installation

    - git clone https://github.com/Clown77/telltime.git
    - python3 install.py -l en

#### add entry to cron

    - open cronjob configuration with	
   	  - 'crontab -e'
    - Add the following lines
   	  - XDG_RUNTIME_DIR=/run/user/1000
   	  - 0,15,30,45 * * * * cd <PATH_TO_FOLDER> && sh tell_time.sh
	- replace <PATH_TO_FOLDER> with path to folder which includes the
   	  'tell_time.sh' script

    The first line makes it possible to shove the sound to the ouput
    device, even if some other sound (e.g. music) is played.

    The second one calls the script every quarter.

#### or use another solution to call the script

	Other solutions can also be chosen to call the script.
	Only the script 'tell_time.sh' must be called for the output.

	However, it is necessary to call the script exaclty every quarter of an
	hour, because only for these times language files were created.
