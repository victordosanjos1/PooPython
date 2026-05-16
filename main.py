class Canal:
    def __init__(self, nome, descricao, inscritos): #Essa é classe principal esse init é com se fosse um codigo magico, 
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos
    
    def inscrever(self, quantidade = 1):
        self.inscritos += quantidade

class CanalEmpresarial(Canal):
    def __init__(self, nome, descricao, inscritos):
        super().__init__(nome, descricao, inscritos)
        self._equipe = []

    @property
    def equipe(self):
        return self._equipe
    
    def adcionar_membro_equipe(self, membro):
        if membro not in self._equipe:
            self._equipe.append(membro)
        else:
            print(f"O {membro} já está na equipe")
    
    def remover_membro_equipe(self, membro):
        if membro in self._equipe:
            self._equipe.remove(membro)
        else:
            print(f"O {membro} não está na equipe")

canal_Lanconde = Canal('Lan Code', 'Codigos e gatos', 34000)
canal_Guanabara = Canal('Canal Guanabara', 'Paixão por ensinar', 250000)
canal_Duolingo = CanalEmpresarial('Duolingo', 'Inglês', 4000000)
