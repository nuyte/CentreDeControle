import sys
import os


# configuration file

class Configuration :

    
    def __init__(self, number=0):

        # define which configuration file will be used in the scripts
        # if 0, the default file is used
        self.number = number
        

    def read_conf_file(self) :

        # function to read the main configuration file for the LAE LF pipeline

        if self.number == 0 : 
            fname = os.environ['MAINDIR'] + 'Input/configuration_default.txt'
        else : 
            fname = os.environ['MAINDIR'] + 'Input/configuration_'+\
                    str(self.number)+'.txt'

        with open(fname, 'r') as myFile :
            for line in myFile :

                # skipping comments 
                if '#' in line or len(line) <= 1 : continue

                # list of lensing fields
                if 'CLIST' in line :
                    clist = line.strip().split('=')[1]
                    clist = clist.split(',')
                    clist = [val.strip() for val in clist]

                # list of seeing for each fileds (in ") :
                if 'SEEING' in line :
                    line   = line.strip().split('=')
                    seeing = line[-1].split(',')
                    seeing = [float(val) for val in seeing]

         
                # Path towards the Muselt_NB images and dir
                if 'PATH_MUSELET_NB' in line :
                    muselet_nb_path =  line.strip().split('=')[1].strip()
                    muselet_nb_path = os.environ['MAINDIR'] + muselet_nb_path
                    
                # path toward the white light image
                if 'PATH_WL' in line :
                    path_wl = line.strip().split('=')[1].strip()
                    path_wl = os.environ['MAINDIR'] + path_wl

    
            
                # used to get path where we store intermediate data
                # for different subsets of the input data
                if 'PATH_DATA' in line :
                    path_data = str(line.strip().split('=')[1])

        return clist,seeing,muselet_nb_path,path_wl,path_data


    def get_clist(self) :

        # retunrs the list of lensing fields to be used in the entire pipeline

        return self.read_conf_file()[0]

    def get_seeing(self) :

        # retunrs the list of seeings for each field in clist, in the same order

        return self.read_conf_file()[11]



    def path2NB(self,name) :

        # returns the path to the cube NB dir 
        
        return self.read_conf_file()[2] + name + '/nb/'

  

    def readPathData(self) :

        # retuns the relative paths where all the intermediate data that
        # need to be separated for independants sets are stored
        
        return self.read_conf_file()[10].strip()



def countlines(start, lines=0, header=True, begin_start=None):

    # function used to count the lines of python code
    if header:
        print('{:>10} |{:>10} | {:<20}'.format('ADDED', 'TOTAL', 'FILE'))
        print('{:->11}|{:->11}|{:->20}'.format('', '', ''))

    for thing in os.listdir(start):
        thing = os.path.join(start, thing)
        if os.path.isfile(thing):
            if thing.endswith('.py'):
                with open(thing, 'r') as f:
                    newlines = f.readlines()
                    newlines = len(newlines)
                    lines += newlines

                    if begin_start is not None:
                        reldir_of_thing = '.' + thing.replace(begin_start, '')
                    else:
                        reldir_of_thing = '.' + thing.replace(start, '')

                    print('{:>10} |{:>10} | {:<20}'.format(
                            newlines, lines, reldir_of_thing))


    for thing in os.listdir(start):
        thing = os.path.join(start, thing)
        if os.path.isdir(thing):
            lines = countlines(thing, lines, header=False, begin_start=start)

    return lines
