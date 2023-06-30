MFTC_files README

Combining.py: .py automation file to combine all the MFTC data sets into one.


Procssing.py: .py automation file to process combined_dataset.csv into test and train .json files, as well as produce the verbalizers.
	      To make the verbalizers yourself, you need to just run the .uniqe code at the end and copy the list of strings
	      output to a .txt file and put it in the fewshot folder.

The -example folders are single runs of their namesake. They hold checkpoints if you want to re-run them. if youd like to,
you need to move them to the fewshot folder and rename the output_dir of the corresponding config file in fewshot<data to 
the name of the output folder in question. Additionally, if you want to do a completely fresh run, just dont move the
example output folder to the fewshot folder. It will create a new one instead.

######################EDIT#####################
In order to manage to get these files onto github, I had to delete the checkpoint folders and models because theyre over 1GB each. I have them saved locally,
so i can try get them to you another method if you'd like them!
