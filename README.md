# Qturbinado
Uma API simples para cadastro de alunos, registro de notas e cálculo de médias, desenvolvida com FastAPI.

---

### Aluna:
**Iasmin Azevedo**

### Disciplina:
**Arquitetura de Sistemas**

### Professor:
**Gabriel Tavares**

---

## Endpoints 🌐

### 1 - **Listar Alunos** 📋
**GET** `/alunos`

Listar alunos.
**Responsta:**
```json
  {
    "id": 1,
    "nome": "Iasmin",
    "media": 8.3
  },...
```

### 2 - Adicionar aluno
**POST** `/alunos`
Adicionar um novo aluno.
**Responsta:**
```json
  {
    "id": 7,
    "nome": "Matheus",
    "notas": [
        8.0,
        8.0,
        9.0
    ]
  }
```

### 3 - Atualizar aluno
**GET** `/alunos/{aluno_id}`
Atualiza informacoes do aluno.
**Responsta:**
```json
  {
    "id": 1,
    "nome": "Iasmin Atualizada",
    "notas": [10.0, 9.0, 8.0]
  }
```

### 4 - Deletar aluno
**DELETE** `/alunos/{aluno_id}`
Deleta um aluno.
**Responsta:**
```json
  {
    [ -informacoes do aluno- ]
}
```

### 5 - Pesquisar aluno por ID
**GET** `/alunos/{aluno_id}`
Lista um aluno com id especificado
**Responsta:**
```json
  {
    "id": 2,
    "nome": "Jordana",
    "media": 8.0
  }
```

### 6 - Adicionar nota
**POST** `/alunos/{aluno_id}/notas`
Adiciona mais uma nota ao aluno
**Responsta:**
```json
  {
    "id": 3,
    "nome": "Weslem",
    "notas": [
        7.0,
        6.5,
        8.0,
        9.5,
        9.5
    ]
  }
```
## Como Executar 🚀

### Pré-requisitos

Antes de rodar o projeto, é necessário ter os seguintes pré-requisitos:

- Python 3.10+
- FastAPI
- Uvicorn

### Passos

1. **Clone o repositório**:
   Se você ainda não tem o projeto, clone-o para sua máquina local com o seguinte comando:
   ```bash
   git clone https://github.com/Iasmin-Azevedo/qturbinado.git
   cd qturbinado
   ```
  
2. Crie um ambiente virtual e ative-o:
   ```bash
     python -m venv venv
     source venv/bin/activate # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
     pip install -r requirements.txt
   ```

4. Execute o servidor:
   ```bash
     uvicorn main:app --reload
   ```
**Abra o navegador em:**
   - API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 📄
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) 📚

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
