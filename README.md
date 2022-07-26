# Sistema de Academia Web
Projeto de um sistema gerenciador de academias Web, desenvolvido em Python (Flask), HTML5, CSS, JavaScript e MySQL.

No sistema é possível cadastrar usuários, treinadores, planos e gerenciar matrículas; o usuário é capaz de se autenticar na plataforma e se comunicar com os treinadores, através de mensagens instântaneas e visualizar seus treinos, assim como se manter atualizado acerca de seu progresso.

## Execução
Para iniciar o banco de dados local, execute:
```
python3 init_db.py
```

Para executar o programa, utilize:
```
pip install requirements.txt
export FLASK_APP=app
flask run
```

As rotas e endereços do programa se encontram no arquivo app.py