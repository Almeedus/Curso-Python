# O que são?
# módulo que fornece um decorador e funções para criar métodos como: 
# __init__(), __repr() e __eq__() 

from dataclasses import dataclass, field

@dataclass(frozen=True, repr=False)
class Pessoa:
    nome: str | None = None
    sobrenome: str | None = None
    idade: int | None = None
    # nome_completo: str = field(init=False)

    # def __post_init__(self):
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'
        
    @property
    def nome_completo(self) -> str:
        return f'{self.nome} {self.sobrenome}'
    
    # @nome_completo.setter
    # def nome_completo(self, nome: str) -> None:
    #     nome, *sobrenome = nome.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)

if __name__ == '__main__':
    p1 = Pessoa('Eduardo', 'Almeida', 23)
    print(p1.nome_completo)
    print(p1)