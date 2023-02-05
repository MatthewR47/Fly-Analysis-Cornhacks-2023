# Fly-Analysis-Cornhacks-2023

This is a data analytics tool intended for use with genetics research dealing with fruit flies. 
The overall summary of the tool: 
It reads in from a file of actvity data that is being read from monitors tracking fly movement. Any time that a registered file is changed, it updates the 
prediction of which flies will perform the best in heat intense conditions based on their movement until that point. This prediction is made based on
precalculated weights from a regression model. As the flies move, up and until 20 minutes of activity monitoring, the prediction becomes more accurate. This 
live monitoring allows for flies to be removed early on and therefore be put aside for breeding before the heat overwelms them. Also included in this project,
is a simulation of an activity monitor to test for accurate readings.

NOTE: this repo has limited version history as it was created just before submission as a public repo. The original repo we used throuhgout the project
contained data that researches who asked us to create this tool asked us not to share. We have permission to share the data in this venue, but not publicly.
If we need to add a member to the private repo for version history view, we can.

Below is the Program request we recieved:

Significance and Scientific Premise

The study of heat tolerance in fruit flies has been of particular interest to researchers for at least the past few decades. The extent of the ability of 
Drosophila to adapt better heat tolerance as a result of selection regimes, how different selection regimes produce different phenotypes, as well as how the 
molecular mechanisms behind such thermal regulation function have been the subjects of some of the most common lines of inquiry (Gong and Golic 2006; 
Hangartner and Hoffmann 2016; Hoffmann et al. 1997; Ko et al. 2019; Sorensen et al. 2013). These types of experiments can garner valuable information regarding 
the evolutionary capacity of fruit flies and other organisms, as well as elucidate the molecular basis for such adaptive change. Further, the ability of 
organisms to adapt to rising temperatures is becoming increasingly relevant in era of dramatic climate change (Kellerman et al. 2012). As such, it is 
especially important to consider the ability of Drosophila to adapt to rising temperatures in the near future (Hangartner and Hoffmann 2016). Therefore, 
continued research in the realm of heat tolerance, including new and innovative approaches to this decades-old field will continue to be valuable. 
In general, heat tolerance has been assessed manually. Briefly, researchers house individual flies in 3.5mL tubes and attach them to a board of sorts that is 
then dropped into a heated water bath. The researches then monitor the flies for physiological collapse (i.e., heat stroke) and note the time. Obviously, this 
method is inherently subjective and can be quite difficult to efficiently perform these assays in the lab. Regardless, this has been the standard for heat 
tolerance research for at least three decades. 
Recently Maclean et al. (2022) described an automated method to measure heat tolerance using a camera-based system and motion-tracking software. However, there 
are issues inherent to this type of analysis, such as a relatively high level of background noise in terms of movement data. This group also described a 
previously uninvestigated aspect of heat tolerance. Namely, Maclean and colleagues found group specific differences in activity level, prompting them to 
suggest a potential implication for analyzing activity data more intently:
The plots of average activity profiles (Figures S10-13) showed treatment specific patterns, indicating that the maximal movement or temperature of maximal 
movement could reveal biological relevant information about the effect of acclimation, ramping rate or species differences. This needs to be explored further 
in dedicated studies, but might mean that individual thermal tolerance can be estimated before physiological collapse is reached. This might have important 
implications for studies applying selection or estimating heritability (e.g. Hangartner and Hoffmann, 2016).
In our data we also saw group-specific differences in activity, prompting us to wonder whether we would have enough variation in activity level during the 
first part of the assay to predict the time to knockdown by only looking at activity level in the first 10 to 20 minutes (note that flies will generally reach 
physiological collapse at 40 to 60 minutes at 37°C). We employed a logistic regression in SPSS (statistical package for the social sciences—which is actually 
built in python) and found that we did indeed have significant predictors. For our dataset we found that minutes 0, 6, 7, 9, 12, and 20 significantly predicted 
time to physiological collapse. We then used the slopes and intercept from this equation on a new dataset of flies to test how valid our predictions were:
	Bottom 75%	Top 25%	
Bottom 75%	155	29	0.842391
Top 25%	26	32	0.551724
	0.856354	0.52459	0.772727
 
In a nutshell:
•	85.63% of the flies predicted to fall in the Bottom 75% actually did fall in that category.
•	52.46% of the flies predicted to fall in the Top 25% actually did fall in that category.
•	As an informal follow-up, I also confirmed that 50/61 (81.97%) flies predicted to fall in the Top 25% did fall in the Top 50%.
•	
This has incredible biological significance. We can essentially predict with fairly high confidence the group of flies that will fall in the top 25% 
(and importantly, 81% of these flies fell above the median). We could use this group of flies to breed the next generation, and so on, allowing to potentially 
push the population towards higher heat tolerance, without ever technically testing the phenotype. We also minimize effects of heat on fitness and fecundity 
(basically fertility) as we only need to expose flies to 20 minutes of heat as opposed to 40-60 minutes without the ability to predict time to knockdown.

