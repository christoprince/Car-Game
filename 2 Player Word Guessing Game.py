from turtle import Screen
import tkinter
from tkinter import *
import time
import tkinter.font
import random as r
import turtle as t
ac=0
bc=0
cc=0
dc=0
ec=0
fc=0
gc=0
hc=0
ic=0
jc=0
kc=0
lc=0
mc=0
nc=0
oc=0
pc=0
qc=0
rc=0
sc=0
tc=0
uc=0
vc=0
wc=0
xc=0
yc=0
zc=0
chance=1
poscore=0
ptscore=0
canvas=tkinter.Tk()
canvas.geometry('1500x1000')
canvas.config(bg='teal')
let =tkinter.font.Font(family='Helvetica', size=9, weight='bold')
titlefont =tkinter.font.Font(family='comic sans ms', size=45, weight='bold')

ones=Label(text=poscore)
ones.config(font=tkinter.font.Font(family='comic sans ms',size=35,weight='bold'),bg='teal',fg='white')
ones.place(x=100,y=300)

twos=Label(text=ptscore)
twos.config(font=tkinter.font.Font(family='comic sans ms',size=35,weight='bold'),bg='teal',fg='white')
twos.place(x=1350,y=300)

top = Label(text='2 PLAYER WORD GAME')
top.config(font=titlefont,bg='teal',fg='cyan')
top.place(x=400,y=0)

name=Label(text='-Christopher Prince')
name.config(font=tkinter.font.Font(family='comic sans ms',size=25),bg='teal',fg='white')
name.place(x=1150,y=700)

player=Label(text='Player 1')
player.config(font=tkinter.font.Font(family='cooper black', size=40),bg='teal',fg='cyan')
player.place(x=600,y=250)

words=' blueprints breakdowns clipboards compatible complained complaints completing cornflakes decorating defaulting despicably destroying educations exhausting exhaustion flamingoes flourished forgivable fruitcakes godfathers graciously harvesting hospitable hypnotized impersonal importance introduces journalism lifeguards lubricated magnitudes methodical microwaves normalized trampoline lumberjack palindrome artichokes earthlings autopsying authorized tambourine thumbscrew thumbnails trapeziums ravenously reductions homecrafts harmonised hyperlinks carbonized campground clubmaster blacksmith blindworms bouldering brutalized broadlines factorised fightacks congratulations sportsman businesswoman suffering afflictions blessings dollars hankerchief forgivable frightsome goldbricks vegetables mocktails'
words=words.split(' ')
word=r.choice(words)
def winner():
    global word,ptscore,poscore,player
    if poscore+ptscore+1==word.count(''):
        if ptscore>poscore:
            player.after(0,player.destroy)
            player=Label(text='Player 2 is the Winner')
            player.config(font=tkinter.font.Font(family='comic sans ms', size=40,weight='bold'),bg='teal',fg='cyan')
            player.place(x=450,y=300)
        if poscore>ptscore:
            player.after(0,player.destroy)
            player=Label(text='Player 1 is the Winner')
            player.config(font=tkinter.font.Font(family='comic sans ms', size=40,weight='bold'),bg='teal',fg='cyan')
            player.place(x=450,y=300)
        if poscore==ptscore:
            player.after(0,player.destroy)
            player=Label(text='The match is a Tie')
            player.config(font=tkinter.font.Font(family='comic sans ms', size=40,weight='bold'),bg='teal',fg='cyan')
            player.place(x=500,y=300)
        wordwas=Label(text='The Word was '+word)
        wordwas.config(font=tkinter.font.Font(family='comic sans ms', size=40,weight='bold'),bg='teal',fg='cyan')
        wordwas.place(x=450,y=150)
end= Button(canvas.master, text="END",height=2,width=4, bg='red',fg='white',font=let, command=canvas.destroy  )
end.place(x=0,y=0)
        
