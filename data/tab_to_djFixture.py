import argparse, os

# Command Line Arguments
parser = argparse.ArgumentParser(description='This script converts a tab file to a json fixture for django.')
parser.add_argument('-a', '--appname', help='Name of the app that owns the model: myawesomeapp', required=True)
parser.add_argument('-m', '--modelname', help='Name of the model the fixture is for: mydatamodel', required=True)
parser.add_argument('-i', '--input', help='Path to output json file: /users/name/jsonFileOutput.json', required=True)
parser.add_argument('-o', '--output', help='Path for output json file: /users/name/jsonFileOutput.json', required=True)
args = parser.parse_args()

# Arg Vars
model = args.appname + "." + args.modelname
ifile = args.input
ofile = args.output

with open (ifile, 'r') as fin:
    # store the file header info for later
    header = fin.readline().strip().split("\t")
    # clear out the contents of any pre-existing output file
    with open (ofile, 'wb') as fout:
        fout.write("[")
    # append the rest of the output to the json file
    with open (ofile, 'a') as fout:
        for index, line in enumerate(fin):
            values = line.strip().split("\t")
            fout.write("\n\t{\n\t\t\"model\": \"%s\",\n\t\t\"pk\": %d,\n\t\t\"fields\": {" % (model, index+1))
            for index, field in enumerate(header):
                # add a comma at the end of each field line iteration
                if index < len(header)-1:
                    try:
                        fout.write('\n\t\t\t\"%s\": \"%s\",' % (field, values[index]))
                    except IndexError:
                        fout.write('\n\t\t\t\"%s\": \"%s\",' % (field, ""))
                    except Exception as e:
                        print "Error on line ", index
                        print e
                # don't add a comma to the last field line though
                else:
                    try:
                        fout.write("\n\t\t\t\"%s\": \"%s\"\n\t\t}\n\t}," % (field, values[index]))
                    except IndexError:
                        fout.write("\n\t\t\t\"%s\": \"%s\"\n\t\t}\n\t}," % (field, ""))
                    except Exception as e:
                        print "Error on line ", index
                        print e
    # clean up the trailing comma and add the closing bracket
    with open (ofile, 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()
        filehandle.write("\n]")
