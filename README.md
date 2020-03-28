# telltime
Outputs the time every quarter of an hour by voice output.


## install requirements

   - python3 (sudo apt-get install python3)
   - gTTS (pip3 install gTTS)

## installation

   - git clone https://github.com/Clown77/telltime.git
   - python3 install.py

### add entry to cron

   - open cronjob configuration with	
   	 - 'crontab -e'
   - Add the following lines
   	 - XDG_RUNTIME_DIR=/run/user/1000
   	 - 0,15,30,45 * * * * cd <PATH_TO_FOLDER> && sh tell_time.sh

   The first line makes it possible to shove the sound to the ouput
   device, even if some other sound (e.g. music) is played.

   The second one calls the script every quarter.
