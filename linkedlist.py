class SLL:
    def __init__(self,a=[],is_LL=False,LL_end=None):
        self.dead=False
        if is_LL:
            self.L=[None,a]
            self.end=LL_end
        else:
            self.L=[None,[]]
            c=self.L
            for i in range(len(a)):
                c=c[-1]
                c+=[a[i],[]]
            self.end=c

    def __len__(self):
        if self.dead:return 0
        c=self.L
        n=0
        while c[-1]:
            c=c[-1]
            n+=1
        return n

    def __getitem__(self,index):
        if self.dead:return None
        c=self.L
        index += 1
        while c[-1] and index:
            c=c[-1]
            index-=1
        return None if index else c[0]

    def __setitem__(self,index,val):
        if self.dead:return None
        c=self.L
        index += 1
        while c[-1] and index:
            c=c[-1]
            index-=1
        if not index:c[0]=val

    def to_list(self):
        if self.dead:return None
        a=[]
        c=self.L
        while c[-1]:
            c=c[-1]
            a.append(c[0])
        return a

    def __repr__(self):
        if self.dead:return "Destroyed"
        return str(self.to_list())

    def getptr(self,index):
        if self.dead:return None
        c=self.L
        index += 1
        while c[-1] and index:
            c=c[-1]
            index-=1
        return None if index else c

    def merge_left(self,other,check='SLL'):
        if self.dead:return None
        assert type(other)==eval(check) and other.dead==False
        other.end[-1]+=self.L[-1]
        self.L=other.L
        other.dead=True

    def merge_right(self,other,check='SLL'):
        if self.dead:return None
        assert type(other)==eval(check) and other.dead==False
        self.end[-1]+=other.L[-1]
        self.end=other.end
        other.dead=True

    def index(self,val):
        if self.dead:return None
        c=self.L
        index=-1
        found=False
        while c[-1]:
            c=c[-1]
            index+=1
            if c[0]==val:
                found=True
                break
        return index if found else -1

    def append(self,val):
        if self.dead:return None
        self.end[-1]+=[val,[]]
        self.end=self.end[-1]

    def appendleft(self,val):
        if self.dead:return None
        self.L[-1]=[val,self.L[-1]]

    def insert_after(self,p,val):
        if self.dead:return None
        p[-1]=[val,p[-1]]

    def split_after(self,p):
        if self.dead:return None
        c=p[-1]
        p[-1]=[]
        c=SLL(c,is_LL=True,LL_end=self.end)
        self.end=p
        return c

    def extend(self,a):
        if self.dead:return None
        for i in a:self.append(i)

    def extend_left(self,a):
        if self.dead:return None
        for i in a:self.appendleft(i)

    def copy(self):
        return SLL(self.to_list())

class DLL(SLL):
    def __init__(self,a,is_LL=False,LL_end=None):
        self.dead=False
        if is_LL:
            self.L=[None,None,a]
            self.end=LL_end
        else:
            self.L=[None,None,[]]
            c=self.L
            for i in range(len(a)):
                p=c
                c=c[-1]
                c+=[a[i],p,[]]
            self.end=c

    def append(self,val):
        if self.dead:return None
        self.end[-1]+=[val,self.end,[]]
        self.end=self.end[-1]

    def appendleft(self,val):
        if self.dead:return None
        self.L[-1]=[val,self.L,self.L[-1]]
        self.L[-1][-1][1]=self.L[-1]

    def insert_after(self,p,val):
        if self.dead:return None
        p[-1]=[val,p,p[-1]]
        p[-1][-1][1]=p[-1]

    def insert_before(self,p,val):
        if self.dead:return None
        self.insert_after(p[1],val)

    def split_before(self,p):
        if self.dead:return None
        self.split_after(p[1])

    def merge_left(self,other,check='DLL'):
        if self.dead:return None
        assert type(other)==eval(check) and other.dead==False
        self.L[-1][1]=other.end
        other.end[-1]+=self.L[-1]
        self.L=other.L
        other.dead=True

    def merge_right(self,other,check='DLL'):
        if self.dead:return None
        assert type(other)==eval(check) and other.dead==False
        other.L[-1][1]=self.end
        self.end[-1]+=other.L[-1]
        self.end=other.end
        other.dead=True

    def copy(self):
        return DLL(self.to_list())
