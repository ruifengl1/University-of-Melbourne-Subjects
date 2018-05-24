import sys
import json
import time
import numpy as np
import re
import mpi4py.MPI as MPI

start_time = time.time()

class Grid:
    Id=''
    xmin=0
    xmax=0
    ymin=0
    ymax=0
    
    def __init__(self,Id,xmin,xmax,ymin,ymax):
        self.Id=Id
        self.xmax=xmax
        self.xmin=xmin
        self.ymax=ymax
        self.ymin=ymin
   
        
'''Build up Melbourne Grid using object array'''
def read_melbGrid(melbGrids,filepath): 
        with open(filepath,'r') as gridFile:
                melbGrid_json = json.load(gridFile)
                for grid in melbGrid_json['features']:
                    melbGrids.append(
                            Grid(grid['properties']['id'],
                            grid['properties']['xmin'],
                            grid['properties']['xmax'],
                            grid['properties']['ymin'],
                            grid['properties']['ymax'],
                            ))

'''Reading the Instagram data from file and sorted out to different blocks  '''       
def read_Instagram(coordinateArray,filepath):
    coordinate=r'"coordinates":\[(.+?)\]'## used for regex
    with open(filepath,'r') as instagramFile:
        for post in instagramFile:
            if 'coordinates' in post:
                match = re.search(coordinate,post) ## Search for  the coordinate each line
                if match:
                    match='{'+match.group(0)+'}' ## Struct to json format in string 
                    match_json= json.loads(match) ## Convert coordinate to json format
                    
                    ##Function used for append coordinates to array
                    coordinateArray.append(match_json["coordinates"])
                    

'''Sorted out different coordinates to corresponding dict'''
def sortOut(coordinateArray,melbGrids,melbGrids_dict,letter_dict,digit_dict):
    for coordinate in coordinateArray:    
        for grid in melbGrids:
            if coordinate[0] and coordinate[1]:
                if coordinate[1] < grid.xmax and coordinate[1] >grid.xmin and coordinate[0]>grid.ymin and coordinate[0]<grid.ymax:

                    melbGrids_dict[grid.Id]+=1
                    letter_dict[grid.Id[0]]+=1
                    digit_dict[grid.Id[1]]+=1
            

'''Combine two dict together'''   
def merge(d1, d2):
    for key in d2:
        if key in d1:
            d1[key] += d2[key]
        else:
            d1[key] = d2[key]
    return d1

''' Initialize 3 dicts'''
def dictInitialize(melbGrids,melbGrids_dict,letter_dict,digit_dict):
    for grid in melbGrids:
        melbGrids_dict[grid.Id]=0
        if grid.Id[0] not in letter_dict:
            letter_dict[grid.Id[0]] =0
        if grid.Id[1] not in digit_dict:
            digit_dict[grid.Id[1]] = 0


'''Combine all dicts' result together'''
def combineDict(final_grids_dict,final_letter_dict,final_digit_dict,new_grids_dict,new_letter_dict,new_digit_dict):
        for i in range(len(new_grids_dict)):
            final_grids_dict = merge(final_grids_dict, new_grids_dict[i])
        for i in range(len(new_letter_dict)):
            final_letter_dict = merge(final_letter_dict, new_letter_dict[i])
        for i in range(len(new_digit_dict)):
            final_digit_dict = merge(final_digit_dict, new_digit_dict[i])
    


'''Rank results based on flatten array, rows and columns '''
def rankAll(final_grids_dict,final_letter_dict,final_digit_dict):

        print("Rank the Grid boxes based on the total number of instagram posts")
        for k, v in sorted(final_grids_dict.items(), key=lambda e: e[1], reverse=True):
            print(k,':',v,'posts')
        print("Rank the Rows based on the total number of instagram posts")
        for k, v in  sorted(final_letter_dict.items(), key=lambda e: e[1], reverse=True):
            print(k,'-Row:',v,'posts')

        print("Rank the Columns based on the total number of instagram posts")
        for k, v in  sorted(final_digit_dict.items(), key=lambda e: e[1], reverse=True):
            print('Column',k,':',v,'posts')


def main():
    ## File path
    instagram_filepath=sys.argv[2]
    melbGrid_filepath=sys.argv[1]

    melbGrids=[]
    coordinateArray=[]
    melbGrids_dict={}
    letter_dict={}
    digit_dict={}

        
    ##initialize MPI
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    ## Read input file of melbGrid
    read_melbGrid(melbGrids,melbGrid_filepath)
    ## Read and retrive data from instagram
    read_Instagram(coordinateArray,instagram_filepath)
    ## Initialize 3 dicts
    dictInitialize(melbGrids,melbGrids_dict,letter_dict,digit_dict)
    
    
    ## Master                                                                                                                  
    if rank == 0:   
        ## split array into chunks based on cores
        data = np.array_split(coordinateArray,size)

    else:
        data= None
        
    ## Slave  
    data = comm.scatter(data,root=0)
    sortOut(data,melbGrids,melbGrids_dict,letter_dict,digit_dict)

    ## Gather all  dict from each rank
    new_grids_dict=comm.gather(melbGrids_dict,root=0)
    new_letter_dict=comm.gather(letter_dict,root=0)
    new_digit_dict=comm.gather(digit_dict,root=0)

    ## New dict used for final results
    final_grids_dict = {}
    final_letter_dict= {}
    final_digit_dict= {}
    
    ## Combine all results in Master
    if rank==0:

        combineDict(final_grids_dict,final_letter_dict,final_digit_dict,new_grids_dict,new_letter_dict,new_digit_dict)
        
        rankAll(final_grids_dict,final_letter_dict,final_digit_dict)
        
        ## Execution time 
        print("--- Totoal running time %s seconds ---" % round((time.time() - start_time),5))

        
if __name__=='__main__':
    main()
    




