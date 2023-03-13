# kooora-top-matches
 
**At first, I wasted much time opening kooora.com site to see matches scores, repeating this in an excessive way, 
so I needed to build notification system that notifies me with all important and top matches scores today, without need to open the site and procrastinate by indulging in news section.**

The Top match box appears to be like this:

<img src="https://user-images.githubusercontent.com/69548206/224582881-942d1e02-b8e2-49cf-ac1a-ec9c5cd16a7c.png" height="500">

1) Open your command prompt (Windows) or terminal (Mac or Linux).
2) Type the following command to check if pip is installed:
`pip --version`
3) If pip is installed, you will see its version number. If not, you can install it by typing:\
`python3 -m ensurepip --default-pip`
4) Once you have pip installed, type the following command and press Enter to install bs4:\
`pip install beautifulsoup4`

**Then after cloning the repository from Github, follow these steps:**
1) Open your command prompt (Windows) or terminal (Mac or Linux).
2) Use the `cd` command to navigate to the directory where you have cloned the repository.
3) Once you are in the directory, you can run the Python file by typing the following command:\
`python kooora.py`

**I made some modifications for more visualization (you can change it as you desire, of course):**
1) If match isn't played yet, it is preceded by 🔘.
2) If match is played right now ( live time ), it is preceded by 🔴.
3) If match is finished, so it becomes 🟢, and obviously the score is the final one. 

For me, I wanted the python output to be parsed in `notify-send` notification when I press on specific i3block, so I modified the
i3blocks config to add this:
```
[separator]
[kooora]
command=echo " ⚽ "; i3-msg exec python3 /home/yassa/.scripts/statusbar/kooora.py
interval=once
```
Of course, You can make it appears to you in time periods you determine,
change `once` in `interval=once` to number of seconds you want the script to refresh and appears to you 

So when I press on that soccer emoji, displays the notification.

<img src="https://user-images.githubusercontent.com/69548206/224584524-0dcb57d6-6b47-4a2c-b9f9-207fbb26d8fa.png" height="200">



