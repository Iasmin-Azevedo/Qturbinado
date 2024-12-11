from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional

app = FastAPI()


# Modelos
class Nota(BaseModel):
    valor: float
    
class Aluno(BaseModel):
    id: int
    nome: str
    notas: List[float]


class AlunoComMedia(BaseModel):
    id: int
    nome: str
    media: Optional[float]  # Pode ser None caso não haja notas


# "Banco de dados" em memória
alunos: Dict[int, Aluno] = {
    1: Aluno(id=1, nome="Iasmin", notas=[9.0, 8.5, 7.5]),
    2: Aluno(id=2, nome="Jordana", notas=[8.0, 7.5, 8.5]),
    3: Aluno(id=3, nome="Weslem", notas=[7.0, 6.5, 8.0]),
    4: Aluno(id=4, nome="Kaela", notas=[9.5, 8.0, 9.0]),
    5: Aluno(id=5, nome="Paulo Victor", notas=[8.5, 8.0, 8.0]),
    6: Aluno(id=6, nome="Williams", notas=[7.5, 7.0, 6.5]),
}

# Endpoints


# 1. Listar todos os alunos e suas médias
@app.get("/alunos", response_model=List[AlunoComMedia])
async def listar_alunos():
    lista = [
        AlunoComMedia(
            id=aluno.id,
            nome=aluno.nome,
            media=round(sum(aluno.notas) / len(aluno.notas), 1)
            if aluno.notas
            else None,
        )
        for aluno in alunos.values()
    ]
    return lista


# 2. Adicionar um novo aluno
@app.post("/alunos", response_model=Aluno)
async def criar_aluno(aluno: Aluno):
    if aluno.id in alunos:
        raise HTTPException(status_code=400, detail="Aluno com este ID já existe.")
    alunos[aluno.id] = aluno
    return aluno


# 3. Atualizar informações de um aluno
@app.put("/alunos/{aluno_id}", response_model=Aluno)
async def atualizar_aluno(aluno_id: int, aluno: Aluno):
    if aluno_id not in alunos:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    alunos[aluno_id] = aluno
    return aluno


# 4. Deletar um aluno
@app.delete("/alunos/{aluno_id}", response_model=Aluno)
async def deletar_aluno(aluno_id: int):
    if aluno_id not in alunos:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    aluno = alunos.pop(aluno_id)
    return aluno


# 5. Obter informações detalhadas de um aluno
@app.get("/alunos/{aluno_id}", response_model=AlunoComMedia)
async def obter_aluno(aluno_id: int):
    aluno = alunos.get(aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    return AlunoComMedia(
        id=aluno.id,
        nome=aluno.nome,
        media=round(sum(aluno.notas) / len(aluno.notas), 1) if aluno.notas else None,
    )


# 6. Adicionar nota para um aluno
@app.post("/alunos/{aluno_id}/notas", response_model=Aluno)
async def adicionar_nota(aluno_id: int, nota: Nota):
    aluno = alunos.get(aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    aluno.notas.append(nota.valor)
    return aluno