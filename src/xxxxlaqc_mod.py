# -*- coding: utf-8 -*-
"""
UNIFEI - Universidade Federal de Itajuba.

LaQC - Laboratorio de Quimica Computacional

Permite modificações em lote dos arquivos de input do Gaussian

Autor............: Rogério Ribeiro Macêdo
Criado em........: 17 de dezembro de 2022
Última alteração.: 01 de setembro de 2023

Versão 0.3

Observações:

    1) type_section: indica a seção do arquivo de entrada (input) que está sendo lida:
        - https://gaussian.com/input/#:~:text=The%20basic%20structure%20of%
        20a,options%20(blank%20line%20terminated)
"""
# pylint: disable=import-error
import sys
import platform
from pathlib import Path


TAM_TEXTO = 45


def existe(arquivo, tipo="arquivo"):
    """
    Verifica se o arquivo/diretorio passado como parâmetro existe.

    Parameters
    ----------
    arquivo : texto
        Nome do arquivo/diretorio a ser verificado.
    tipo : texto
        Indicador se será validado um diretório ou um arquivo.

    Returns
    -------
    Bool
        True, se o arquivo/diretorio existe; False, se o arquivo/diretorio não existe.

    """
    path = Path(arquivo)
    if tipo == "arquivo":
        resultado = (path.exists() and path.is_file())
    else:
        resultado = path.exists()

    return resultado


def head_msg():
    """
    Mensagem de cabeçalho.

    Returns
    -------
    None.

    """
    print()
    print("-".center(80, "-"))
    print(f'{"|":<1} {"UNIFEI - Universidade Federal de Itajubá":^76} '
          f'{"|":>1}')
    print(f'{"|":<1} {"LaQC - Laboratório de Química Computacional":^76} '
          f'{"|":>1}')
    print("-".center(80, "-"))
    print(f'{"|":<1} {" ":^76} {"|":>1}')
    print(f'{"|":<1} {"obs 1: digite [sair] para encerrar o programa ":<76} '
          f'{"|":>1}')
    print(f'{"|":<1} {" ":^76} {"|":>1}')
    print(f'{"|":<1} {"obs 2: não informar valor considera que o parâmetro não será modificado.":<76} '
          f'{"|":>1}')
    print(f'{"|":<1} {" ":^76} {"|":>1}')
    print("-".center(80, "-"))
    print(f'{"|":<1} {"Modificação em lote dos arquivo de input do Gaussian":^76} '
          f'{"|":>1}')
    print("-".center(80, "-"))
    print()


def tchau():
    """
    Saindo e dizendo Tchau!.

    Returns
    -------
    None.

    """
    print("")
    print("-".center(80, "-"))
    print(f'{"|":<1} {"UNIFEI - Universidade Federal de Itajubá":^76} '
          f'{"|":>1}')
    print(f'{"|":<1} {"LaQC - Laboratório de Química Computacional":^76} '
          f'{"|":>1}')
    print(f'{"|":<1} {" ":^76} {"|":>1}')
    print(f'{"|":<1} {"Tchau!!!!":^76} '
          f'{"|":>1}')
    print(f'{"|":<1} {" ":^76} {"|":>1}')
    print("-".center(80, "-"))
    print("")
    sys.exit()


def usar_arq_conf():
    """
    Questiona o usuário se irá usar, ou não, arquivo de configuração para realizar alterações.

    Returns
    -------
    Boolean
        True, usará arquivo de configuração.
        False, não usará arquivo, portanto, o script irá questionar o usuário.

    """
    val = input("Usar arquivo de configuração? [N]".ljust(TAM_TEXTO, ".") + ": ").strip()
    if val.upper() == "SAIR":
        tchau()
    else:
        if val == "":
            val = "N"
        else:
            if val not in ["S", "s", "N", "n"]:
                print(f" + Valor ({val}), inválido . Saindo!")
                sys.exit()

    return (val in ["S", "s"])


