# SWCAR
### Sistema Web de Controle de Atividades e Recompensas
Um projeto apresentado como parte integrante a disicplina GCC188 - Engenharia de software ofertada pelo Departamento de Ciência da Computação localizado na Universidade Federal de Lavras.

## Estrutura do Projeto

A estrutura do projeto se apresenta como a seguinte:

```
documentos/
  requesitos/
src/
  manage.py
  swcar/
    __init__.py
    settings.py
    urls.py
    wsgi.py
public/
      index.html
      pages/ 
```
Essas pastas representam:
* Pasta **src** onde serão inseridos arquivos integrantes do back-end.
  * Subpasta **swcar** de arquivos criados pelo framework Django na inicialização do projeto.
  
* Pasta **public** onde são armazenadoas as arquivos de interface gráfica disponível ao usuário.
  * Subpasta **pages**, onde são colocadas as páginas html, com exceção da primeira, e arquivos css e javascript. Index é a primeira página presentada pelo sistema.
  
* Pasta **documentos** onde ficarão armaze nados documentos criados durante a iteração do desenvolvimento de software.
  * Subpasta **requesitos**, onde é organizados os arquivos referente aos requesitos levantados do projeto.
   
