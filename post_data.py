import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains


def formatValue(valor):
    if isinstance(valor, (int, float)):
        return f"{valor:.2f}".replace('.', ',')
    elif isinstance(valor, str):
        if ',' in valor:
            partes = valor.split(',')
            if len(partes[1]) == 1:
                return f"{partes[0]},{partes[1]}0"
            return valor
        else:
            return f"{valor},00"
    return valor

def escriturarData(driver,ano, mes ): 

    clicar_escrituracao = driver.find_element(By.XPATH, '//*[@id="navbar"]/ul/li[6]/a')
    clicar_escrituracao.click()
    time.sleep(2)

    clicar_escrituracao2 = driver.find_element(By.XPATH, '//*[@id="formMenuTopo:menuEscrituracao:j_id78"]')
    clicar_escrituracao2.click()
    time.sleep(2) 

    clicar_data =  driver.find_element(By.XPATH,'//*[@id="manterEscrituracaoForm:dataInicialHeader"]/label/div' ) 
    clicar_data.click()
    time.sleep(2)

    clicar_mes = driver.find_element(By.XPATH, f'//*[@id="manterEscrituracaoForm:dataInicialDateEditorLayoutM{mes - 1}"]')
    clicar_mes.click()
    time.sleep(2)

    lista_tabela_ano = driver.find_elements(By.XPATH, '//*[@id="manterEscrituracaoForm:dataInicialDateEditorLayout"]/tbody/tr/td/div')
    for i in lista_tabela_ano:
        if i.text == ano:
            i.click()
    time.sleep(1)

    clicar_ok = driver.find_element(By.XPATH, '//*[@id="manterEscrituracaoForm:dataInicialDateEditorButtonOk"]')
    clicar_ok.click()
    time.sleep(1)

    clicar_data2 = driver.find_element(By.XPATH, '//*[@id="manterEscrituracaoForm:dataFinalHeader"]/label/div')
    clicar_data2.click()
    time.sleep(1)

    clicar_mes2 = driver.find_element(By.XPATH, f'//*[@id="manterEscrituracaoForm:dataFinalDateEditorLayoutM{mes - 1}"]')
    clicar_mes2.click()
    time.sleep(1)

    lista_tabela_ano2 = driver.find_elements(By.XPATH, '//*[@id="manterEscrituracaoForm:dataFinalDateEditorLayout"]/tbody/tr/td/div')
    for i in lista_tabela_ano2:
        if i.text == ano:
            i.click()
    time.sleep(1)

    clicar_ok = driver.find_element(By.XPATH, '//*[@id="manterEscrituracaoForm:dataFinalDateEditorButtonOk"]')
    clicar_ok.click()
    time.sleep(2)

    clicar_consultar = driver.find_element(By.XPATH, '//*[@id="manterEscrituracaoForm:btnConsultar"]')
    clicar_consultar.click()
    time.sleep(2)

    clicar_escriturar = driver.find_element(By.XPATH, '//*[@id="manterEscrituracaoForm:dataTable:0:escriturar"]')
    clicar_escriturar.click()
    time.sleep(10)


def escriturando1(driver):
     

    clicar_tomados = driver.find_element(By.XPATH, '//*[@id="aba_tomados_lbl"]')
    clicar_tomados.click()
    time.sleep(2)

    clicar_digitardoc = driver.find_element(By.XPATH, '//*[@id="servico_tomado_form:seamj_id836"]')
    clicar_digitardoc.click()
    time.sleep(2)


