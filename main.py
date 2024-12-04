from fastapi import FastAPI, HTTPException # type: ignore
from typing import List

app = FastAPI()

cursos = [
    {"id": 1, "nome": "Curso de Python", "preco_unitario": 200, "quantidade": 1},
    {"id": 2, "nome": "Curso de JavaScript", "preco_unitario": 150, "quantidade": 1},
    {"id": 3, "nome": "Código de ouro - Java ", "preco_unitario": 200, "quantidade": 1}
]

alunos = [
    {"id": 1, "nome": "Carlos Silva", "matricula": 12345, "cursos_matriculados": [1]},
    {"id": 2, "nome": "Ana Pereira", "matricula": 12346, "cursos_matriculados": [2]},
    {"id": 3, "nome": "João", "matricula": 12347, "cursos_matriculados": [2]}

]

professores = [
    {"id": 1, "nome": "Prof. João", "cursos_ensinado": [1]},
    {"id": 2, "nome": "Prof. Maria", "cursos_ensinado": [2]},
    {"id": 3, "nome": "Prof. Gabriel", "cursos_ensinado": [2]}

]

@app.get("/")
def bem_vindo():
    return {"Bem-vindo à API de Cursos! Use os endpoints disponíveis para navegar, como /alunos, /cursos, ou /professores."}

@app.get("/cursos", response_model=List[dict])
def listar_cursos():
    return cursos

@app.get("/curso/{curso_id}", response_model=dict)
def buscar_curso(curso_id: int):
    curso = next((curso for curso in cursos if curso["id"] == curso_id), None)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return curso

@app.post("/cursos", response_model=dict)
def adicionar_curso(curso: dict):
    novo_id = max(curso["id"] for curso in cursos) + 1 if cursos else 1
    curso["id"] = novo_id
    cursos.append(curso)
    return curso

@app.put("/curso/{curso_id}", response_model=dict)
def atualizar_curso(curso_id: int, curso: dict):
    curso_antigo = next((c for c in cursos if c["id"] == curso_id), None)
    if curso_antigo is None:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    
    curso_antigo.update(curso)
    return curso_antigo

@app.delete("/curso/{curso_id}")
def remover_curso(curso_id: int):
    global cursos
    cursos = [curso for curso in cursos if curso["id"] != curso_id]
    return {"message": f"Curso {curso_id} removido com sucesso"}

@app.get("/alunos", response_model=List[dict])
def listar_alunos():
    return alunos

@app.get("/aluno/{aluno_id}", response_model=dict)
def buscar_aluno(aluno_id: int):
    aluno = next((aluno for aluno in alunos if aluno["id"] == aluno_id), None)
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

@app.post("/alunos", response_model=dict)
def adicionar_aluno(aluno: dict):
    novo_id = max(aluno["id"] for aluno in alunos) + 1 if alunos else 1
    aluno["id"] = novo_id
    alunos.append(aluno)
    return aluno

@app.put("/aluno/{aluno_id}", response_model=dict)
def atualizar_aluno(aluno_id: int, aluno: dict):
    aluno_antigo = next((a for a in alunos if a["id"] == aluno_id), None)
    if aluno_antigo is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    
    aluno_antigo.update(aluno)
    return aluno_antigo

@app.delete("/aluno/{aluno_id}")
def remover_aluno(aluno_id: int):
    global alunos
    alunos = [aluno for aluno in alunos if aluno["id"] != aluno_id]
    return {"message": f"Aluno {aluno_id} removido com sucesso"}

@app.get("/professores", response_model=List[dict])
def listar_professores():
    return professores

@app.get("/professor/{professor_id}", response_model=dict)
def buscar_professor(professor_id: int):
    professor = next((professor for professor in professores if professor["id"] == professor_id), None)
    if professor is None:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    return professor

@app.post("/professores", response_model=dict)
def adicionar_professor(professor: dict):
    novo_id = max(professor["id"] for professor in professores) + 1 if professores else 1
    professor["id"] = novo_id
    professores.append(professor)
    return professor

@app.put("/professor/{professor_id}", response_model=dict)
def atualizar_professor(professor_id: int, professor: dict):
    professor_antigo = next((p for p in professores if p["id"] == professor_id), None)
    if professor_antigo is None:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    
    professor_antigo.update(professor)
    return professor_antigo

@app.delete("/professor/{professor_id}")
def remover_professor(professor_id: int):
    global professores
    professores = [professor for professor in professores if professor["id"] != professor_id]
    return {"message": f"Professor {professor_id} removido com sucesso"}