From a basic science perspective this is incredibly intriguing, but there are practical implications. One such example is the problem of adaption to increasing 
temperatures that pollinators face. As another example, Hangartner et al. (2017) found that exposure to 37°C for 75 minutes on days 3, 5, and 7 post-eclosion 
led to reduced predation by juvenile jumping spiders on day 7 in Drosophila melanogaster. The authors reason that the heat exposure could lead to reduced 
metabolic rate and activity (as a coping mechanism during stressor). Less active insects might translate to reduced predator-prey encounter rate, as well as 
increased time spend hiding. The authors cite Dinh et al. (2016), who found exposure to a heat wave decreases electron transport chain activity, and by 
extension, metabolic rate as evidence supporting their explanation. By examining activity level during heat stress, we can essentially offer a mechanism for 
the results seen by Hangartner et al., as we have found prior exposure to heat stress to reduce activity level at future time points. This project essentially 
takes thee focus from the moment of physiological collapse during heat shock and examines it as a process.

Program Description and Function

What our research team would like is a program to apply our logistic regression function in real time, so that we can have the activity monitoring system 
running, and we could know which flies to remove to breed the next generation. This is under the assumption that the researchers using this program would 
already have an existing regression function based on their population. This is because there is enough variation between lab populations that each lab using
this would need to calculate their own logistic regression based on control activity in their population at elevated temperatures. 


Text files (data file)

Attached to this email is are example text files. These are the text files that the acquisition software that we use automatically writes to. It writes to 
these every 15 seconds in our case, because that it what I have set the index to in the software. The construction of the files is as follows: Column 3 is 
the timestamp; Columns 11-42 then correspond to individual flies. So for example, if we look at column 11 and read down, each row gives the number of 
movements for that fly during each index (timestamp in column 3). These would be the files that will be updating every 15 seconds while the program is 
running. 

Excel files (data processing)

The (“Validation_Sample”) excel file is the process we used to predict. Note that the first sheet is the data transposed. The first two rows are elapsed time 
in minutes and seconds, respectively. The subsequent rows are individual flies. The data far to the right on this sheet was simply a way we used to get the
last time of movement, but undoubtedly Matthew’s method in the existing program is more efficient. The next sheet are the Log Rank Weight (essentially the 
slopes and intercepts for the equation). The first grouping is when we are trying to predict which flies fall in top 25% and the second set is when we predict 
which flies fall in the top 10%. Note when I say, top 25 or 10%, I am meaning that the last 25 or 10% to reach physiological collapse. At the beginning I 
would just focus on the top 25%, unless there is time to do both. 

The next two sheets are calculating the predictions for the top 15 and 10%, respectively. Both follow the same format, and the labels are fairly 
self-explanatory. Briefly, “LastMove” is the time of physiological collapse. Really the only two that we need for this program are the two columns in 
green. The “predicted” value is the answer to the regression equation, which can be followed by examined the excel sheet. Then, if the value is larger 
than 0.019 (from the logistic regression), the fly is predicted to fall in the top 25% (1), and if less than, it is predicted to fall in bottom 75% (0). 

What we essentially want is for the program your team is building to take the text files with the original data and apply the regression equation are
read out to us which flies are predicted to fall in top 25% so we know which ones to pull out. If it could work in real time as the text files are updated, 
that would be really cool!

Extras – If need more complexity for competition

If there ends up being more time:
 
The (“Modeling_Sample”) excel file is the process we used to plug the data into the logistic regression. The first sheet is the original data with the 
timestamp changed to elapsed time in minutes. Notice that in this sheet though we have combined many monitor datasets into one. Columns here still represent 
individual flies and their movements. The next sheet is the transposed data into a format usable by SPSS. Way to the right is just a way to get last time of
movement, but that would probably be easier and more efficient with Matthew’s pre-existing program. Finally, the third sheet is the summed activity in 
1-minute increments up to 20 minutes, along with the last movement (i.e., time to knockdown) in seconds for each fly. These were put into the logistic 
regression analysis. I did check and python does have a StatsModels package, so if there would be a way to have the program take activity data from those 
original text files, put them together into a large dataset and run the logistic regression to generate the equation for the top 25% or top 10% that would 
be hugely beneficial. As I mentioned above, this equation has been validated for our population, but will likely need to be recalculated for other labs based
on their fly populations. To check the validity of the model, that is where those other columns in the (“Validation_Sample”) excel file on sheets three and 
four come into play. Those are essentially seeing whether the flies predicted to fall in the top 25 or 10% actually did fall there. 

For this functionality, it would not run in real time, as the dataset would need to include the knockdown times in order for the logistic regression 
analysis to be run.
