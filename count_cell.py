'''
The Method is like this : In general Synopsys or Any timing report will be like this 

Startpoint :
Endpoint   : 

Cell Name tr tf cap delay

The script anlaogy is simple :

STEP1 : The cellname will be generally like this 

Cell_Path(Hierarchical_path)/.*_inv_4_/IN
Cell_Path(Hierarchical_path)/.*_inv_4_/OUT

Cell_Path(Hierarchical_path)/.*_inv_8_/IN
Cell_Path(Hierarchical_path)/.*_inv_8_/OUT

Cell_Path(Hierarchical_path)/.*_buff_4_/IN
Cell_Path(Hierarchical_path)/.*_buff_4_/OUT

Cell_Path(Hierarchical_path)/.*_buff_8_/IN
Cell_Path(Hierarchical_path)/.*_buff_8_/OUT

So above we can see the logic or pattern is simple like The names are differing from line to line but if consecutive match and only change in the pin names count the numbers. In Excel we can segerate it as :

PATH_DETAILS  INV INV2  INV4  INV8  INV16  BUFF BUFF2  BUFF4  BUFF8  BUFF16
PATH1         5    2    -     -     2      -    2      4      1      2  
PATH2         5    2    -     -     2      -    2      4      1      2 
PATH3         5    2    -     -     2      -    2      4      1      2 

In way if we want to make it like reduce power then cahnge the type of the cell to HVT type. 

HVT  :  High Threshold Voltage Cell    |   Less leakage.    |  High delay.
NVT  :  Normal Threshold Voltage Cell  |   Normal.        |  Normal delay.
LVT  :  Low Threshold Voltage Cell     |   More leakage.  |  Less delay.

So, in way on top level we come to know the exact scenarios where which path we can optimize you know instead of openeing all the 1000's of report tweaking the stuff like that. 
We can go in specific path or report and do the changes like provoide the feedback and stuff. 
This is just a Heuristic Algorithm.

'''
