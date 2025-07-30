# Timing
The Report Timing. 

It's just a thought way of thinking. This might have already been done also. 

Google provides the Image datasets, Classifier and Pre-built trained models ready ones. 

So, similarly Synopysys, Cadence, MG and third parties can also provide the data. Even the Foundries give the Standard Cell Transition, delays, caps in Table format. 
The table formats like Interpolation and  Extrapolation concepts are used for predicting or calculating the delays. We did basic calculations in college as part of coursework. 

In general the table is like this :

<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/45a68006-88be-4baf-beb1-4cfe94d649a1" />

<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/21dfe5ca-018d-4bd3-9dbc-95bc246df43a" />

<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/7574f580-3827-4c64-be73-7ee0bdba7484" />

For doing STA analysis we generally use the concept of Multi Mode and Multi Corner (MMMC). In our case we have
- skylane130_fd_sc_hd__typical.lib : skylane130_fd_sc_hd__tt_025C_1v80.
- skylane130_fd_sc_hd__slow.lib : skylane130_fd_sc_hd__ss_100C_1v60
- skylane130_fd_sc_hd__fast.lib : skylane130_fd_sc_hd__ff_n40C_1v95

The dataset creation can be like this :
The way we calculate delay is based on the above table format shown in images. Similiarly we can extrapolate or interploate the same calculation below also. 
- INV - INV   : The distance can be 5units, 10 units, 15units ......... 200 ....... 500units. So, Measure the tr, tf, td, cap, diving strength.
- INV - BUF   : The distance can be 5units, 10 units, 15units ......... 200 ....... 500units. So, Measure the tr, tf, td, cap, diving strength.
- BUF - BUF   : The distance can be 5units, 10 units, 15units ......... 200 ....... 500units. So, Measure the tr, tf, td, cap, diving strength.
- NOT - NOT   : The distance can be 5units, 10 units, 15units ......... 200 ....... 500units. So, Measure the tr, tf, td, cap, diving strength.

- Like this for all combinations of the logic gates. Like different test cases scenarios like how we verify various scenarios.  

- Make a huge list now we have AI. It can generate a random list the same way like how we do in Verification. The Random constraints concepts just this time we will include in constraints list the logic gates and distance in one more list. It has to place these stuff in Synopsys ICC2 tool and run the timing analysis and collect the reports, analyze them. 

Similarly now for Flip-Flops :

- STA book J Bhasker : All the 8 case scenarios which were taught for us in college. Similar tweaking like above generates the test cases and measures the timing delay.
- Next once the timing report is generated, now use script to parse and have pre-conditions set for that path. Like we can say the cap value, tr value, fanout value. If there are violations, create a cell list like how we did in college in TCL script INV list, buffer list, Logic gates list. Keep all the cells in it. When it wants to upsize it based on the index it will upgrade or downsize it will downgrade.
- Step 9 can create a catastrophe like a chain reaction where you try to fix one it might affect others or the optimization is such that it takes longer time to do. Dependency of things. There can be a lot of scenarios also.
- In similar additional test cases and concepts can be linked or added. Like the Clock Domain Crossing, Duty Cycle Distortion and different scenarios also.  
- If we can set limits so it doesn't go into a lot of optimization or longer duration. Ya with few Heuristics this can be done. Yes its possible.  


## Tool : Infinisim 
My Master Thesis was on Duty Cycle Distorition for the Clock paths. The Rail to Rail Failure and Duty Cycle Distortion have explained in my report. As part of the feedback/fixes giving so based on the experiment carried out the following analysis was araised. As part of the simulation we used Infinisim. Link : https://infinisim.com/. The Infinisim also provides Webinars How the tool helps in detecting the R2R and DCD on CLock paths and Even they have Jitter analysis and Aging of the transistors. 

## Video : Clock Analysis at 7nm and below 
Infinisim Link : https://infinisim.com/ 


## Top Level Analysis (LEVEL 0 DEBUG)

Level 0 : Debug Analysis.
- In the Source/Image section we observe similar stuff. The Paths might have few levels as similar cells present in the path like kind of root path. 
- The clk path may be same for many paths like at the end like 10 or 20 levels may change. If we optimize the root path cells then multiple paths are already optimized further.

Based on the Report like : In below we observe the cell name followed by pin :
 
