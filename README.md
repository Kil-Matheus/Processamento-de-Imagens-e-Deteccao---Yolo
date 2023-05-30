<table>

<tr>

</td>

  

<td><a  href= "https://www.inteli.edu.br/"><img  src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png"  alt="Inteli - Instituto de Tecnologia e Liderança"  border="0"  width="80%"></a>

</td>

</tr>

</table>

  

<font  size="20"><center>

Processamento de imagens e detecção de objetos

</center></font>

  

# **Sumário**

  

- [Autores](#autores)


- [Visão Geral do Projeto](#visão-geral-do-projeto)


- [Objetivos](#objetivos)
  

- [Instalação de Ambiente](#instalação-de-ambiente)


- [Desenvolvimento](#desenvolvimento)
  

- [Conclusão](#conclusão)

  
- [Referências](#referências)

  

# Autores

  

Kil Matheus Gomes Teixeira

  

# Visão Geral do Projeto

## Proposta

A fim de proporcionar aprendizado prático aos alunos do 2º ano do curso de Engenharia da Computação, o Instituto de Liderança e Tecnologia - INTELI, juntamente com o professor de programação Rodrigo Mangoni Nicola, propôs uma atividade desafiadora que busca aplicar os conhecimentos adquiridos sobre ambiente ROS2 (Ambiente de Programação de Desenvolvimento de Sistemas Robóticos) e Ubuntu.

# Objetivos

Desenvolva um script em Python capaz de identificar rachaduras em paredes de concreto. Utilize o [dataset](https://universe.roboflow.com/university-bswxt/crack-bphdr/dataset/2) desenvolvido pela Roboflow. Para o desenvolvimento dessa atividade, recomenda-se o uso de um modelo de detecção de objetos pré-treinado, como o [YoLo](https://github.com/ultralytics/ultralytics). É possível ver um exemplo de como desenvolver um script similar [nesse vídeo](https://www.youtube.com/watch?v=vFGxM2KLs10).

## Requisitos

Segundo o card do AdaLove do prof. Rodrigo Mangoni Nicola, os requisitos são descritos como seguintes:

Padrão de Qualidade:

Para esta atividade, espera-se a capacidade demonstrável de interagir com imagens utilizando os conceitos de visão computacional e modelos preditivos pré-treinados. A entrega deve ser um vídeo demonstrando o funcionamento do projeto, um texto conciso descrevendo como foi feita a implementação e o link para o repositório público no github onde foi feita a implementação. O código fonte pode ser tanto em formato de de script em Python (`.py`) como em formato de notebook Jupyter (`.ipynb`). A nota se divide em:

1.  Setup do modelo pré-treinado utilizado; (peso 2)
2.  Retreinamento do modelo para o conjunto de dados disponibilizado; (peso 3)
3.  Explicação coerente e concisa da implementação (min 250 caracteres e máximo 1500); (peso 3)
4.  Congruência entre o que foi escrito e o código disposto no repositório do github; (peso 2)

## Instalação de Ambiente

### Yolo V8

YOLO é uma abreviação para "You Only Look Once" ("Você Só Olha uma Vez", em tradução livre). É um dos algoritmos mais populares e eficientes para detecção de objetos em imagens e vídeos em tempo real.

O YOLO utiliza uma rede neural convolucional para realizar a detecção de objetos em tempo real. Essa rede é treinada em um grande conjunto de dados rotulados, onde as imagens são anotadas com caixas delimitadoras e classes correspondentes. Durante a inferência, o YOLO processa a imagem inteira de uma só vez e retorna as previsões das caixas delimitadoras e suas classes associadas.

### OpenCV

O OpenCV (Open Source Computer Vision) é uma biblioteca de código aberto. O objetivo principal do OpenCV é fornecer um conjunto de funções e algoritmos que facilitem a implementação de aplicações de visão computacional, como detecção de objetos, reconhecimento facial, calibração de câmera, rastreamento de movimento, entre outros.

### Colab

O Google Colab é uma plataforma baseada em nuvem desenvolvida pelo Google que permite escrever, executar e colaborar em código Python diretamente no navegador, sem a necessidade de configurar um ambiente de desenvolvimento local. Ele é amplamente utilizado para desenvolvimento de projetos de ciência de dados, aprendizado de máquina, pesquisa e ensino.

## Desenvolvimento

Para podermos atingir o nosso objetivo de conseguir identificar rachaduras utilizando uma Inteligência Artificial, primeiramente precisamos utilizar um Dataset, que um arquivo de referência para a Rede Neural conseguir identificar as fixuras. 
No exercício, ele nos indica utilizar o site Roboflow, que é uma plataforma que contém diversos Datasets prontos para download.

Para a nossa aplicação, o professor de programação nos indicou a seguir esses vídeos como tutorial para o download e utilização desses datasets utilizando o Colab, sendo o link anexado logo abaixo:

Link do Tutorial:
https://www.youtube.com/watch?v=vFGxM2KLs10

Link do Dataset:
https://universe.roboflow.com/university-bswxt/crack-bphdr/dataset/2

*Nota: O resultado final da nossa aplicação é diferente da mostrada no tutorial, mas ela gera o mesmo resultado final. A parte que utilizamos no tutorial é principalmente a exportação do  dataset.

Após entendermos como é feita a exportação do dataset para o Colab, já que o código abaixo vai requisitar uma 'Api Key' , agora vamos utilizar essas informações para treinar a nossa Inteligência Artificial.

<center>
<img  src="img\colab_training.png"  alt="Treinamento no Colab"  />
</center>

**<font  size=2> Estrutura um Python utilizada no Colab para exportar o dataset do Roboflow e fazer treinar a IA </font>**

Após isso, ela vai gera um documento chamado 'best.pt' como indicado na imagem o caminho do arquivo para download.

<center>
<img  src="img\last_training.png"  alt="Caminho do Documento"  />
</center>

**<font  size=2> Local do Arquivo 'best.pt' </font>**

Com o arquivo já treinado, agora vamos para o nosso ambiente em Python local (VSCode). No mesmo diretório, vamos colocar o nosso arquivo 'best.pt' e o código Python com o seguinte conteúdo.

<center>
<img  src="img\local_python.png"  alt="Código Local"  />
</center>

**<font  size=2> Código rodando Localmente</font>**

O resultado final é o seguinte, quando a câmera detecta alguma fixura, ela indica visualmente contornando o objeto.

<center>
<img  src="img\result.png"  alt="Resultado Final"  />
</center>

**<font  size=2> Resultado do código funcionado</font>**

Vídeo de funcionamento se encontra no Github, na pasta './media' ou nesse link:
https://drive.google.com/file/d/1LpTBWuos-8VHA16Mfy89EmOG-KlGkDCX/view?usp=sharing


## Conclusão

Podemos concluir que nessa atividade, o objetivo de nos mostrar que as ferramentas de inteligência artificial alinhadas com as de processamento de imagens, podem trazer um grande benefício para a sociedade. No exemplo da nossa solução, esse conjunto pode ser utilizado para detectar rachaduras em tubulações, indicando algum tipo de vazamento ou até  mesmo o comprometimento da estrutura interna, antes mesmo de um ser humano ter que ir até o local averiguar a situação, gerando mais segurança e integridade dos colaboradores.

## Referências

TEIXEIRA. Kil Matheus Gomes. Robô Digital. Repositório Github. Disponível em: [https://github.com/Kil-Matheus/Processamento-de-Imagens-e-Deteccao---Yolo](https://github.com/Kil-Matheus/Turtlesim---Desenhando-com-Caminho.git). Acesso em: 29 mai. 2023.

NICOLA,  Rodrigo Mangoni (2023). Ponderada 3 - # Processamento de imagens e detecção de objetos . Instituto de Tecnologia e Liderança - INTELI. Disponível em: https://github.com/Murilo-ZC/Questoes-Trabalhos-Inteli-M6/tree/main/ponderada3. Acesso em: 24 abril 2023. 

# Agradecimentos

Agradecimentos especiais a:

 Rodrigo Mangoni Nicola pelo seu grande conhecimento em programação que sempre nos ajuda em todos os desenvolvimentos.