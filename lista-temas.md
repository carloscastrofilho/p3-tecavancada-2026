
{
  "tables": {
    "users": {
      "id": 1,
      "columns": {
        "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
        "name": { "type": "string", "size": 100, "nullable": false },
        "login": { "type": "string", "size": 150, "nullable": false },
        "password": { "type": "string", "size":254, "nullable": false },
        "created_at" : {"type": "datetime", "nullable": false, "default":true},
        "actived":{ "type":"boolean", "nullabre": false, "default":true}
      }
    },
    "roles" : {
      "id": 2,
      "columns": {
      "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
      "role": { "type": "string", "size": 100, "nullable": false },
      "created_at" : {"type": "datetime", "nullable": false, "default":true}
      }
    },
    "usersroles" : {
      "id": 3,
      "columns": {
      "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
      "idroler": { "type": "int", "nullable": false },
      "iduser": { "type": "int", "nullable": false },      
      "created_at" : {"type": "datetime", "nullable": false, "default":true}
      }
    },
    "alunos" : {
      "id": 4,
      "columns": {
        "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
        "aluno": { "type": "string", "size": 100, "nullable": false },
        "email": { "type": "string", "size": 150, "nullable": false },
        "created_at" : {"type": "datetime", "nullable": false, "default":true}
      }
    },
    "estados": {
      "id": 5,
      "columns": {
        "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
        "estado": { "type": "string", "nullable": false , "size": 80 , "decimal": 0 },
        "regiao": { "type": "string", "size": 30 ,"nullable": true },
        "uf": { "type": "string", "size": 2 ,"nullable": false },
        "created_at" : {"type": "datetime", "nullable": false, "default":true}
      }
    },
    "municipios": {
      "id": 6,
      "columns": {
        "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
        "municipio": { "type": "string", "size": 100, "nullable": false },
        "uf": { "type": "string", "size": 2, "nullable": false },
        "populacao": { "type": "int", "nullable": true },
        "created_at" : {"type": "datetime", "nullable": false, "default": true }
      }
    },
    "bairros": {
      "id": 7,
      "columns": {
        "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
        "bairro": { "type": "string", "size": 100, "nullable": false },
        "created_at" : {"type": "datetime", "nullable": false, "default": true }
      }
    },
    "logradouros": {
      "id": 8,
      "columns": {
        "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
        "logradouro": { "type": "string", "size": 100, "nullable": false },
        "created_at" : {"type": "datetime", "nullable": false, "default": true }
      }
    },
    "contatos":{
        "id": 9,
        "columns": {
            "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
            "nome": { "type": "string", "size": 100, "nullable": false },
            "telefone": { "type": "string", "size": 15 , "nullable": false },
            "celular": { "type": "string", "size": 15 , "nullable": false },
            "created_at" : {"type": "datetime", "nullable": false, "default": true }
        }
    },
    "clientes":{
        "id": 10,
        "columns": {
            "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
            "cliente": { "type": "string", "size": 100, "nullable": false },
            "telefone": { "type": "string", "size": 15 , "nullable": false },
            "email": { "type": "string", "size": 250 , "nullable": false },
            "created_at" : {"type": "datetime", "nullable": false, "default": true }
        }
    },
    "disciplinas":{
        "id": 11,     
        "columns": {
            "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
            "disciplina": { "type": "string", "size": 100, "nullable": false },
            "created_at" : {"type": "datetime", "nullable": false, "default": true }            
        }
    }
    ,
    "fornecedores":{
        "id": 12,
        "columns": {
            "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
            "fornecedor": { "type": "string", "size": 100, "nullable": false },
            "telefone": { "type": "string", "size": 15 , "nullable": false },
            "email": { "type": "string", "size": 250 , "nullable": false },
            "created_at" : {"type": "datetime", "nullable": false, "default": true }
        }
    },
    "transportadoras":{
        "id": 13,
        "columns": {
            "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
            "transportadora": {"type": "string", "size": 100, "nullable": false },
            "telefone": { "type": "string", "size": 15 , "nullable": false },
            "email": { "type": "string", "size": 250 , "nullable": false },
            "created_at" : {"type": "datetime", "nullable": false, "default": true }
        }
    }
    ,
    "produtos":{
        "id": 14,
        "columns": {
            "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
            "descricao": {"type": "string", "size": 80, "nullable": false },
            "unidade": { "type": "string", "size": 10 , "nullable": false },
            "precovenda": { "type": "number", "size": 12 , "decimal": 2, "nullable": false },
            "created_at" : {"type": "datetime", "nullable": false, "default": true }
        }
    }
    ,
    "categorias":{
        "id": 15,
        "columns": {
            "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
            "categoria": {"type": "string", "size": 30, "nullable": false },            
            "created_at" : {"type": "datetime", "nullable": false, "default": true }
        }
    }
    ,
    "produtosestoque":{
        "id": 16,
        "columns": {
            "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
            "idproduto": { "type": "int", "primaryKey": false, "nullable": false},
            "entrada": { "type": "number", "nullable": true},
            "saida": { "type": "number", "nullable": true}           
        }
    }
    ,
    "cursos":{
        "id": 17,
        "columns": {
            "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
            "curso": {"type": "string", "size": 30, "nullable": false },            
            "siglamec": {"type": "string", "size": 10, "nullable": true },            
            "created_at" : {"type": "datetime", "nullable": false, "default": true }
        }
    }
    ,
    "turnos":{
        "id": 18,
        "columns": {
            "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
            "turno": {"type": "string", "size": 30, "nullable": false },            
            "turnosigla": {"type": "string", "size": 30, "nullable": true },            
            "created_at" : {"type": "datetime", "nullable": false, "default": true }
        }
    }    
    ,
    "docentes":{
        "id": 19,
        "columns": {
            "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
            "docente": { "type": "string", "size": 100, "nullable": false },
            "telefone": { "type": "string", "size": 15 , "nullable": false },
            "email": { "type": "string", "size": 250 , "nullable": false },
            "created_at" : {"type": "datetime", "nullable": false, "default": true }
        }
    },
    "funcionarios":{
        "id": 21,
        "columns": {
            "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
            "funcionario": { "type": "string", "size": 100, "nullable": false },
            "telefone": { "type": "string", "size": 15 , "nullable": false },
            "email": { "type": "string", "size": 250 , "nullable": false },
            "salario": { "type": "number", "nullable": true},
            "created_at" : {"type": "datetime", "nullable": false, "default": true }
        }
    }
    "departamentos":{
        "id": 22,
        "columns": {
            "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
            "departamento": {"type": "string", "size": 30, "nullable": false },            
            "sigla": {"type": "string", "size": 30, "nullable": true },            
            "nrofuncionario": { "type": "number", "nullable": true},
            "created_at" : {"type": "datetime", "nullable": false, "default": true }
        }
    }    
    "funcoes":{
        "id": 23,
        "columns": {
            "id": { "type": "int", "primaryKey": true, "autoIncrement": true },
            "funcao": {"type": "string", "size": 30, "nullable": false },            
            "sigla": {"type": "string", "size": 30, "nullable": true },            
            "nrofuncionario": { "type": "number", "nullable": true},
            "created_at" : {"type": "datetime", "nullable": false, "default": true }
        }
    }    
    ,
    "":{
        "id": ?? ,
        "columns": {
            "id": { "type": "int", "primaryKey": true, "autoIncrement": true },

        }
    }

  }
}