def finishInscricao(driver, dados):
    clicar_cnpj_prestador = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:tipoPesquisaTomadorRb"]/tbody/tr/td[2]/label')
    actions = ActionChains(driver)
    actions.move_to_element(clicar_cnpj_prestador).click().perform()
    time.sleep(1)

    clicar_colocar_cnpj = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:cpfPesquisaTomador"]')
    clicar_colocar_cnpj.click()
    for index, row in dados.iterrows():
        driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:cpfPesquisaTomador"]').send_keys(row['CNPJ'])
        time.sleep(1)
        clicar_colocar_cnpj.send_keys(Keys.ENTER)
    time.sleep(2) 
    
    clicar_servico = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:abaServico_lbl"]')
    clicar_servico.click()
    time.sleep(2)

    clicar_select = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:tipoDocumentoDigitado"]')
    clicar_select.click()
    time.sleep(2)
    for i in range(1):
        clicar_select.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        clicar_select.send_keys(Keys.ENTER)
        time.sleep(2)

    clicar_numero = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:numeroDocumentoDigitado"]')
    clicar_numero.click()
    driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:numeroDocumentoDigitado"]').send_keys(row['Nº DOCUMENTO'])
    time.sleep(1)

    clicar_serie = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:serieDocumentoDigitado"]')
    clicar_serie.send_keys('E')

    dados['DATA DOCUMENTO'] = pd.to_datetime(dados['DATA DOCUMENTO'], errors='coerce').dt.strftime('%d/%m/%Y')
    if dados['DATA DOCUMENTO'].isnull().any():
        print("Há valores inválidos na coluna 'DATA DOCUMENTO'. Por favor, revise a planilha.")
    else:
        for index,row in dados.iterrows():
            dataDoc = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:dataEmissaoInputDate"]')
            dataDoc.clear()
            dataDoc.send_keys(row['DATA DOCUMENTO'])
            time.sleep(1)

    clicar_situacao = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:statusNfse"]')
    clicar_situacao.click()
    time.sleep(1)
    for i in range(1):
        clicar_situacao.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
    clicar_situacao.send_keys(Keys.ENTER)
    time.sleep(2)

    clicar_pesquisarCnae = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:idLinkPesquisarCnae"]')
    clicar_pesquisarCnae.click()
    time.sleep(2)

    codigoCnae = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:idFormularioPesquisaCnae:idCnaePesquisa"]')
    codigoCnae.click()
    driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:idFormularioPesquisaCnae:idCnaePesquisa"]').send_keys(row['CODIGO CNAE'])
    time.sleep(2)
    
    fecharCnae = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:idFormularioPesquisaCnae:idPesquisar"]')
    fecharCnae.click()
    time.sleep(3)

    textDescricao = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:idFormularioPesquisaCnae:idDatatableListaCnae:0:j_id451"]/span').text

    clicar_opçaoCnae = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:idFormularioPesquisaCnae:idDatatableListaCnae:0:j_id451"]')
    clicar_opçaoCnae.click()
    time.sleep(2)

    return textDescricao

def escrituracaoFinalStretch(driver, dados):
    clickUF = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:comboEscolherEstadoLocalPrestacao"]')
    clickUF.click()
    time.sleep(1)
    for i, row in dados.iterrows():             
        clickUF.send_keys(row['UF'])
        time.sleep(2)
        clickUF.send_keys(Keys.ENTER)
        time.sleep(2)


    clickCity= driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:comboEscolherCidadeLocalPrestacao"]')
    clickCity.click()
    time.sleep(1)
    for i, row in dados.iterrows():             
        clickCity.send_keys(row['CIDADE'])
        time.sleep(2)
        clickCity.send_keys(Keys.ENTER)
        time.sleep(2)

    clickOperacao = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:comboEscolherLocalPrestacao"]')
    clickOperacao.click()
    for i in range(1):
        clickOperacao.send_keys(Keys.ARROW_DOWN)
        time.sleep(3)
        clickOperacao.send_keys(Keys.ENTER)
        time.sleep(2)

    clickIssRetido = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:divIssRetidoSub"]/input')
    clickIssRetido.click()
    time.sleep(2)

    valor_servico = row['VALOR DO SERVIÇO']
    valor_formatado = formatValue(valor_servico)

    valorServico = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:idValorServicoPrestado"]')
    valorServico.click()
    valorServico.send_keys(valor_formatado)
    time.sleep(3)

    # clickEscrituracao = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:j_id475"]')
    # clickEscrituracao.click()
    time.sleep(1000)
