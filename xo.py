dic={'a':' ','b':' ','c':' ','d':' ','e':' ','f':' ','g':' ','h':' ','i':' '}
def ass(number,turn):
    if turn%2==0:
        if number==1 and dic['a']=='':
            dic['a']='O'
        elif number==2:
            dic['b']='O'
        elif number==3:
            dic['c']='O'
            print('here')
        elif number==4:
            dic['d']='O'
        elif number==5:
            dic['e']='O'
        elif number==6:
            dic['f']='O'
        elif number==7:
            dic['g']='O'
        elif number==8:
            dic['h']='O'
        elif number==9:
            dic['i']='O'
    else:
        if number==1:
            dic['a']='X'
        elif number==2:
            dic['b']='X'
        elif number==3:
            dic['c']='X'
            print('here')
        elif number==4:
            dic['d']='X'
        elif number==5:
            dic['e']='X'
        elif number==6:
            dic['f']='X'
        elif number==7:
            dic['g']='X'
        elif number==8:
            dic['h']='X'
        elif number==9:
            dic['i']='X'

def display():
    
    
    print(turn)
    ##3dic['b']='X'
    A=dic['a']
    B=dic['b']
    C=dic['c']
    D=dic['d']
    E=dic['e']
    F=dic['f']
    G=dic['g']
    H=dic['h']
    I=dic['i']
    
    print(f'        |         |        ')
    print(f'    {A}   |    {B}    |   {C}  ')
    print(f'        |         |        ')
    print('-------------------------')
    print(f'        |         |        ')
    print(f'    {D}   |    {E}    |   {F}  ')
    print(f'        |         |        ')
    print('-------------------------')
    print(f'        |         |        ')
    print(f'    {G}   |    {H}    |   {I}  ')
    print(f'        |         |        ')
    #3return 0
def check():
    if ((dic['a']==dic['b']==dic['c']=='O') or (dic['d']==dic['e']==dic['f']=='O') or (dic['g']==dic['h']==dic['i']=='O') or (dic['a']==dic['d']==dic['g']=='O') or (dic['b']==dic['e']==dic['h']=='O') or (dic['c']==dic['f']==dic['i']=='O') or (dic['a']==dic['e']==dic['i']=='O') or (dic['c']==dic['e']==dic['g']=='O')):
        return 1
    elif ((dic['a']==dic['b']==dic['c']=='X') or (dic['d']==dic['e']==dic['f']=='X') or (dic['g']==dic['h']==dic['i']=='X') or (dic['a']==dic['d']==dic['g']=='X') or (dic['b']==dic['e']==dic['h']=='X') or (dic['c']==dic['f']==dic['i']=='X') or (dic['a']==dic['e']==dic['i']=='X') or (dic['c']==dic['e']==dic['g']=='X')):
        return 2
        
i=0
turn=1
while i<9:
    no=int(input('enter a no.'))
    ass(no,turn)
    display()
    w=check()
    if w==1:
        print('Player 1 Won!!!!')
        break;
    elif w==2:
        print('Player 2 Won!!!!')
        break;
    i=i+1
    turn=turn+1