def ler_arq_conf(configuracoes):
    """
    Leitura do arquivo de configuração.

    Returns
    -------
    alterar : dict
        Dicionário contendo os valores que serão modificados.

    """
    arquivo_conf = input("Local/nome do arquivo de configuração".ljust(TAM_TEXTO, ".")
                         + ": ").strip()
    if arquivo_conf != "":
        if arquivo_conf.upper() == "SAIR":
            tchau()
        else:
            if existe(arquivo_conf):
                with open(arquivo_conf, "r") as f_arquivo_conf:
                    for line in f_arquivo_conf:
                        # Se o primeiro caracter é ';' quer dizer que é um comentário
                        if (line[0] != ";") and (len(line.strip()) > 0):
                            variavel, valor = line.split(sep=":=")
                            configuracoes[variavel.strip()] = valor.strip()

                    # fechando arquivo
                    f_arquivo_conf.close()
            else:
                print(f" + Arquivo ({arquivo_conf}) não encontrado!. Saindo!")
                sys.exit()
    else:
        print(" + Local/nome não informado. Saindo!")
        sys.exit()

    return configuracoes


def origem(configuracoes):
    """
    Questão sobre a origem dos arquivos a serem alterados.

    Parameters
    ----------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    Returns
    -------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    """
    questao_ok = False
    while not questao_ok:
        origem_arq = input("Local de origem dos arquivos".ljust(TAM_TEXTO, ".") + ": ").strip()
        if origem_arq.upper() == "SAIR":
            tchau()
        else:
            if not existe(origem_arq, "diretorio") or origem_arq == "":
                print(" + Local informado não existe ou em branco!")
            else:
                configuracoes['origem'] = origem_arq
                questao_ok = True

    return configuracoes


def destino(configuracoes):
    """
    Questão sobre o destino dos arquivos depois de alterados.

    Parameters
    ----------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    Returns
    -------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    """
    questao_ok = False
    while not questao_ok:
        destino_arq = input("Local de destino dos arquivos".ljust(TAM_TEXTO, ".") + ": ").strip()
        if destino_arq.upper() == "SAIR":
            tchau()
        else:
            if not existe(destino_arq, "diretorio") or destino_arq == "":
                print(" + Local informado não existe ou em branco!")
            else:
                configuracoes['destino'] = destino_arq
                questao_ok = True

    return configuracoes


def parametros(configuracoes):
    """
    Questão sobre os parâmetros de cálculo.

    Parameters
    ----------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    Returns
    -------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    """
    questao_ok = False
    while not questao_ok:
        vlr_parametros = input("Parâmetros de cálculo".ljust(TAM_TEXTO, ".") + ": ").strip()
        if vlr_parametros.upper() == "SAIR":
            tchau()
        else:
            if vlr_parametros != "":
                if vlr_parametros[0] != "#":
                    vlr_parametros[0] = "#"
                configuracoes['parametros'] = vlr_parametros
                questao_ok = True
            else:
                questao_ok = True

    return configuracoes


def nprocshared(configuracoes):
    """
    Questão sobre o número de processadores a serem usados no cálculo.

    Parameters
    ----------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    Returns
    -------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    """
    questao_ok = False
    while not questao_ok:
        vlr_processadores = input("Número de processadores".ljust(TAM_TEXTO, ".") + ": ").strip()
        if vlr_processadores.upper() == "SAIR":
            tchau()
        else:
            try:
                if vlr_processadores != "":
                    # conversão apenas para efeito de validação do dado
                    int(vlr_processadores)
                    configuracoes['nprocshared'] = vlr_processadores
                    questao_ok = True
                else:
                    questao_ok = True
            except ValueError:
                print(f" + Valor informado ({vlr_processadores}), não é um número inteiro.")

    return configuracoes


