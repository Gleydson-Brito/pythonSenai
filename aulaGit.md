# Entendendo Git

|comando|descrição|
|-|:-:|
| git init | Inicia o monitoramento do projeto |
| git branch -M + nome da nova branch| Renomeia a branch principal |
| git status | Mostra os arquivos que ainda não passaram na triagem |
| git add + nome e extensão do documento | Ele faz um checkpoint somente nesse arquivo e caso tenha algum problema, pode retornar ao ponto anterior. Manda os arquivos pra area de staging. |
|git add . | Salva todo o projeto de uma vez |
| git config --global user.name 'nome' | Salva o nome da pessoa responsável pelo projeto |
| git config --global user.email 'email' | Coloca o email de contato do responsável |
| git config --list | Mostra se o nome e email está conforme o cadastrado do projeto. Lista as configurações de gis |
| git commit -m 'primeiro commit' | cria o primeiro ponto de restauração no projeto |
| git log | Visualizar a lista de commit
| git checkout -b + nome da ramificação de branch | Cria uma ramificação ligada a ramificação principal "main" onde tem acesso a tudo que foi criado antes dessa ramificação.|
| git checkout + nome da branch | Muda da branch em uso para uma outra branch que foi selecionado. |