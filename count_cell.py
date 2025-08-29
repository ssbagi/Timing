'''
The Method is like this : In general Synopsys or Any timing report will be like this 
This was helpful for me when I was doing DCD report understanding and stuff.
There is inbuilt commands avialable in Synopsys. 

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

Go line by line parse the reports. 
Starting of the Report will be having Startpoint then start to read the cells after the Endpoint like there will be Cell_path as indicator for starting. 

The Logic is simple Dictonary Creation : 
1. Key will the cell type and Value will be the Count of the cells. 
2. Detect the end of the report and then put the collected cell count in the Excel file. 
3. Then loops the same logic in all the Clock path reports. 

Capture the following metrics from each run 
• Inst Count
• Buf/Inv Count  
• Congestion number post Clock routing  
• Insertion Delay  
• Skew  
• Clock-Cell Count  
• No. of Levels in the clock tree 

'''

# Define the cell libraries for different threshold voltages and types
# Nominal Voltage Threshold (NVT)
nominal_vt_inv = [
    'SAEDRVT14_INV_S_2', 'SAEDRVT14_INV_S_4', 'SAEDRVT14_INV_S_6',
    'SAEDRVT14_INV_S_8', 'SAEDRVT14_INV_S_16', 'SAEDRVT14_INV_S_20',
    'SAEDRVT14_INV_S_40', 'SAEDRVT14_INV_S_60', 'SAEDRVT14_INV_S_80'
]

nominal_vt_buff = [
    'SAEDRVT14_BUFF_S_2', 'SAEDRVT14_BUFF_S_4', 'SAEDRVT14_BUFF_S_6',
    'SAEDRVT14_BUFF_S_8', 'SAEDRVT14_BUFF_S_16', 'SAEDRVT14_BUFF_S_20',
    'SAEDRVT14_BUFF_S_40', 'SAEDRVT14_BUFF_S_60', 'SAEDRVT14_BUFF_S_80'
]

# Low Voltage Threshold (LVT)
low_vt_inv = [
    'SAEDLVT14_INV_S_2', 'SAEDLVT14_INV_S_4', 'SAEDLVT14_INV_S_6',
    'SAEDLVT14_INV_S_8', 'SAEDLVT14_INV_S_16', 'SAEDLVT14_INV_S_20',
    'SAEDLVT14_INV_S_40', 'SAEDLVT14_INV_S_60', 'SAEDLVT14_INV_S_80'
]

low_vt_buff = [
    'SAEDLVT14_BUFF_S_2', 'SAEDLVT14_BUFF_S_4', 'SAEDLVT14_BUFF_S_6',
    'SAEDLVT14_BUFF_S_8', 'SAEDLVT14_BUFF_S_16', 'SAEDLVT14_BUFF_S_20',
    'SAEDLVT14_BUFF_S_40', 'SAEDLVT14_BUFF_S_60', 'SAEDLVT14_BUFF_S_80'
]

# High Voltage Threshold (HVT)
high_vt_inv = [
    'SAEDHVT14_INV_S_2', 'SAEDHVT14_INV_S_4', 'SAEDHVT14_INV_S_6',
    'SAEDHVT14_INV_S_8', 'SAEDHVT14_INV_S_16', 'SAEDHVT14_INV_S_20',
    'SAEDHVT14_INV_S_40', 'SAEDHVT14_INV_S_60', 'SAEDHVT14_INV_S_80'
]

high_vt_buff = [
    'SAEDHVT14_BUFF_S_2', 'SAEDHVT14_BUFF_S_4', 'SAEDHVT14_BUFF_S_6',
    'SAEDHVT14_BUFF_S_8', 'SAEDHVT14_BUFF_S_16', 'SAEDHVT14_BUFF_S_20',
    'SAEDHVT14_BUFF_S_40', 'SAEDHVT14_BUFF_S_60', 'SAEDHVT14_BUFF_S_80'
]

# Compile the regex once for efficiency
startpoint_pattern = re.compile(r'.*Startpoint.*')
endpoint_pattern = re.compile(r'.*Endpoint.*')

'''

'''
# Define the cell libraries for different threshold voltages and types
# Nominal Voltage Threshold (NVT)
nominal_vt_inv = [
    'SAEDRVT14_INV_S_2', 'SAEDRVT14_INV_S_4', 'SAEDRVT14_INV_S_6',
    'SAEDRVT14_INV_S_8', 'SAEDRVT14_INV_S_16', 'SAEDRVT14_INV_S_20',
    'SAEDRVT14_INV_S_40', 'SAEDRVT14_INV_S_60', 'SAEDRVT14_INV_S_80'
]

nominal_vt_buff = [
    'SAEDRVT14_BUFF_S_2', 'SAEDRVT14_BUFF_S_4', 'SAEDRVT14_BUFF_S_6',
    'SAEDRVT14_BUFF_S_8', 'SAEDRVT14_BUFF_S_16', 'SAEDRVT14_BUFF_S_20',
    'SAEDRVT14_BUFF_S_40', 'SAEDRVT14_BUFF_S_60', 'SAEDRVT14_BUFF_S_80'
]

# Low Voltage Threshold (LVT)
low_vt_inv = [
    'SAEDLVT14_INV_S_2', 'SAEDLVT14_INV_S_4', 'SAEDLVT14_INV_S_6',
    'SAEDLVT14_INV_S_8', 'SAEDLVT14_INV_S_16', 'SAEDLVT14_INV_S_20',
    'SAEDLVT14_INV_S_40', 'SAEDLVT14_INV_S_60', 'SAEDLVT14_INV_S_80'
]