def memoria(configuracoes):
    """
    Questão sobre a quantidade de memória usada no cálculo.

    Parameters
    ----------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    Returns
    -------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    """
    questao_ok = False
    while not questao_ok:
        vlr_memoria = input("Quantidade de memória".ljust(TAM_TEXTO, ".") + ": ").strip()
        if vlr_memoria.upper() == "SAIR":
            tchau()
        else:
            if vlr_memoria == "":
                questao_ok = True
            else:
                configuracoes['memoria'] = vlr_memoria
                questao_ok = True

    return configuracoes


def rwf_arquivo(configuracoes):
    """
    Questão sobre o arquivo rwf e seu tamanho.

    Parameters
    ----------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    Returns
    -------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    """
    questao_ok = False
    while not questao_ok:
        vlr_rwf = input("RWF".ljust(TAM_TEXTO, ".") + ": ").strip()
        if vlr_rwf.upper() == "SAIR":
            tchau()
        else:
            if vlr_rwf == "":
                questao_ok = True
            else:
                configuracoes['rwf'] = vlr_rwf
                questao_ok = True

    return configuracoes


def layers_camadas(configuracoes):
    """
    Identificacao das camadas ONION.

    Parameters
    ----------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    Returns
    -------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    """
    vlr_simbolo = input(" - Identificar as camadas? [S]".ljust(TAM_TEXTO, ".") + ": ").strip()
    if vlr_simbolo.upper == "SAIR":
        tchau()
    else:
        if vlr_simbolo == "":
            configuracoes['layers_simbolo'] = str(True)
        else:
            configuracoes['layers_simbolo'] = str(vlr_simbolo in ["S", "s"])

    vlr_layer_high = input(" - Linhas para 'layer high'? [0-0]".ljust(TAM_TEXTO, ".")
                           + ": ").strip()
    if vlr_simbolo.upper == "SAIR":
        tchau()
    else:
        if vlr_layer_high == "":
            configuracoes['layer_high'] = '0-0'
        else:
            configuracoes['layer_high'] = vlr_layer_high

    vlr_layer_middle = input(" - Linhas para 'layer middle'? [0-0]".ljust(TAM_TEXTO, ".")
                             + ": ").strip()
    if vlr_simbolo.upper == "SAIR":
        tchau()
    else:
        if vlr_layer_middle == "":
            configuracoes['layer_middle'] = '0-0'
        else:
            configuracoes['layer_middle'] = vlr_layer_middle

    vlr_layer_low = input(" - Linhas para 'layer low'? [0-0]".ljust(TAM_TEXTO, ".") + ": ").strip()
    if vlr_simbolo.upper == "SAIR":
        tchau()
    else:
        if vlr_layer_low == "":
            configuracoes['layer_low'] = '0-0'
        else:
            configuracoes['layer_low'] = vlr_layer_low

    return configuracoes


def layers(configuracoes):
    """
    Questão sobre camadas.

    Parameters
    ----------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    Returns
    -------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    """
    questao_ok = False
    while not questao_ok:
        vlr_layers = input("Uso de camadas para cálculo ONION? [N]".ljust(TAM_TEXTO, ".")
                           + ": ").strip()
        if vlr_layers.upper() == "SAIR":
            tchau()
        else:
            if vlr_layers == "":
                questao_ok = True
            else:
                if vlr_layers not in ["S", "s", "N", "n"]:
                    print(f"Valor informado ({vlr_layers}), inválido!")
                else:
                    configuracoes['layers'] = str((vlr_layers in ["S", "s"]))
                    questao_ok = True

    if vlr_layers in ["S", "s"]:
        configuracoes = layers_camadas(configuracoes)

    return configuracoes


