__all__=["lire_fichier","separe","poser_questions"]

def _x0(_p):
    _r=[]
    _f=open(_p,'r',encoding='utf8')
    for _l in _f:
        _r.append(_l.rstrip("\n"))
    _f.close()
    return _r

def _x1(_t,_d):
    _q=[]
    for _e in _t:
        _q.append(_e.split(_d))
    return _q

def _x2(_L,_a):
    _s=0
    for _i in _L:
        print(_i[0])
        if _a==_i[1]:
            print("bravo !");_s+=1
        else:
            print("dommage")
    print(_s)

def lire_fichier():
    return _x0("projet-question.txt")

def separe(tab):
    return _x1(tab,";;")

def poser_questions(liste):
    return _x2(liste,"Blanc")