def score():
    global twos,ones
    twos.after(0,twos.destroy)
    twos=Label(text=ptscore)
    twos.config(font=tkinter.font.Font(family='comic sans ms', size=35,weight='bold'),bg='teal',fg='white')
    twos.place(x=1350,y=300)
    ones.after(0,ones.destroy)
    ones=Label(text=poscore)
    ones.config(font=tkinter.font.Font(family='comic sans ms',size=35,weight='bold'),bg='teal',fg='white')
    ones.place(x=100,y=300)
def chances():
    global ac,player,chance
    if chance==1:
        player.after(0,player.destroy)
        player=Label(text='Player 2')
        player.config(font=tkinter.font.Font(family='cooper black', size=40),bg='teal',fg='cyan')
        player.place(x=600,y=250)
        chance=2
    elif chance==2:
        player.after(0,player.destroy)
        player=Label(text='Player 1')
        player.config(font=tkinter.font.Font(family='cooper black', size=40),bg='teal',fg='cyan')
        player.place(x=600,y=250)
        chance=1

def a():
    global ac,player,chance,a
    if ac==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('a')
        if chance==2:
            ptscore+=word.count('a')
    if 'a' not in word:
        a.after(0,a.destroy)
    elif 'a' in word:
        a.after(0,a.destroy)
        a= Button(canvas.master, text="A",height=2,width=3, bg='cyan',font=let,command= a)
        a.place(x=150,y=550)
    ac=1
    score()
    chances()
    winner()

def b():
    global bc,player,chance,b
    if bc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('b')
        if chance==2:
            ptscore+=word.count('b')
    bc=1
    score()
    chances()
    winner()
    if 'b' not in word:
        b.after(0,b.destroy)
    elif 'b' in word:
        b.after(0,b.destroy)
        b= Button(canvas.master, text="B",height=2,width=3, bg='cyan',font=let,command= b)
        b.place(x=600,y=600)
def c():
    global cc,player,chance,c
    if cc==0:
        global chance,poscore,ptscore,ones,twos 
        if chance==1:
            poscore+=word.count('c')
        if chance==2:
            ptscore+=word.count('c')
    if 'c' not in word:
        c.after(0,c.destroy)
    elif 'c' in word:
        c.after(0,c.destroy)
        c= Button(canvas.master, text="C",height=2,width=3, bg='cyan',font=let,command= a)
        c.place(x=400,y=600)
    cc=1
    score()
    chances()
    winner()
def d():
    global dc,player,chance,d
    if dc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('d')
        if chance==2:
            ptscore+=word.count('d')
    dc=1
    score()
    chances()
    winner()
    if 'd' not in word:
        d.after(0,d.destroy)
    elif 'd' in word:
        d.after(0,d.destroy)
        d= Button(canvas.master, text="D",height=2,width=3, bg='cyan',font=let,command= d)
        d.place(x=350,y=550)
def e():
    global ec,player,chance,e
    if ec==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('e')
        if chance==2:
            ptscore+=word.count('e')
    if 'e' not in word:
        e.after(0,e.destroy)
    else:
        e.after(0,e.destroy)
        e= Button(canvas.master, text="E",height=2,width=3, bg='cyan',font=let,command= e)
        e.place(x=300,y=500)
    ec=1
    score()
    chances()
    winner()
def f():
    global fc,player,chance,f
    if fc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('f')
        if chance==2:
            ptscore+=word.count('f')
    fc=1
    score()
    chances()
    winner()
    if 'f' not in word:
        f.after(0,f.destroy)
    else:
        f.after(0,f.destroy)
        f= Button(canvas.master, text="F",height=2,width=3, bg='cyan',font=let,command= f)
        f.place(x=450,y=550)
def g():
    global gc,player,chance,g
    if gc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('g')
        if chance==2:
            ptscore+=word.count('g')
    gc=1
    score()
    chances()
    if 'g' not in word:
        g.after(0,g.destroy)
    else:
        g.after(0,g.destroy)
        g= Button(canvas.master, text="G",height=2,width=3, bg='cyan',font=let,command= g)
        g.place(x=550,y=550)