low_vt_buff = [
    'SAEDLVT14_BUFF_S_2', 'SAEDLVT14_BUFF_S_4', 'SAEDLVT14_BUFF_S_6',
    'SAEDLVT14_BUFF_S_8', 'SAEDLVT14_BUFF_S_16', 'SAEDLVT14_BUFF_S_20',
    'SAEDLVT14_BUFF_S_40', 'SAEDLVT14_BUFF_S_60', 'SAEDLVT14_BUFF_S_80'
]

# High Voltage Threshold (HVT)
high_vt_inv = [
    'SAEDHVT14_INV_S_2', 'SAEDHVT14_INV_S_4', 'SAEDHVT14_INV_S_6',
    'SAEDHVT14_INV_S_8', 'SAEDHVT14_INV_S_16', 'SAEDHVT14_INV_S_20',
    'SAEDHVT14_INV_S_40', 'SAEDHVT14_INV_S_60', 'SAEDHVT14_INV_S_80'
]

high_vt_buff = [
    'SAEDHVT14_BUFF_S_2', 'SAEDHVT14_BUFF_S_4', 'SAEDHVT14_BUFF_S_6',
    'SAEDHVT14_BUFF_S_8', 'SAEDHVT14_BUFF_S_16', 'SAEDHVT14_BUFF_S_20',
    'SAEDHVT14_BUFF_S_40', 'SAEDHVT14_BUFF_S_60', 'SAEDHVT14_BUFF_S_80'
]

# Compile the regex once for efficiency
startpoint_pattern = re.compile(r'.*Startpoint.*')
endpoint_pattern = re.compile(r'.*Endpoint.*')

'''
Key to be strength of the cell and value to be count of the cells.
'''
INV_CELL_COUNT = defaultdict(int)
BUFF_CELL_COUNT = defaultdict(int)

def main():
    parser = argparse.ArgumentParser(description="Process a report and generate a logfile.")
    
    parser.add_argument('--input_report', type=str, required=True,
                        help='Path to the input report file')
    parser.add_argument('--output_logfile', type=str, default='logfile.txt',
                        help='Filename or path for the output logfile (default: logfile.txt in current directory)')

    args = parser.parse_args()

    # Resolve input path
    input_path = os.path.realpath(args.input_report)
    
    # Handle output path: if it's just a filename, place it in current directory
    if os.path.dirname(args.output_logfile):
        output_path = os.path.realpath(args.output_logfile)
    else:
        output_path = os.path.join(os.getcwd(), args.output_logfile)
    
    input_file_extract_content(input_path, output_path)
    
    try:
        with open(input_path, 'r') as infile:
            report_data = infile.read()
            print(f"Loaded report from: {input_path}")
            
    except Exception as e:
        print(f"Error during processing: {e}")

def input_file_extract_content(input_path, output_path):
    try:
        with open(input_path, 'r') as report:
            report_data = report.read()
            print(f"Loaded report from: {input_path}")
            '''
            Startpoint :
            Endpoint   :
            Cell_Name   tr   tf   cap   delay
            Cell_Path(Hierarchical_path)/.*_inv_4_/IN
            Cell_Path(Hierarchical_path)/.*_inv_4_/OUT
            '''
            cell_in = ""
            cell_out = ""
            strength = ""
            for line_number, line in enumerate(report_data, start=1):
                startpoint_match = startpoint_pattern.search(line)
                endpoint_match = endpoint_pattern.search(line)
                # SAEDHVT14_BUFF_S_4
                inv_cell_name_in = re.search(r'G2_Datapath.*/.*/(.*_INV_.*)_(\d+)/(IN)', line)
                inv_cell_name_out = re.search(r'G2_Datapath.*/.*/(.*_INV_.*)_(\d+)/(OUT)', line)
                buff_cell_name_in = re.search(r'G2_Datapath.*/.*/(.*_BUFF_.*)_(\d+)/(IN)', line)
                buff_cell_name_out = re.search(r'G2_Datapath.*/.*/(.*_BUFF_.*)_(\d+)/(OUT)', line)
                if startpoint_match:
                    keyword = startpoint_match.group(1)
                    print(f"{keyword} found on line {line_number}: {line.strip()}")
                if endpoint_match:
                    keyword = endpoint_match.group(1)
                    print(f"{keyword} found on line {line_number}: {line.strip()}")
                
                if inv_cell_name_in:
                    inv_cell_in = inv_cell_name_in.group(1)
                    inv_strength_in = int(inv_cell_name_in.group(2))
                if inv_cell_name_out:
                    inv_cell_out = inv_cell_name_out.group(1)
                    inv_strength_out = int(inv_cell_name_out.group(2))
                    if (inv_cell_in == inv_cell_out) and (inv_strength_in == inv_strength_out):
                        print(f"Matching cell found: {inv_cell_in}")
                        INV_CELL_COUNT[inv_strength_in] += 1

                if buff_cell_name_in:
                    buff_cell_in = buff_cell_name_in.group(1)
                    buff_strength_in = int(buff_cell_name_in.group(2))
                if buff_cell_name_out:
                    buff_cell_out = buff_cell_name_out.group(1)
                    buff_strength_out = int(buff_cell_name_out.group(2))
                    if (buff_cell_in == buff_cell_out) and (buff_strength_in == buff_strength_out):
                        print(f"Matching cell found: {buff_cell_in}")
                        BUFF_CELL_COUNT[buff_strength_in] += 1
        output_report_write(output_path)
    except Exception as e:
        print(f"Error reading file {input_path}: {e}")

def output_report_write(output_path):
    with open(output_path, 'w') as outfile:
        for strength, count in INV_CELL_COUNT.items():
            outfile.write(f"INV Strength {strength}: {count}\n")
        for strength, count in BUFF_CELL_COUNT.items():
            outfile.write(f"BUFF Strength {strength}: {count}\n")

if __name__ == "__main__":
    main()





