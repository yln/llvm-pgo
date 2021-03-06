import sys
import os

def usage():
    print >> sys.stderr, "usage: python parse_experiment.py list_of_program_prefixes"

def main():
    dataBucket = {} # map to list of lists
    fname = sys.argv[1]
    prefix_fnames = open(fname, 'r')
    for prefix in prefix_fnames:
        prefix = prefix.strip()
        if len(prefix) > 0:

            # Add this prefix to the data bucket
            dataBucket[prefix] = []
            dataBucket[prefix].append([]) # list for modified data time
            dataBucket[prefix].append([]) # list for unmodified data time

            dataBucket[prefix].append([]) # first modified
            dataBucket[prefix].append([]) # first unmodified

            dataBucket[prefix].append([]) # last modified
            dataBucket[prefix].append([]) # last unmodified
            print >> sys.stderr, "Parsing prefix: " + str(prefix)

            for dirpath, dnames, fnames in os.walk("."):
                for f in fnames:
                    if f.startswith(prefix):
                        full = os.path.join(dirpath, f)

                        # Extract time
                        ftimef = open(full, 'r')
                        size = 0
                        time = 0
                        for l in ftimef:
                            if "TIME:" in l:
                                data = l.split(":")[1].split(",")
                                size = int(data[0])
                                time = float(data[1])
                                break
                        if ".first." in f and ".mod" in f:
                            dataBucket[prefix][2].append((size, time))
                        elif ".first." in f:
                            dataBucket[prefix][3].append((size, time))
                        elif ".last." in f and ".mod" in f:
                            dataBucket[prefix][4].append((size, time))
                        elif ".last." in f:
                            dataBucket[prefix][5].append((size, time))
                        elif ".mod." in f:
                            dataBucket[prefix][0].append((size, time))
                        else:
                            dataBucket[prefix][1].append((size, time))

            # Generate CSV output for first comparison
            csv = "size,optimized,unoptimized\n"
            total1 = {}
            count1 = {}
            for i in range(len(dataBucket[prefix][0])):
                size = dataBucket[prefix][0][i][0]
                if not (size in total1):
                    total1[size] = 0.0
                    count1[size] = 0
                total1[size] = total1[size] + dataBucket[prefix][0][i][1]
                count1[size] = count1[size] + 1
            avg1 = {}
            for i in total1:
                avg1[i] = total1[i] / count1[i]

            total2 = {}
            count2 = {}
            for i in range(len(dataBucket[prefix][1])):
                size = dataBucket[prefix][1][i][0]
                if not (size in total2):
                    total2[size] = 0.0
                    count2[size] = 0
                total2[size] = total2[size] + dataBucket[prefix][1][i][1]
                count2[size] = count2[size] + 1
            avg2 = {}
            for i in total2:
                avg2[i] = total2[i] / count2[i]

            for i in avg1:
                for j in avg2:
                    if i == j:
                        csv = csv + str(i) + "," + str(avg1[i]) + "," + str(avg2[i]) + "\n"
            
            # Write the data to a CSV file
            csvf = open(prefix + ".data.csv", 'w')
            csvf.write(csv + "\n")
            csvf.close()

            ###### FIRST

            # Generate CSV output for first comparison
            csv = "size,optimized,unoptimized\n"
            total1 = {}
            count1 = {}
            for i in range(len(dataBucket[prefix][2])):
                size = dataBucket[prefix][2][i][0]
                if not (size in total1):
                    total1[size] = 0.0
                    count1[size] = 0
                total1[size] = total1[size] + dataBucket[prefix][2][i][1]
                count1[size] = count1[size] + 1
            avg1 = {}
            for i in total1:
                avg1[i] = total1[i] / count1[i]

            total2 = {}
            count2 = {}
            for i in range(len(dataBucket[prefix][3])):
                size = dataBucket[prefix][3][i][0]
                if not (size in total2):
                    total2[size] = 0.0
                    count2[size] = 0
                total2[size] = total2[size] + dataBucket[prefix][3][i][1]
                count2[size] = count2[size] + 1
            avg2 = {}
            for i in total2:
                avg2[i] = total2[i] / count2[i]

            for i in avg1:
                for j in avg2:
                    if i == j:
                        csv = csv + str(i) + "," + str(avg1[i]) + "," + str(avg2[i]) + "\n"
            
            # Write the data to a CSV file
            csvf = open(prefix + ".first.data.csv", 'w')
            csvf.write(csv + "\n")
            csvf.close()

            ###### LAST

            # Generate CSV output for first comparison
            csv = "size,optimized,unoptimized\n"
            total1 = {}
            count1 = {}
            for i in range(len(dataBucket[prefix][4])):
                size = dataBucket[prefix][4][i][0]
                if not (size in total1):
                    total1[size] = 0.0
                    count1[size] = 0
                total1[size] = total1[size] + dataBucket[prefix][4][i][1]
                count1[size] = count1[size] + 1
            avg1 = {}
            for i in total1:
                avg1[i] = total1[i] / count1[i]

            total2 = {}
            count2 = {}
            for i in range(len(dataBucket[prefix][5])):
                size = dataBucket[prefix][5][i][0]
                if not (size in total2):
                    total2[size] = 0.0
                    count2[size] = 0
                total2[size] = total2[size] + dataBucket[prefix][5][i][1]
                count2[size] = count2[size] + 1
            avg2 = {}
            for i in total2:
                avg2[i] = total2[i] / count2[i]

            for i in avg1:
                for j in avg2:
                    if i == j:
                        csv = csv + str(i) + "," + str(avg1[i]) + "," + str(avg2[i]) + "\n"
            
            # Write the data to a CSV file
            csvf = open(prefix + ".last.data.csv", 'w')
            csvf.write(csv + "\n")
            csvf.close()

if __name__ == "__main__":
    main()