def h():
    global hc,player,chance,h
    if hc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('h')
        if chance==2:
            ptscore+=word.count('h')
    hc=1
    score()
    chances()
    winner()
    if 'h' not in word:
        h.after(0,h.destroy)
    else:
        h.after(0,h.destroy)
        h= Button(canvas.master, text="H",height=2,width=3, bg='cyan',font=let,command= h)
        h.place(x=650,y=550)
def i():
    global ic,player,chance,i
    if ic==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('i')
        if chance==2:
            ptscore+=word.count('i')
    ic=1
    score()
    chances()
    winner()
    if 'i' not in word:
        i.after(0,i.destroy)
    else:
        i.after(0,i.destroy)
        i= Button(canvas.master, text="I",height=2,width=3, bg='cyan',font=let,command= i)
        i.place(x=800,y=500)
def j():
    global jc,player,chance,j
    if jc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('j')
        if chance==2:
            ptscore+=word.count('j')
    jc=1
    score()
    chances()
    winner()
    if 'j' not in word:
        j.after(0,j.destroy)
    else:
        j.after(0,j.destroy)
        j= Button(canvas.master, text="J",height=2,width=3, bg='cyan',font=let,command= j)
        j.place(x=750,y=550)
def k():
    global kc,player,chance,k
    if kc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('k')
        if chance==2:
            ptscore+=word.count('k')
    kc=1
    score()
    chances()
    winner()
    if 'k' not in word:
        k.after(0,k.destroy)
    else:
        k.after(0,k.destroy)
        k= Button(canvas.master, text="K",height=2,width=3, bg='cyan',font=let,command= k)
        k.place(x=850,y=550)
def l():
    global lc,player,chance,l
    if lc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('l')
        if chance==2:
            ptscore+=word.count('l')
    lc=1
    score()
    chances()
    winner()
    if 'l' not in word:
        l.after(0,l.destroy)
    else:
        l.after(0,l.destroy)
        l= Button(canvas.master, text="L",height=2,width=3, bg='cyan',font=let,command= l)
        l.place(x=950,y=550)
def m():
    global mc,player,chance,m
    if mc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('m')
        if chance==2:
            ptscore+=word.count('m')
    mc=1
    score()
    chances()
    winner()
    if 'm' not in word:
        m.after(0,m.destroy)
    else:
        m.after(0,m.destroy)
        m= Button(canvas.master, text="M",height=2,width=3, bg='cyan',font=let,command= m)
        m.place(x=800,y=600)
def n():
    global nc,player,chance,n
    if nc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('n')
        if chance==2:
            ptscore+=word.count('n')
    nc=1
    score()
    chances()
    winner()
    if 'n' not in word:
        n.after(0,n.destroy)
    else:
        n.after(0,n.destroy)
        n= Button(canvas.master, text="N",height=2,width=3, bg='cyan',font=let,command= n)
        n.place(x=700,y=600)
def o():
    global oc,player,chance,o
    if oc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('o')
        if chance==2:
            ptscore+=word.count('o')
    oc=1
    score()
    chances()
    winner()
    if 'o' not in word:
        o.after(0,o.destroy)
    else:
        o.after(0,o.destroy)
        o= Button(canvas.master, text="O",height=2,width=3, bg='cyan',font=let,command= o)
        o.place(x=900,y=500)
def p():
    global pc,player,chance,p
    if pc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('p')
        if chance==2:
            ptscore+=word.count('p')
    pc=1
    score()
    chances()
    if 'p' not in word:
        p.after(0,p.destroy)
    else:
        p.after(0,p.destroy)
        p= Button(canvas.master, text="P",height=2,width=3, bg='cyan',font=let,command= p)
        p.place(x=1000,y=500)
    winner()
