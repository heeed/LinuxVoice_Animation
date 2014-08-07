#!/bin/bash
echo "This script will create a video from all of the jpg files"
echo "Please ensure that you have installed mencoder"

ls *.jpg > stills.txt

mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=4/3:vbitrate=8000000 -vf scale=640:480 -o timelapse.avi -mf type=jpeg:fps=6 mf://@stills.txt
