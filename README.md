# analise-lexica-code-start
Este repositório contém o código inicial de referência para o desenvolvimento da fase de Análise Léxica do Projeto do Compilador para a linguagem TPP.

# Análise Léxica

A __Análise Léxica__ é a fase do compilador que lê o código-fonte do arquivo de entrada como um fluxo de caracteres, e nesse processo de varredura reconhece os _tokens_ ou marcas da linguagem. As denominações Sistema de Varredura, Analisador Léxico e _Scanner_ são equivalentes.

Devem ser reconhecidas as marcas presentes na linguagem `TPP`, como `se`, `então`, `repita`, `até` que são palavras chave, palavras reservadas. Precisam ser reconhecidos os nomes de variáveis e funções que são os _identificadores_, símbolos e operadores aritméticos, lógicos e relacionais.

O processo de reconhecimento das marcas, a identificação de padrões pode ser feito de duas formas: utilizando-se __expressões regulares__ ou implementando o analisador com a teoria de __autômatos finitos__.

Neste projeto serão utilizadas _expressões regulares_ na __especificação léxica__, os padrões de reconhecimentos das marcas.

Para um código simples em `TPP` igual o Código 1.

```c
{ Programa simples. }

inteiro principal()
  retorna(0)
fim
```
_Código 1: Programa em C-_


A lista de marcas que precisam ser identificadas é:
```
INTEIRO
ID
ABRE_PARENTESE
FECHA_PARENTESE
RETORNA
ABRE_PARENTESE
NUM_INTEIRO
FECHA_PARENTESE
FIM
```

## Preparação do Ambiente

Para a implementação da fase de __Análise Léxica__ é necessário instalar ferramentas, como o `PLY`. Os pré-requisitos podem ser instalados utilizando o arquivo de `requirements.txt`.

```bash
$ pip install  -r requirements.txt
```

```bash
$ cat requirements.txt
pytest
ply
configparser
logging
```

## Execução de Testes

No projeto está sendo disponibilizado arquivos de exemplos em `TPP` para testes. Os testes estão no diretório `tests` do raiz do projeto.

Para executar um teste em específico a implementação do analisador léxico pode ser chamada, o parâmetro `-k` pode ser utilizado para que somente _chaves de erros_ sejam impressas.

```bash
$ python tpplex.py tests/teste-006.tpp -k
INTEIRO
ID
ABRE_PARENTESE
FECHA_PARENTESE
RETORNA
ABRE_PARENTESE
NUM_INTEIRO
FECHA_PARENTESE
FIM
```

Todos os testes podem ser executados via `pytest`.

```bash
[rogerio@ryzen-nitro analise-lexica-code-start]$ pytest -v
==================================================== test session starts =====================================================
platform linux -- Python 3.12.6, pytest-8.3.3, pluggy-1.5.0 -- /usr/bin/python
cachedir: .pytest_cache
rootdir: /run/media/rogerio/BK-RAG-HP1TB/repositorios/Dropbox/dados/rogerio/projetos/projetos.github/analise-lexica-code-start
plugins: typeguard-4.3.0
collected 37 items                                                                                                           

tpplex_test.py::test_001 PASSED                                                            [  2%]
tpplex_test.py::test_002 PASSED                                                            [  5%]
tpplex_test.py::test_003 PASSED                                                            [  8%]
tpplex_test.py::test_004 PASSED                                                            [ 10%]
tpplex_test.py::test_005 PASSED                                                            [ 13%]
tpplex_test.py::test_006 PASSED                                                            [ 16%]
tpplex_test.py::test_007 PASSED                                                            [ 18%]
tpplex_test.py::test_008 PASSED                                                            [ 21%]
tpplex_test.py::test_009 PASSED                                                            [ 24%]
tpplex_test.py::test_010 PASSED                                                            [ 27%]
tpplex_test.py::test_011 PASSED                                                            [ 29%]
tpplex_test.py::test_012 PASSED                                                            [ 32%]
tpplex_test.py::test_013 PASSED                                                            [ 35%]
tpplex_test.py::test_014 PASSED                                                            [ 37%]
tpplex_test.py::test_015 PASSED                                                            [ 40%]
tpplex_test.py::test_016 PASSED                                                            [ 43%]
tpplex_test.py::test_017 PASSED                                                            [ 45%]
tpplex_test.py::test_018 PASSED                                                            [ 48%]
tpplex_test.py::test_019 PASSED                                                            [ 51%]
tpplex_test.py::test_020 PASSED                                                            [ 54%]
tpplex_test.py::test_021 PASSED                                                            [ 56%]
tpplex_test.py::test_022 PASSED                                                            [ 59%]
tpplex_test.py::test_023 PASSED                                                            [ 62%]
tpplex_test.py::test_024 PASSED                                                            [ 64%]
tpplex_test.py::test_025 PASSED                                                            [ 67%]
tpplex_test.py::test_026 PASSED                                                            [ 70%]
tpplex_test.py::test_027 PASSED                                                            [ 72%]
tpplex_test.py::test_028 PASSED                                                            [ 75%]
tpplex_test.py::test_029 PASSED                                                            [ 78%]
tpplex_test.py::test_030 PASSED                                                            [ 81%]
tpplex_test.py::test_031 PASSED                                                            [ 83%]
tpplex_test.py::test_032 PASSED                                                            [ 86%]
tpplex_test.py::test_033 PASSED                                                            [ 89%]
tpplex_test.py::test_034 PASSED                                                            [ 91%]
tpplex_test.py::test_035 PASSED                                                            [ 94%]
tpplex_test.py::test_036 PASSED                                                            [ 97%]
tpplex_test.py::test_037 PASSED                                                            [100%]

======================================= 37 passed in 1.74s =======================================
$
```

## Leitura Recomendada

1. __Capítulo 2:__ _Varredura_

    LOUDEN, Kenneth C. Compiladores: princípios e práticas. São Paulo, SP: Thomson, c2004. xiv, 569 p. ISBN 8522104220.

2. __Capítulo 3:__ _Análise Léxica_

    AHO, Alfred V. et al. Compiladores: princípios, técnicas e ferramentas. 2. ed. São Paulo, SP: Pearson Addison-Wesley, 2008. x, 634 p. ISBN 9788588639249.