# Practical Python: Data Wrangling and Data Quality

This repo contains draft coding exercises for the early-release version of the book _Practical Python: Data Wrangling and Data Quality_ to be published by O'Reilly Media in 2021.

## Before You Begin

Below you will find an overview of this repo's contents, as well as important tips and information on how to use these files. In general, all exercises are accessible as standalone `.py` files, and as Jupyter Notebooks. The notebooks can either be downloaded to your device and run locally, or opened and run in Google Colab (https://colab.research.google.com/). The draft text of Chapter 1 includes basic instructions on how to get started with some of these tools; this text will be updated/completed before final publication.

### Working with data files

Because data sets can often be quite large, the data sets for these exercises are available for download [here](https://drive.google.com/drive/folders/1cU5Tdg_fvrCcwvAAyhMOhpbEcI2fF7sb?usp=sharing). 

#### If you are working locally
Data sets should be downloaded/copied in the same folder as the Python file or notebook, unless otherwise indicated.

#### If you are using Google Colab

There are two ways that you can load data files into Google Colab:

1. Link directly to the copies of the data that I have made available via _my_ Google Drive account.
2. Upload copies of the data files to your own Google Drive account


Each of these options has tradeoffs. If you are short on Google Drive space, using option 2 will save you space on your own account and only require commenting/uncommenting some code in the provided Jupyter notebooks. On the other hand, if my shared copies disappear (always a possibility on the interwebs!), work that relies on option 1 will not be affected. You may also find option 1 more straightforward when substituting your own data sets into the example notebooks.

##### Option 1: Link directly to shared data files

All of the notebooks provided in this repo can be opened and used in Google Colab (whether or not they contain the Colaboratory "bug" at the top). In most cases, you will need to can the notebook first and fully uncomment any cells that start with the line **UNCOMMENT BELOW TO USE WITH GOOGLE COLAB**. For this, I recommend highlighting the entire cell and then using the `Ctrl+/` shortcut, which will toggle comments on all selected lines.


##### Option 2: Using data stored on your own account

You will need to upload the data files into a Google Drive folder **on your own account**. _Each time_ you open the notebook, you will need to "mount" your Google Drive folder in order to make the data available to your notebook:

1. Open your target notebook in Google Colab.
2. Click on the `Files` folder icon on the left-hand side of the window. A new pane will open to the right of this icon, and may show a `Connecting...` message for several seconds. Once the connection has been established, you'll see three icons at the top: `Upload to session storage`, `Refresh` and `Mount Drive`. Click `Mount Drive`.
3. A new cell will appear in your notebook (accompanied, the first time, by a blue comment cell indicating that you need to run that cell to mount your Google Drive files). Be sure to move that cell to the very top of your notebook using the arrows positioned over its top right edge.
4. Hit the `play` button to the left of the cell. You will see a warning message that the notebook was not authored by Google (it was authored by me!). Select `RUN ANYWAY`.
5. Click on the link in the cell. It will ask you to select a Google account - you should choose the one to which you have uploaded the data files. You will then need to grant **Google Drive File Stream** (which _is_ a Google service) access to that Google account by clicking the blue `Allow` button. 
6. Finally, copy the long string from the new tab and paste it into the (much smaller) box in your notebook, below the text that says `Enter your authoriation code:` and, with your cursor still in that text box, hit the `enter` key. After several seconds, the cell should reset (the link and authorization code will disappear) and a new folder icon labeled `drive` should appear in the `Files` pane at left. If you don't, try closing the pane via the `X` at the top right and opening it again by clicking on the folder icon at far left.

At this point, you will be able to browse _all_ of your Google Drive folders via the pane to the left of your notebook. 

##### Adjusting the code

Once you have mounted your Google Drive within Colab, you need to browser to your target file. In my Google Drive, for example, I have a folder called `data_wranglig_exercises` which has data files stored in folders by chapter. 

For the Citi Bike data example in Chapter 2, I will navigate to `data_wrangling_exercises -> chapter_2_data_files`, right-click on the file whose name matches the one in the exercise (in this case `202009CitibikeTripdataExample.csv`) and then select `Copy path`. I will then paste this path into the code where the data file is being loaded. For example, I would modify this code:

```python
source_file = open("202009CitibikeTripdataExample.csv","r")
```
To this:

```python
source_file = open("/content/drive/My Drive/data_wrangling_exercises/chapter_2_data_files/202009CitibikeTripdataExample.csv","r")
```

The code will now point to the copy of the data that I have stored on Google Drive.

This needs to be updated!


