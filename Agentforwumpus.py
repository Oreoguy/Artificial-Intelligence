class Agent:
    def __init__(self):
        self.__wumpusWorld = [
                 ['','','P',''], 
                 ['P','','W',''],  
                 ['','P','P',''], 
                 ['','P','',''], 
                ] 
        self.__curLoc = [1,1]
        self.__isAlive = True
        self.__hasExited = False

    def __FindIndicesForLocation(self,loc):
        x,y = loc
        i,j = y-1, x-1
        return i,j

    def __CheckForPitWumpus(self):
        ww = self.__wumpusWorld
        i,j = self.__FindIndicesForLocation(self.__curLoc)
        if 'P' in ww[i][j] or 'W' in ww[i][j]:
            print(ww[i][j])
            self.__isAlive = False
            print('Agent back to the start.')
        return self.__isAlive

    def TakeAction(self,action): # The function takes an action and returns whether the Agent is alive
                                # after taking the action.
        validActions = ['Up','Down','Left','Right']
        assert action in validActions, 'Invalid Action.'
        if self.__isAlive == False:
            print('Action cannot be performed. Agent is back to the start. Location:{0}'.format(self.__curLoc))
            return False
        if self.__hasExited == True:
            print('Action cannot be performed. Agent has exited the Wumpus world.'.format(self.__curLoc))
            return False

        index = validActions.index(action)
        validMoves = [[0,1],[0,-1],[-1,0],[1,0]]
        move = validMoves[index]
        newLoc = []
        for v, inc in zip(self.__curLoc,move):
            z = v + inc #increment location index
            z = 4 if z>4 else 1 if z<1 else z #Ensure that index is between 1 and 4
            newLoc.append(z)
        self.__curLoc = newLoc
        print('Action Taken: {0}, Current Location {1}'.format(action,self.__curLoc))
        if self.__curLoc[0]==4 and self.__curLoc[1]==4:
            self.__hasExited=True
        return self.__CheckForPitWumpus()
    
    def __FindAdjacentRooms(self):
        cLoc = self.__curLoc
        validMoves = [[0,1],[0,-1],[-1,0],[1,0]]
        adjRooms = []
        for vM in validMoves:
            room = []
            valid = True
            for v, inc in zip(cLoc,vM):
                z = v + inc
                if z<1 or z>4:
                    valid = False
                    break
                else:
                    room.append(z)
            if valid==True:
                adjRooms.append(room)
        return adjRooms
                
        
    def PerceiveCurrentLocation(self): #This function perceives the current location. 
                                        #It tells whether breeze and stench are present in the current location.
        breeze, stench = False, False
        ww = self.__wumpusWorld
        if self.__isAlive == False:
            print('Agent cannot perceive. Agent is back to the start. Location:{0}'.format(self.__curLoc))
            return [None,None]
        if self.__hasExited == True:
            print('Agent cannot perceive. Agent is back to the start.'.format(self.__curLoc))
            return [None,None]

        adjRooms = self.__FindAdjacentRooms()
        for room in adjRooms:
            i,j = self.__FindIndicesForLocation(room)
            if 'P' in ww[i][j]:
                breeze = True
            if 'W' in ww[i][j]:
                stench = True
        return [breeze,stench]
    
    def FindCurrentLocation(self):
        return self.__curLoc

def main():
    ag = Agent()
    print('curLoc',ag.FindCurrentLocation())
    print('Percept [breeze, stench] :',ag.PerceiveCurrentLocation())
    ag.TakeAction('Right')
    print('Percept',ag.PerceiveCurrentLocation())
    ag.TakeAction('Right')
    print('Percept',ag.PerceiveCurrentLocation())
    ag.TakeAction('Right')
    print('Percept',ag.PerceiveCurrentLocation())
    ag.TakeAction('Up')
    print('Percept',ag.PerceiveCurrentLocation())
    ag.TakeAction('Up')
    print('Percept',ag.PerceiveCurrentLocation())
    ag.TakeAction('Up')
    print('Percept',ag.PerceiveCurrentLocation())


if __name__=='__main__':
    main()