def q():
    global qc,player,chance,q
    if qc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('q')
        if chance==2:
            ptscore+=word.count('q')
    qc=1
    score()
    chances()
    winner()
    if 'q' not in word:
        q.after(0,q.destroy)
    else:
        q.after(0,q.destroy)
        q= Button(canvas.master, text="Q",height=2,width=3, bg='cyan',font=let,command= q)
        q.place(x=100,y=500)
def r():
    global rc,player,chance,r
    if rc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('r')
        if chance==2:
            ptscore+=word.count('r')
    rc=1
    score()
    chances()
    winner()
    if 'r' not in word:
        r.after(0,r.destroy)
    else:
        r.after(0,r.destroy)
        r= Button(canvas.master, text="R",height=2,width=3, bg='cyan',font=let,command= r)
        r.place(x=400,y=500)
def s():
    global sc,player,chance,s
    if sc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('s')
        if chance==2:
            ptscore+=word.count('s')
    sc=1
    score()
    chances()
    winner()
    if 's' not in word:
        s.after(0,s.destroy)
    else:
        s.after(0,s.destroy)
        s= Button(canvas.master, text="S",height=2,width=3, bg='cyan',font=let,command= s)
        s.place(x=250,y=550)
def t():
    global tc,player,chance,t
    if tc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('t')
        if chance==2:
            ptscore+=word.count('t')
    tc=1
    score()
    chances()
    winner()
    if 't' not in word:
        t.after(0,t.destroy)
    else:
        t.after(0,t.destroy)
        t= Button(canvas.master, text="T",height=2,width=3, bg='cyan',font=let,command= t)
        t.place(x=500,y=500)
def u():
    global uc,player,chance,u
    if uc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('u')
        if chance==2:
            ptscore+=word.count('u')
    uc=1
    score()
    chances()
    winner()
    if 'u' not in word:
        u.after(0,u.destroy)
    else:
        u.after(0,u.destroy)
        u= Button(canvas.master, text="U",height=2,width=3, bg='cyan',font=let,command= u)
        u.place(x=700,y=500)
def v():
    global vc,player,chance,v
    if vc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('v')
        if chance==2:
            ptscore+=word.count('v')
    vc=1
    score()
    chances()
    winner()
    if 'v' not in word:
        v.after(0,v.destroy)
    else:
        v.after(0,v.destroy)
        v= Button(canvas.master, text="V",height=2,width=3, bg='cyan',font=let,command= v)
        v.place(x=500,y=600)
def w():
    global wc,player,chance,w
    if wc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('w')
        if chance==2:
            ptscore+=word.count('w')
    wc=1
    score()
    chances()
    winner()
    if 'w' not in word:
        w.after(0,w.destroy)
    else:
        w.after(0,w.destroy)
        w= Button(canvas.master, text="W",height=2,width=3, bg='cyan',font=let,command= w)
        w.place(x=200,y=500)
def x():
    global xc,player,chance,x
    if xc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('x')
        if chance==2:
            ptscore+=word.count('x')
    xc=1
    score()
    chances()
    winner()
    if 'x' not in word:
        x.after(0,x.destroy)
    else:
        x.after(0,x.destroy)
        x= Button(canvas.master, text="X",height=2,width=3, bg='cyan',font=let,command= x)
        x.place(x=300,y=600)
def y():
    global yc,player,chance,y
    if yc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('y')
        if chance==2:
            ptscore+=word.count('y')
    yc=1
    score()
    chances()
    winner()
    if 'y' not in word:
        y.after(0,y.destroy)
    else:
        y.after(0,y.destroy)
        y= Button(canvas.master, text="Y",height=2,width=3, bg='cyan',font=let,command= y)
        y.place(x=600,y=500)
