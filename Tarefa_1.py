def viewonshell(textfile):
    file = open(textfile, 'r')
    filecontents = file.read()
    print(filecontents)
    file.close()
    
def views(textfile):
    f = open(textfile,'r')
    content = [line.strip('\n') for line in f.readlines()]
    return content

def channellist(contentlist):
    channels = []
    for c in contentlist:
        channels.append(c[0:3])
    return channels

def search(lst, channel):
    for index in lst:
        if index[0:3] == channel:
            return index
   
def selectionsort(lst):
    viewlist = []
    for v in lst:
        viewlist.append(int(v[4:6]))
    for i in range(len(viewlist)-1):
        min_index = i
        for j in range(i+1, len(viewlist)-1):
            if viewlist[j] < viewlist[min_index]:
                min_index = j
        viewlist[i], viewlist[min_index] = viewlist[min_index], viewlist[i]
    views = []
    for view in viewlist:
        views.append(str(view))
    sortedlst = []
    for y in views:
        for x in lst:
            if x[4:6] == y and x[0:3] not in sortedlst:
                sortedlst.append(x[0:3])
    return sortedlst

def searchviews(lst, channel, day):
    for index in lst:
        if index[0:3] == channel and index[7:8] == day:
            return index[4:6]

def main():
    print('F1 - Visualizações, F2 - Canal visto na semana, F3 - Lista dos canais por maior número de visualizações, F4 - Visualizações de um canal num dia')
    command = str(input('? '))
    if command == 'F1':
        viewonshell('visualizacoes.txt')
    if command == 'F2':
        viewlist = views('visualizacoes.txt')
        channels = channellist(viewlist)
        print(channels)
        choosechannel = str(input('Qual canal? '))
        print(search(viewlist, choosechannel))
    if command == 'F3':
        viewlist = views('visualizacoes.txt')
        print(selectionsort(viewlist))
    if command == 'F4':
        viewlist = views('visualizacoes.txt')
        channels = channellist(viewlist)        
        print(channels)
        daylist = ['1 - Segunda', '2 - Terça' , '3 - Quarta', '4 - Quinta' ,'5 - Sexta','6 - Sábado', '7 - Domingo']
        print(daylist)
        whichchannel = str(input('Qual canal? '))
        whichday  = str(input('Qual dia? '))
        print(searchviews(viewlist,whichchannel,whichday))

main()