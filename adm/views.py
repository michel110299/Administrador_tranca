from django.shortcuts import render,redirect
from adm.models import *

def ViewInicio(request):
    listJogos = Jogo.objects.all()

    context = {
        "listJogos":listJogos,
    }

    return render(request,"inicio.html",context)

def ViewCadastro(request):
    if request.method == "POST":
        listPessoas = request.POST.getlist('Jogador[]', None)
        x=0
        objJogo = Jogo()
        for pessoa in listPessoas:
            objPessoa = Pessoa()
            objPessoa.Nome = pessoa
            objPessoa.save()

            if (x%2) == 0:
                objEquipe = Equipe()
                objPessoaAux = objPessoa

                objEquipe.Nome = objPessoa 
                objEquipe.save()
                objEquipe.Pessoas.add(objPessoa)
            else:
                objEquipe.Nome = "(" + str(objPessoa) + '/' + str(objPessoaAux) + ")"
                objEquipe.save()
                objEquipe.Pessoas.add(objPessoa)

                objJogo.Nome += objEquipe.Nome
                objJogo.save()
                objJogo.Equipes.add(objEquipe)
            x+=1
        return redirect("InicioJogo", objJogo.id)

    return render(request,"cadastro.html")

def ViewInicioJogo(request,idJogo):
    objJogo = Jogo.objects.get(pk=idJogo)
    listEquipes = objJogo.Equipes.all()

    if request.method == "POST":

        try:
            ObjPartida = Partida.objects.get(Jogo=objJogo,Fim=False)
        except:
            ObjPartida = Partida()
            ObjPartida.Jogo = objJogo
            ObjPartida.save()

        listRodada=[]

        for index, PtsCanastra in enumerate(request.POST.getlist('PtsCanastra[]')):      

            obj = {
                "PtsCanastra": PtsCanastra,
                "QtdCartas" :request.POST.getlist("QtdCartas[]", None)[index],
                "QtdRed" : request.POST.getlist("QtdRed[]", None)[index],
                "QtdBlack" : request.POST.getlist("QtdBlack[]", None)[index],
                # "Morto" : request.POST.getlist("Morto[]", None)[index],
            }
            listRodada.append(obj)

        EquipeSelecionada=0
        MaiorPontuacao = 0
        for rodada in listRodada:
            ObjRodada = Rodada()
            ObjRodada.Partida = ObjPartida
            ObjRodada.Equipe = listEquipes[EquipeSelecionada]
            ObjRodada.PontosCanastra = rodada["PtsCanastra"]
            ObjRodada.QtdCartas = rodada["QtdCartas"]
            ObjRodada.QtdRed = rodada["QtdRed"]
            ObjRodada.QtdBlack = rodada["QtdBlack"]
            ObjRodada.Morto = True
            ObjRodada.TotalPontos = 0
            
            if int(ObjRodada.PontosCanastra) < 100:
                ObjRodada.TotalPontos = (((int(ObjRodada.PontosCanastra) + (int(ObjRodada.QtdCartas)*10)) - (100*int(ObjRodada.QtdRed))) - (int(ObjRodada.QtdBlack)*100))
            else:
                ObjRodada.TotalPontos = (((int(ObjRodada.PontosCanastra) + (int(ObjRodada.QtdCartas)*10)) + (100*int(ObjRodada.QtdRed))) - (int(ObjRodada.QtdBlack)*100))
            
            if ObjRodada.Morto == False:
                ObjRodada.TotalPontos -= 100
            
            ObjRodada.save()
            
            try:
                listRodadas = Rodada.objects.filter(Partida=ObjPartida,Equipe=listEquipes[EquipeSelecionada])
                totalpontos = 0
                
                for rodada in listRodadas:
                    totalpontos += rodada.TotalPontos
                    if totalpontos >= 3000:
                        if MaiorPontuacao == 0:
                            MaiorPontuacao = totalpontos
                        if MaiorPontuacao <= totalpontos:
                            ObjPartida.Vencedora = listEquipes[EquipeSelecionada]
                            ObjPartida.Fim = True
                            for eq in listEquipes:
                                if eq != listEquipes[EquipeSelecionada]:
                                    ObjPartida.Perdedora = eq
                    ObjPartida.save()

            except:
                listRodadas = []

            EquipeSelecionada+=1

        ListPartida = Partida.objects.filter(Jogo=objJogo)
        listEquipe1 = []
        listEquipe2 = []

        print("estou aqui")
        for partida in ListPartida:
            if partida.Vencedora == listEquipes[0]:
                listEquipe1.append(partida)
            else:
                listEquipe2.append(partida)
        

        if len(listEquipe1)>len(listEquipe2):
            print(f'{listEquipes[0]} vencedora')
            objJogo.Vencedora = listEquipes[0]
            objJogo.Perdedora = listEquipes[1]

        elif len(listEquipe2)>len(listEquipe1):
            print(f'{listEquipes[1]} vencedora')
            objJogo.Vencedora = listEquipes[1]
            objJogo.Perdedora = listEquipes[0]

        else:
            print("empate")
            objJogo.Vencedora = None
            objJogo.Perdedora = None
        
        objJogo.save()
        
    context = {
        "objJogo":objJogo,
        "listEquipes":listEquipes,
    }

    return render(request,"inicio_jogo.html",context)


def ViewResultado(request,idJogo):
    objJogo = Jogo.objects.get(pk=idJogo)
    try:
        ListPartidas = Partida.objects.filter(Jogo=objJogo)
    except:
        ListPartidas = []

    context = {
        "objJogo":objJogo,
        "ListPartidas":ListPartidas,
    }

    return render(request,"resultados.html",context)


def ViewInfo(request,idPartida,idJogo):
    objJogo = Jogo.objects.get(pk=idJogo)
    ObjPartida = Partida.objects.get(pk=idPartida)
    try:
        ListRodada = Rodada.objects.filter(Partida=ObjPartida)
    except:
        ListRodada = []
    context = {
        "ObjPartida":ObjPartida,
        "ListRodada":ListRodada,
        "objJogo":objJogo,
    }

    return render(request,"mais_informacoes.html",context)