def z():
    global zc,player,chance,z
    if zc==0:
        global chance,poscore,ptscore,ones,twos , ptscore
        if chance==1:
            poscore+=word.count('z')
        if chance==2:
            ptscore+=word.count('z')
    zc=1
    score()
    chances()
    winner()
    if 'z' not in word:
        z.after(0,z.destroy)
    else:
        z.after(0,z.destroy)
        z= Button(canvas.master, text="Z",height=2,width=3, bg='cyan',font=let,command= z)
        z.place(x=200,y=600)
    
a= Button(canvas.master, text="A",height=2,width=3, bg='lime',font=let,command= a)
b= Button(canvas.master, text="B",height=2,width=3, bg='lawngreen',font=let, command=b )
c= Button(canvas.master, text="C", height=2,width=3, bg='lawngreen',font=let,command=c )
d= Button(canvas.master, text="D",height=2,width=3, bg='lime',font=let, command=d )
e= Button(canvas.master, text="E", height=2,width=3, bg='springgreen',font=let,command= e)
f= Button(canvas.master, text="F", height=2,width=3, bg='lime',font=let,command=f   )
g= Button(canvas.master, text="G",height=2,width=3, bg='lime',font=let, command= g   )
h= Button(canvas.master, text="H", height=2,width=3, bg='lime',font=let,command=h  )
i= Button(canvas.master, text="I", height=2,width=3, bg='springgreen',font=let,command=i  )
j= Button(canvas.master, text="J", height=2,width=3, bg='lime',font=let,command=j  )
k= Button(canvas.master, text="K", height=2,width=3, bg='lime',font=let,command=k  )
l= Button(canvas.master, text="L", height=2,width=3, bg='lime',font=let,command=l  )
m= Button(canvas.master, text="M", height=2,width=3, bg='lawngreen',font=let,command=m  )
n= Button(canvas.master, text="N", height=2,width=3, bg='lawngreen',font=let,command=n  )
o= Button(canvas.master, text="O", height=2,width=3, bg='springgreen',font=let,command=o  )
p= Button(canvas.master, text="P", height=2,width=3, bg='springgreen',font=let,command= p )
q= Button(canvas.master, text="Q", height=2,width=3, bg='springgreen',font=let,command= q   )
r= Button(canvas.master, text="R", height=2,width=3, bg='springgreen',font=let,command=  r  )
s= Button(canvas.master, text="S",height=2,width=3, bg='lime',font=let, command=   s )
t= Button(canvas.master, text="T",height=2,width=3, bg='springgreen',font=let, command=  t  )
u= Button(canvas.master, text="U", height=2,width=3, bg='springgreen',font=let,command=  u  )
v= Button(canvas.master, text="V",height=2,width=3, bg='lawngreen',font=let, command=   v )
w= Button(canvas.master, text="W", height=2,width=3, bg='springgreen',font=let,command=  w  )
x= Button(canvas.master, text="X", height=2,width=3, bg='lawngreen',font=let,command=   x )
y= Button(canvas.master, text="Y", height=2,width=3, bg='springgreen',font=let,command=  y  )
z= Button(canvas.master, text="Z",height=2,width=3, bg='lawngreen',font=let, command=z  )
q.place(x=100,y=500)
w.place(x=200,y=500)
e.place(x=300,y=500)
r.place(x=400,y=500)
t.place(x=500,y=500)
y.place(x=600,y=500)
u.place(x=700,y=500)
i.place(x=800,y=500)
o.place(x=900,y=500)
p.place(x=1000,y=500)
a.place(x=150,y=550)
s.place(x=250,y=550)
d.place(x=350,y=550)
f.place(x=450,y=550)
g.place(x=550,y=550)
h.place(x=650,y=550)
j.place(x=750,y=550)
k.place(x=850,y=550)
l.place(x=950,y=550)
m.place(x=800,y=600)
n.place(x=700,y=600)
b.place(x=600,y=600)
v.place(x=500,y=600)
c.place(x=400,y=600)
x.place(x=300,y=600)
z.place(x=200,y=600)

canvas.mainloop()