def freeze_camadas(configuracoes):
    """
    Identificacao das camadas Freeze.

    Parameters
    ----------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    Returns
    -------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    """
    vlr_freeze_high = input(" - Valor 'freeze layer high'? [0]".ljust(TAM_TEXTO, ".")
                            + ": ").strip()
    if vlr_freeze_high.upper == "SAIR":
        tchau()
    else:
        if vlr_freeze_high == "":
            configuracoes['value_layer_high'] = 0
        else:
            configuracoes['value_layer_high'] = vlr_freeze_high

    vlr_freeze_middle = input(" - Valor 'freeze layer middle'? [0]".ljust(TAM_TEXTO, ".")
                              + ": ").strip()
    if vlr_freeze_middle.upper == "SAIR":
        tchau()
    else:
        if vlr_freeze_middle == "":
            configuracoes['value_layer_middle'] = 0
        else:
            configuracoes['value_layer_middle'] = vlr_freeze_middle

    vlr_freeze_low = input(" - Valor 'freeze layer low'? [0]".ljust(TAM_TEXTO, ".") + ": ").strip()
    if vlr_freeze_low.upper == "SAIR":
        tchau()
    else:
        if vlr_freeze_low == "":
            configuracoes['value_layer_low'] = 0
        else:
            configuracoes['value_layer_low'] = vlr_freeze_low

    return configuracoes


def freeze(configuracoes):
    """
    Questão sobre camadas freeze.

    Parameters
    ----------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    Returns
    -------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    """
    questao_ok = False
    while not questao_ok:
        vlr_freeze = input("Congelar átomos ('freeze')? [N]".ljust(TAM_TEXTO, ".") + ": ").strip()
        if vlr_freeze.upper() == "SAIR":
            tchau()
        else:
            if vlr_freeze == "":
                questao_ok = True
            else:
                if vlr_freeze not in ["S", "s", "N", "n"]:
                    print(f"Valor informado ({vlr_freeze}), inválido!")
                else:
                    configuracoes['freeze'] = str(vlr_freeze in ["S", "s"])
                    questao_ok = True

    if vlr_freeze in ["S", "s"]:
        configuracoes = freeze_camadas(configuracoes)

    return configuracoes


def script_executar(configuracoes):
    """
    Questão sobre criar ou não script de execução de cálculo.

    Parameters
    ----------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    Returns
    -------
    configuracoes : dict
        Dicionário contendo os valores que serão alterados.

    """
    questao_ok = False
    while not questao_ok:
        vlr_criar_script = input("Criar script de execução? [S]".ljust(TAM_TEXTO, ".")
                                 + ": ").strip()
        if vlr_criar_script.upper() == "SAIR":
            tchau()
        else:
            if vlr_criar_script == "":
                configuracoes['criar_script_execucao'] = "True"
                questao_ok = True
            else:
                if vlr_criar_script not in ["S", "s", "N", "n"]:
                    print(f"Valor informado ({vlr_criar_script}), inválido!")
                else:
                    configuracoes['criar_script_execucao'] = str((vlr_criar_script in ["S", "s"]))
                    questao_ok = True

    return configuracoes


def questionar(configuracoes):
    """
    Questiona o usuário sobre quais alterações irá realizar.

    Returns
    -------
    alterar : dict
        Dicionário contendo os valores que serão modificados.

    """
    # Local de origem dos arquivos
    configuracoes = origem(configuracoes)

    # Destino onde os arquivos serão salvos
    configuracoes = destino(configuracoes)

    # Parâmetros de cálculo
    configuracoes = parametros(configuracoes)

    # Número de processadores
    configuracoes = nprocshared(configuracoes)

    # Memoria
    configuracoes = memoria(configuracoes)

    # RWF
    configuracoes = rwf_arquivo(configuracoes)

    # Layers
    configuracoes = layers(configuracoes)

    # Freeze
    configuracoes = freeze(configuracoes)

    # Criar script de execução
    configuracoes = script_executar(configuracoes)

    return configuracoes