- Count the No. of Inverter or Buffer present in the Clock path : Top Analysis Easy feedback. (It's just Regular Expression script can be written in Python)
  - count inverter cells
  - count buffer cells.
  - Segregate based on the strength of the cells. 

Consider this as one top level of giving feedback on the clock paths. Like In general Replace the long cells of Buffer with few Inverter cells.
If the degradation is more in any path then add a buffer in between the inverter path. Not changing the logic. Retain the logic. 

<img width="940" height="528" alt="image" src="https://github.com/user-attachments/assets/fd996f07-fab5-4969-8870-1b9dd4faa2c3" />

## Script 

### Why ?
The reason for this script is beecuase to give faster feedback to the PD team. So, in most of the times what happens is its same path we are simulating many times. Once the design enters into PD cycle its hardly any changes in RTL to Synthesis then again to PD cycle most of the time this is avoided here and there few corner scenarios are present. So, same set of paths like PLL to Source Clk path to Network Clk path then to CLk pin of all the Flip - Flop. In between there many clock dividers also and then clock domain crossing also. So, due to feedback given to PD team the placemnt of the cells or size of the cell or interaction of the cell may lead to R2R Violation or DCD Violation. Since, we are simulating same path multiple times hence, this script is usefull. Like a pattern or same paths. ANalyze some 1000 of timing reports. If you observe carefully the paths upto some level remain same. Consider this as root path. 

At the point of diveregence, then the paths have distortion and stuff. So, hence this script will be usefull. We can have a basic heuristics like How many Inverter cells or Buffer cells or Clock gating cells (CGC) ?, Whether placed cells are of clk type or non clk type ?, What is the Vt of the cells ?, How many levels of cells are present in the path? these get to know since after analyzing few times or reading through the report we can get to know the flow of the clk in the SoC. So, hence we can have fair analysis based on the clk level that after this many levels we can expect this much distortion and stuff.  

### Feedback given to PD Team 

- Replace the number of Clk Buffers with Clk Inverters if you want to reduce area and not seeing much distortion. 1 Clk buffer = 2 Inverters Replace Even number of Buffers with Odd number of Inverter. Retain the same logic so replace 2 buffers with 1 inverter.
  
- If you observe a large change in the distortion then add Buffer. { INV - BUFFER - INV } This combination what will happen is assume first inverter had Ton = 48% the buffer will maintain the same duty cycle then INV then Ton = 52%. So there is distortion of 2% right so now inorder to bring it back you place the Inverter very close to the previous one. So, now the Ton = 49%. 1% improvement is seen and more over INV to INV the logic got changed then add one more inverter close to it so, now the Duty cycle became 50%.
  
- The Size of the cell also matters, Placement of the cell also matters and the routing of the cell in which Metal layer it is routed. This also matters.
  - In general based on the Technology node we have several Metal layers. The 5nm tech node has 13 Metal layers. In general Few metal layers are fixed for clk paths, few metal layers are fixed for Signal routing and few metal layers are fixed for the Power Signals. So, when we have large delays we tend to give feedback to change the metal layer routing i.e., move it to next metal layer. As the Metal layer increases I mean M4 is routed signal now we move it to M6 so, now transition is faster and the delay is reduced, the time taken to charge or discharge cap is less. As we move the routing to higher metal layers the current flow increases and width of the metal layer is also large. Hence there is improvement in things. 
  - Check the distance between the cells, I mean how much is the routing distance between the cells. Like is it 20um or 40um try to reduce this also. This can also been seen as a pattern for given sceanrio. 
  - We know that T = RC right so each distance like assume 1um wirelength based on the tech node it provides 1ns delay {There is similar calculation like this}. Based on this we can give feedback to PD team for reducing the distance or upscalig the cells.
 

The script is attached in this GitHub. The Method flow is simple :
- STEP1 : Feed one Timing Report.
- STEP2 : In Log File we can see the Number of Inverter Cells, Buffer Cells and with respect to their strength.
- STEP3 : In the Excel File for each path we can see the count written. 

Level 0 Debug : Initial top level analysis. 

The Method is like this : In general Synopsys or Any timing report will be like this.

Source : 
- https://anysilicon.com/clock-tree-synthesis/
- https://vlsiuniverse.blogspot.com/2017/12/what-is-difference-between-normal.html 

Image : 

![clock-tree-overview1_jpg](https://github.com/user-attachments/assets/149e2c10-1a34-4fc0-8f50-a06e39848d16)

![clock-tree-overview8_jpg](https://github.com/user-attachments/assets/b5f3ec48-1208-4e52-93bd-d884e3cdf128)

Takeaway Points :
- In above paths we see the Clock path (PLL to the Clk pin of the FF's there are many levels) we can count the number of Clock Cells and Non Clock Cells present in the clock path.
- Need of Clk cells in the clock path. (Link : https://vlsiuniverse.blogspot.com/2017/12/what-is-difference-between-normal.html)
- We can set a threshold like cell count to be 50 if something crossing we need to reduce or less increase. We can keep +/- 10% count varaition also.
- The above can vary w.r.t to tech node, the Floorplan, Placement changes and stuff. 

Timing Report : Example one Report like this as shown below. 

Startpoint :
Endpoint   : 

Cell Name tr tf cap delay

The script anlaogy is simple :

STEP1 : The cellname will be generally like this 

Non CLK Cell List :

Cell_Path(Hierarchical_path)/.*_inv_4_/IN
Cell_Path(Hierarchical_path)/.*_inv_4_/OUT

Cell_Path(Hierarchical_path)/.*_inv_8_/IN
Cell_Path(Hierarchical_path)/.*_inv_8_/OUT

Cell_Path(Hierarchical_path)/.*_buff_4_/IN
Cell_Path(Hierarchical_path)/.*_buff_4_/OUT

Cell_Path(Hierarchical_path)/.*_buff_8_/IN
Cell_Path(Hierarchical_path)/.*_buff_8_/OUT

CLK Cell List :

Cell_Path(Hierarchical_path)/.*_clk_inv_4_/IN
Cell_Path(Hierarchical_path)/.*_clk_inv_4_/OUT

Cell_Path(Hierarchical_path)/.*_clk_inv_8_/IN
Cell_Path(Hierarchical_path)/.*_clk_inv_8_/OUT

Cell_Path(Hierarchical_path)/.*_clk_buff_4_/IN
Cell_Path(Hierarchical_path)/.*_clk_buff_4_/OUT

Cell_Path(Hierarchical_path)/.*_clk_buff_8_/IN
Cell_Path(Hierarchical_path)/.*_clk_buff_8_/OUT

So above we can see the logic or pattern is simple like The names are differing from line to line but if consecutive match and only change in the pin names count the numbers. In Excel we can segerate it as :

## Path Details

| PATH_DETAILS | INV | INV2 | INV4 | INV8 | INV16  | BUFF | BUFF2  | BUFF4  | BUFF8  | BUFF16 | CLK CELLS | Non CLK CELLS |TOTAL |
|--------------|-----|------|------|------|--------|------|--------|--------|--------|--------|-----------|---------------|------|
| PATH1        | 5   | 2    | -    | -    | 2      | -    | 2      | 4      | 1      | 2      | 13        |      12       |  25  |
| PATH2        | 5   | 2    | -    | -    | 2      | -    | 2      | 4      | 1      | 2      | 12        |      13       |  25  |
| PATH3        | 5   | 2    | -    | -    | 2      | -    | 2      | 4      | 1      | 2      | 10        |      15       |  25  |

Based on the cell name present we can even segregate the cells based on the threshold types also.
In way if we want to make it like reduce power then cahnge the type of the cell to HVT type. 

- HVT  :  High Threshold Voltage Cell    |   Less leakage.    |  High delay.
- NVT  :  Normal Threshold Voltage Cell  |   Normal.          |  Normal delay.
- LVT  :  Low Threshold Voltage Cell     |   More leakage.    |  Less delay.

**Takeaway Point** :
- If the number of LVT are more we can check the no. of cells present in the path and count the LVT type of cells and say it maybe have more leakage power. If we want to reduce low leakage replace few of the cells with HVT cells and vice-versa.
- If the path is having non-clock cells we need to reomve them and make everything to clk cells only. 

# Conclusion 
- A Heuristic Algorithm kind of Level 0 Debug Analysis. 
- In way on top level we come to know the exact scenarios where which path we can optimize the paths. 
- Few Paths might have few levels as similar like kind of root path. If we optimize these cells then multiple paths are already optimized further. We can go in specific path or report and do the changes like provide the feedback and stuff. 






