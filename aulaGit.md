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
| git checkout | Mostra a lista de branch que existe no projeto |
| git merge + nome da branch | serve para mesclar uma branch segundária com a principal. A branch principal nesse caso é a "main" e a secundária é a "github". |
| git branch -d + nome da branch | Serve para deletar uma branch que já está finalizada e mesclada com a principal. |
| python3 -m venv venv | Comando para criar uma ambiente virtual do python. Serve para quando tiver várias pessoas fazendo um trabalho em equipe, para ca dada um tenha sua versão na qual está acostumado a trabalhar. O segundo nome venv é o nome da pasta. |