def listar_arquivos(local, tipo=".log"):
    """
    Lista dos arquivos .log/.com no diretorio especificado.

    Returns
    -------
    list_files : array
        Lista com o nome de todos os arquivos encontrados.

    """
    lista_dos_arquivos = []

    path = Path(local)

    # Lista todos os arquivos com a extenção informada
    lista_dos_arquivos = [arquivo.name for arquivo in path.iterdir()
                          if arquivo.is_file() if arquivo.suffix == tipo]

    return lista_dos_arquivos


def get_separador():
    """
    Captura o separador de caminho de acordo com o sistema operacional.

    Returns
    -------
    separador : string
        Caracter separador.

    """
    separador = "/"
    sistema_operacional = platform.system()
    if sistema_operacional == 'Linux':
        separador = "/"
    else:
        separador = "\\"

    return separador


def get_parametros(configuracoes, parametro):
    """
    Pega o valor do parametro setado pelo arquivo de configuracao.

    Parameters
    ----------
    configuracoes : dict
        Dicionário que armazena os parametros setados no arquivo
        de configuracao ou informados pelo usuário.
    parametro : text
        O parâmetro a ser retornado.

    Returns
    -------
    Text
        Valor do parâmetro. Caso não encontre o parâmetro retorna um valor em branco.

    """
    if parametro in configuracoes:
        retorno = configuracoes[parametro]
    else:
        retorno = ""

    return retorno


def valida_camadas(camada):
    """
    Realiza apenas uma conversão de tipo em relação ao que é lido no arquivo de input.

    Parameters
    ----------
    camada : text
        Valor lido pelo parâmetro camada do arquivo de input

    Returns
    -------
    vetor_camada : vetor
        Vetor contendo valores inteiros referentes às linhas que devem ser consideradas como camada.

    """
    vetor_camada = []

    if len(camada) == 1:
        # implica em dizer que o usuário não definiu valores para a camada
        # em questão
        vetor_camada = [0, 0]
    else:
        try:
            vetor_camada = camada.split("-")
            vetor_camada = [int(vetor_camada[0]), int(vetor_camada[1])]
        except ValueError:
            vetor_camada = [0, 0]

    return vetor_camada


def get_freeze(configuracao, parametro):
    """
    Captura os valores a serem usandos nas camadas.

    Parameters
    ----------
    configuracao : dict
        dicionário de parametros.
    parametro : text
        Parâmetros que está sendo tratado (layer_high, layer_middle ou layer_low).

    Returns
    -------
    value_freeze : int
        Valor a ser usado como freeze.

    """
    try:
        if get_parametros(configuracao, "freeze") == "True":
            if parametro == "layer_high":
                if get_parametros(configuracao, "value_layer_high") != "":
                    value_freeze = int(get_parametros(configuracao, "value_layer_high"))
                else:
                    value_freeze = 0
            else:
                if parametro == "layer_middle":
                    if get_parametros(configuracao, "value_layer_middle") != "":
                        value_freeze = int(get_parametros(configuracao, "value_layer_middle"))
                    else:
                        value_freeze = -1
                else:
                    if parametro == "layer_low":
                        if get_parametros(configuracao, "value_layer_low") != "":
                            value_freeze = int(get_parametros(configuracao, "value_layer_low"))
                        else:
                            value_freeze = -1
                    else:
                        value_freeze = ""
        else:
            value_freeze = ""
    except ValueError:
        value_freeze = ""

    return value_freeze


