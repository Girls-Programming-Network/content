# Content

This repo contains projects as designed by the Girls' Programming Network team to enaable further inclusion in technology. Projects explore concepts in technologies such as Python, MicroBit, Pygame Zero, and others. You'll find concepts covered such as cyber security and cryptography, AI, game design, and electronics.

Each projects comes equiped with content (designed with high school students in mind, but suitable for any learner), including including final code, workbooks, tutor answers, cheat sheeets, and additional assets. 

*We are still in the process of transitioning our content to this new repo, some pieces may not have migrated for each project yet.*

## Updating existing content
There are a couple steps you will need to follow in order to correctly update files from within this repo (majority of these steps are also suggested for when adding new files too as they are good overall habits).

There are a couple reasons you need to follow this process. One is so that you can update the repository without creating conflicts and allowing for suggestions on the changes to be made, and saving the new version of the file to the same name as the old file ensures all links that were referencing the old version now reference the new correct version. Both of these are really important.

Firstly you'll need to fork and then clone this repo. This is so that you can make changes locally on your device as you won't be able to directly edit the main content. In order to fork this repo you will need to go to the __CODE__ tab and press the button that says __fork__. This will essentially make a copy of the repo that you own and are allowed to make changes to without directly affecting the main repo. The next step you'll need to do is to __Clone__ your fork. 

This part is slightly more difficult and will need to either use the desktop version of Github or your machines Terminal/Command Promt variant. (These steps will generalise but there will be information on the internet for any bits you get stuck on). To clone your fork go to the code tab of your forked version of the repository and press the green code button to get the drop down. You'll want to be in the local section as to update the files you'll need a local clone. Using your prefered method (e.g. copying the clone https link into the add repository section of Github Desktop) add this clone as a local repository (this may take some time to load/download as this repo is quite large).

Once you have a clone of the repo you can start working on the changes you want to make. The first step is to make a new branch in your clone (You can do this in your terminal or github desktop and it can be called anything). __*This step is really important especially for non pdf files (i.e. python files or markdown files) as it will allow others to edit the changes you've made before they are accepted into the main repo*__. Then in order to update sepcific files, you will need to replace them locally. You can do this by deleting the old version of the file, saving the new version of the file to the same place as the old one and calling it the same thing as the old one. 

Once you have made all of the changes you want to make you will need to make sure your branch has been published (this will sync it up with your cloud based fork so it can be connected to the main repo), then you will need to "Commit" your changes to the branch (this will require a summary of the changes you've made so that others can see what you've done). Once you've done this you'll need to go to the main repo (not your fork) and open the section called __pull requests__ and click the button that says "New Pull Request". There should be a blue link above it that says "compare across forks" you will need to select this so that you can create a pull request based off the branch in your fork. Then the first section of the pull request should say something like "base repository: GPN/content" "base: main" -> ... you will need to select the second part that says "head repository:...." and click on your fork. You will also need to click the part that says "head:..." and selec the branch you were just using. You will now be able to select the button that says "Create pull request". You will then need to add a summary of the pull request and someone will need to review it in order for it to be added to the main repo.

## Licences
Girls' Programming Network licences it's material so that you can use it, share it, remix it, but not sell.
Our content is licenced under the [CC BY-NC-SA License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
