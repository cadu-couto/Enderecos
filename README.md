# Enderecos

Este projeto contempla os requisitos para a entrega do MVP da Sprint III: Arquitetura de Software do curso de Pós Graduação em Engenharia de Software da PUC RIO.



Componente A - Frontend >> FrontAddress: Que permite o acesso as APIs de Endereço e Consulta CEP.

Componente B - Serviço >> Consulta Cep: Que permite o consulta do Endereço via CEP, utilizando o serviço público disponibilizado pela Via CEP.

Componente C - Serviço >> Endereço: Que permite a criação, edição, exclussão de uma endereço vinculado a uma cliente. E, ainda, disponibiliza a consulta da distância entre o endereço do cliente e os serviços de assintência técbica.


Executando com Docker
Você pode executar o projeto em um contêiner Docker. Certifique-se de ter o Docker instalado no seu sistema.


Clone o repositório para o seu computador :

git clone https://github.com/seu-usuario/nome-do-repositorio.git

Navegue até o diretório do projeto:

cd nome-do-repositorio

Construa a imagem Docker :

docker build -t nome_da_imagem .

Execute o contêiner Docker:

docker run -p 8080:5000 nome_da_imagem

O aplicativo estará acessível no seu navegador em http://localhost:8080.