def criar_script_execucao(configuracoes):
    """
    Cria um arquivo .sh contendo linhas para execução da simulação dos arquivos.

    Parameters
    ----------
    configuracoes : dict
        Dicionário contendo os parâmetros informados no arquivo de input.

    Returns
    -------
    bool
        'True' se o arquivo for criado com sucesso, 'False' caso contrário.

    """
    destino = get_parametros(configuracoes, "destino")

    try:
        if len(destino) > 0:
            # Lista de arquivos
            lista_arquivos = listar_arquivos(destino, '.com')
            if len(lista_arquivos) > 0:
                # creating script
                if destino[-1] != get_separador():
                    destino = destino + get_separador() + 'executar_script.sh'
                else:
                    destino = destino + 'executar_script.sh'

                arquivo_destino = open(destino, "w")

                arquivo_destino.write("#!/bin/bash" + "\n")
                arquivo_destino.write("\n")

                for linha in lista_arquivos:
                    arquivo_destino.write("g09 " + linha + "\n")

                # Fechando arquivo de destino
                arquivo_destino.close()

                retorno = True
            else:
                retorno = False
        else:
            print(" x Parâmetro 'destino' nulo ou com valor vazio")
            retorno = False

        return retorno
    except Exception as ex:
        print(f" x Erro {ex.error}".format(ex.error))
        return False


