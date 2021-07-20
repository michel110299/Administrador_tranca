from django.db import models

class Pessoa(models.Model):

    Nome = models.CharField(
        verbose_name = "Nome completo",
        max_length = 194,
    )
    DataCadastro = models.DateTimeField(verbose_name="Data de cadastro",auto_now_add=True)

    class Meta:
        verbose_name = "Pessoa"
        db_table = "pessoa"

    def __str__(self):
        return self.Nome


class Equipe(models.Model):
    
    Pessoas = models.ManyToManyField(Pessoa)
    Nome = models.CharField(
        verbose_name = "Nome da Equipe",
        max_length = 194,
    )

    DataCadastro = models.DateTimeField(verbose_name="Data de cadastro",auto_now_add=True)

    class Meta:
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"

    def __str__(self):
        return self.Nome


class Jogo(models.Model):
    Vencedora = models.ForeignKey(Equipe,on_delete=models.CASCADE,null=True, verbose_name="vencedora", related_name='vencedora')
    Perdedora = models.ForeignKey(Equipe,on_delete=models.CASCADE,null=True, verbose_name="perdedora", related_name='perdedora')
    Equipes = models.ManyToManyField(Equipe, related_name='equipes')
    Nome = models.CharField(
        verbose_name = "Nome do Jogo",
        max_length = 194,
    )
    DataCadastro = models.DateTimeField(verbose_name="Data de cadastro",auto_now_add=True)

    class Meta:
        verbose_name = "Jogos"
        verbose_name_plural = "Jogos"

    def __str__(self):
        return self.Nome


class Partida(models.Model):
    Vencedora = models.ForeignKey(Equipe,on_delete=models.CASCADE,null=True, verbose_name="Equipe_vencedora", related_name='Equipe_vencedora')
    Perdedora = models.ForeignKey(Equipe,on_delete=models.CASCADE,null=True, verbose_name="Equipe_perdedora", related_name='Equipe_perdedora')
    Jogo = models.ForeignKey(Jogo,on_delete=models.CASCADE, verbose_name="Jogo", related_name='Jogo')
    Fim = models.BooleanField(verbose_name="Status da partida", default=False)
    DataCadastro = models.DateTimeField(verbose_name="Data de cadastro",auto_now_add=True)

    class Meta:
        verbose_name = "Partida"
        verbose_name_plural = "Partidas"

    def __str__(self):
        return str(self.Jogo)

class Rodada(models.Model):
    Equipe = models.ForeignKey(Equipe,on_delete=models.CASCADE,verbose_name="Equipe")
    Partida = models.ForeignKey(Partida,on_delete=models.CASCADE, verbose_name="Partida", related_name='Partida')
    QtdRed = models.PositiveIntegerField(verbose_name="Quantidade de 3 vermelhos")
    QtdBlack = models.PositiveIntegerField(verbose_name="Quantidade de 3 pretos")
    QtdCartas = models.PositiveIntegerField(verbose_name="Quantidade de cartas")
    PontosCanastra = models.IntegerField(verbose_name="Pontos totais de canastra")
    TotalPontos = models.IntegerField(verbose_name="Pontos totais")
    Morto = models.BooleanField(verbose_name="Pegou morto", default=False)
    DataCadastro = models.DateTimeField(verbose_name="Data de cadastro",auto_now_add=True)

    class Meta:
        verbose_name = "Rodada"
        verbose_name_plural = "Rodadas"

    def __str__(self):
        return str(self.Equipe)