def main(configuracoes):
    """
    Função principal.

    Returns
    -------
    None.

    """
    print("")
    print("Processando arquivos...")

    # Lista de arquivos a serem alterados (*.com)
    origem = configuracoes['origem']
    destino = configuracoes['destino']

    lista_arq_input = listar_arquivos(origem, '.com')
    if len(lista_arq_input) > 0:
        for arq_input in lista_arq_input:
            print(f" - Modificando arquivo: {arq_input}")

            # local_input: arquivo de origem
            if origem[-1] != get_separador():
                local_input = origem + get_separador() + arq_input

            # Criando arquivo de destino
            if destino[-1] != get_separador():
                nome_destino = destino + get_separador() + arq_input
            arq_destino = open(nome_destino, "w")

            # seções do arquivo de input do gaussiam:
            type_sections = ["link_route", "title", "molecule"]
            pos_section = 0

            # multiplicidade = False implica em dizer que a linha ainda não foi modificada
            # isso depende se a mesma foi definida no arquivo de configuracao
            multiplicidade = False

            # contador de linhas
            linha = 0
            with open(local_input, "r") as f_input:
                for line in f_input:
                    linha += 1

                    if len(line.strip()) == 0:
                        # Linha em branco encontrada, mudança de seção
                        arq_destino.write(line)
                        pos_section += 1
                        if pos_section > 2:
                            # Chegou ao final do arquivo
                            break
                    else:
                        if type_sections[pos_section] == "link_route":
                            if line.startswith("%"):
                                if line.startswith("%chk"):
                                    # checkpoint
                                    arq_destino.write("%chk=" + nome_destino.replace(".com", ".chk") + "\n")
                                else:
                                    if line.startswith('%mem='):
                                        if len(get_parametros(configuracoes, "memoria")) > 0:
                                            arq_destino.write('%mem=' + get_parametros(configuracoes, "memoria") + '\n')
                                        else:
                                            arq_destino.write(line)
                                    else:
                                        if line.startswith('%nprocshared='):
                                            if len(get_parametros(configuracoes, "nprocshared")) > 0:
                                                arq_destino.write('%nprocshared=' +
                                                                  str(get_parametros(configuracoes, "nprocshared")) + '\n')
                                            else:
                                                arq_destino.write(line)
                                        else:
                                            if line.startswith('%rwf='):
                                                if len(get_parametros(configuracoes, "rwf")) > 0:
                                                    arq_destino.write('%rwf=' + get_parametros(configuracoes, 'rwf') + '\n')
                                                else:
                                                    arq_destino.write(line)
                                            else:
                                                arq_destino.write(line)
                            else:
                                if line.startswith("#"):
                                    # linha de parâmetros
                                    if len(get_parametros(configuracoes, "parametros")) > 0:
                                        arq_destino.write(get_parametros(configuracoes, "parametros") + "\n")
                                    else:
                                        arq_destino.write(line)
                        else:
                            if type_sections[pos_section] == "title":
                                arq_destino.write(line)
                            else:
                                if type_sections[pos_section] == "molecule":
                                    if not multiplicidade:
                                        multiplicidade = True
                                        if len(get_parametros(configuracoes, "multiplicidade")) > 0:
                                            arq_destino.write(get_parametros(configuracoes, "multiplicidade") + "\n")
                                        else:
                                            arq_destino.write(line)
                                    else:
                                        # Linhas de especificacao da molécula
                                        if ((len(get_parametros(configuracoes, "layers")) > 0) and (get_parametros(configuracoes, "layers").strip() == "True")):
                                            # Ajustes das camadas
                                            colunas_linha = line.rstrip().split(sep=" ")

                                            # Especificação dasLinhas para as camadas
                                            layer_high = valida_camadas(get_parametros(configuracoes, "layer_high"))
                                            layer_middle = valida_camadas(get_parametros(configuracoes, "layer_middle"))
                                            layer_low = valida_camadas(get_parametros(configuracoes, "layer_low"))

                                            # High
                                            if ((linha >= int(layer_high[0])) and (linha <= int(layer_high[1]))):
                                                # adiciona um valor depois do simbolo da molécula (Freeze)

                                                # colunas_linha[5] = "0"
                                                colunas_linha[5] = get_freeze(configuracoes, "layer_high")

                                                # adiciona uma nova coluna ao final, caso tenha sido especificado pelo usuário
                                                if get_parametros(configuracoes, "layers_simbolo").strip() == "True":
                                                    colunas_linha.append(" H")

                                                texto = " ".join([str(item) for item in colunas_linha])
                                                arq_destino.write(texto + "\n")
                                            else:
                                                # Middle
                                                if (linha >= int(layer_middle[0])) and (linha <= int(layer_middle[1])):
                                                    # adiciona um valor depois do simbolo da molécula
                                                    colunas_linha[5] = get_freeze(configuracoes, "layer_middle")

                                                    # adiciona uma nova coluna ao final, caso tenha sido especificado pelo usuário
                                                    if get_parametros(configuracoes, "layers_simbolo").strip() == "True":
                                                        colunas_linha.append(" M")

                                                    texto = " ".join([str(item) for item in colunas_linha])
                                                    arq_destino.write(texto + "\n")
                                                else:
                                                    # Low
                                                    if ((linha >= int(layer_low[0])) and (linha <= int(layer_low[1]))):
                                                        # adiciona um valor depois do simbolo da molécula
                                                        colunas_linha[5] = get_freeze(configuracoes, "layer_low")

                                                        # adiciona uma nova coluna ao final, caso tenha sido
                                                        # especificado pelo usuário
                                                        if get_parametros(configuracoes, "layers_simbolo").strip() == "True":
                                                            colunas_linha.append(" L")

                                                        texto = " ".join([str(item) for item in colunas_linha])
                                                        arq_destino.write(texto + "\n")
                                                    else:
                                                        arq_destino.write(line)
                                        else:
                                            arq_destino.write(line)

            # Fechando arquivo de origem
            f_input.close()

            # Arquivo de base
            # if len(arq_base) > 0:
            #     with open(arq_base, "r") as f_base:
            #         for line_base in f_base:
            #             arq_destino.write(line_base)
            #     f_base.close()

            # Fechando arquivo de destino
            arq_destino.close()

        script_execucao = get_parametros(configuracoes, "criar_script_execucao")
        if script_execucao == "True":
            if criar_script_execucao(configuracoes):
                print(" - Arquivo de execucao executar_script.sh' criado!")
    else:
        print(f" x Arquivos não encontrados no diretorio ({origem}). Saindo!")
        sys.exit()


if __name__ == "__main__":
    head_msg()

    dict_alteracoes = {}

    if usar_arq_conf():
        dict_alteracoes = ler_arq_conf(dict_alteracoes)
    else:
        dict_alteracoes = questionar(dict_alteracoes)

    if len(dict_alteracoes) >= 1:
        main(dict_alteracoes)
    else:
        print("Nada foi encontrado! Saindo!")
        sys.exit()
