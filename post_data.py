import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as present_of_element_located
from selenium.common.exceptions import TimeoutException

def formatValue(valor):
    try:
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
    
    except Exception as e:
        print(f'Erro na função FormatValue reinicie a aplicaçao: {e}')

def escriturarData(driver,ano, mes ): 
    try:
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
    except Exception as e:
        print(f'Erro na função escriturarData reinicie a aplicaçao: {e}')

def escriturando1(driver):
     
    try:
        clicar_tomados = driver.find_element(By.XPATH, '//*[@id="aba_tomados_lbl"]')
        clicar_tomados.click()
        time.sleep(2)

        clicar_digitardoc = driver.find_element(By.XPATH, '//*[@id="servico_tomado_form:seamj_id836"]')
        clicar_digitardoc.click()
        time.sleep(2)
    except Exception as e:
        print(f'Erro na função escriturando1 reinicie a aplicaçao: {e}')

def finishInscricao(driver, dados, row):

    try:
        
        clicar_cnpj_prestador = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:tipoPesquisaTomadorRb"]/tbody/tr/td[2]/label')
        actions = ActionChains(driver)
        actions.move_to_element(clicar_cnpj_prestador).click().perform()
        time.sleep(1)

        clicar_colocar_cnpj = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:cpfPesquisaTomador"]')
        clicar_colocar_cnpj.click()
        
        driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:cpfPesquisaTomador"]').send_keys(row['CNPJ'])
        time.sleep(1)
        clicar_colocar_cnpj.send_keys(Keys.ENTER)

        time.sleep(2) 
        
        clicar_servico = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:abaServico_lbl"]')
        clicar_servico.click()
        time.sleep(2)
        
        clicar_select = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:tipoDocumentoDigitado"]')

        opcoes = clicar_select.find_elements(By.TAG_NAME, "option")

        for opcao in opcoes:
            texto = opcao.text
            print(f"Opção encontrada: {texto}")  

            if texto.strip() == "NFS-e de Outro Município":
                opcao.click()
                print('✅ Clicou na opção "NFS-e de Outro Município"')
        time.sleep(2)
                
        
        clicar_numero = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:numeroDocumentoDigitado"]')
        clicar_numero.click()
        driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:numeroDocumentoDigitado"]').send_keys(row['Nº DOCUMENTO'])
        time.sleep(1)

        clicar_serie = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:serieDocumentoDigitado"]')
        clicar_serie.send_keys('E')
        time.sleep(1)
        
        data = row['DATA DOCUMENTO'].strftime('%d/%m/%Y')  
        dataDoc = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:dataEmissaoInputDate"]')
        dataDoc.clear()
        dataDoc.send_keys(data)
        time.sleep(1)

        clicar_situacao = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:statusNfse"]')
        select = Select(clicar_situacao)
        select.select_by_index(1)

        time.sleep(1)

        clicar_pesquisarCnae = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:idLinkPesquisarCnae"]')
        clicar_pesquisarCnae.click()
        time.sleep(2)

        codigoCnae = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:idFormularioPesquisaCnae:idCnaePesquisa"]')
        codigoCnae.click()
        driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:idFormularioPesquisaCnae:idCnaePesquisa"]').send_keys(row['CODIGO CNAE'])
        time.sleep(2)
        
        fecharCnae = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:idFormularioPesquisaCnae:idPesquisar"]')
        fecharCnae.click()
        time.sleep(2)

        textDescricao = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:idFormularioPesquisaCnae:idDatatableListaCnae:0:j_id451"]/span').text

        descricaoServico = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:idDescricaoServico"]')
        descricaoServico.send_keys(textDescricao)

        clicar_opçaoCnae = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:idFormularioPesquisaCnae:idDatatableListaCnae:0:j_id451"]')
        clicar_opçaoCnae.click()
        time.sleep(2)

        return textDescricao
    except Exception as e:
        print(f'Erro na função FinishInscriçao reinicie a aplicaçao: {e}')


def escrituracaoFinalStretch(driver, row):
    try:
        clickUF = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:comboEscolherEstadoLocalPrestacao"]')
        clickUF.click()
        time.sleep(1)
                    
        clickUF.send_keys(row['UF'])
        time.sleep(2)
        clickUF.send_keys(Keys.ENTER)
        time.sleep(2)


        clickCity= driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:comboEscolherCidadeLocalPrestacao"]')
        clickCity.click()
        time.sleep(1)
                    
        clickCity.send_keys(row['CIDADE'])
        time.sleep(2)
        clickCity.send_keys(Keys.ENTER)
        time.sleep(2)

        clickOperacao = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:comboEscolherLocalPrestacao"]')

        options = clickOperacao.find_elements(By.TAG_NAME, "option")
        for opcao in options:
            texto = opcao.text
            print(f"Opção encontrada: {texto}")  

            if texto.strip() == "Tributação Fora do Município":
                opcao.click()
                print('✅ Clicou na opção "Tributação Fora do Município"')
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

        clickEscrituracao = driver.find_element(By.XPATH, '//*[@id="digitarDocumentoForm:j_id475"]')
        clickEscrituracao.click()
        print("Finalizando escrituração...")
        time.sleep(2)
      


        try:
            tbody = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="digitarDocumentoForm:confirmacao_customizadaContentTable"]/tbody'))
            )
            if tbody:
                recuse_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="digitarDocumentoForm:j_id491"]'))
                )
                recuse_button.click()
                print('Operação recusada com sucesso.')

                time.sleep(2)

                voltarISS = driver.find_element(By.XPATH, '//*[@id="j_id7"]/img')
                voltarISS.click()
                time.sleep(7)

                return 'inicio'
        except:
            print("❌ Tbody não encontrado. Prosseguindo para verificação de mensagens de erro.")

        try:
            erro_encontrado = False

            for i in range(1, 6):
                try:
                    xpath_mensagem = f'//*[@id="mensagens"]/dt[{i}]'
                    print(f"Tentando localizar mensagem de erro no XPath: {xpath_mensagem}")

                    mensagem_erro = WebDriverWait(driver, 2).until(
                        EC.presence_of_element_located((By.XPATH, xpath_mensagem))
                    )     
                    texto_erro = mensagem_erro.text
                    print(f"🛑 Mensagem encontrada: {texto_erro}") 

                    if "já foi escriturado" in texto_erro.lower():
                        print("🔄 Nota já escriturada. Continuando o processo normalmente...")
                        erro_encontrado = False
                    else:
                        voltarISS = driver.find_element(By.XPATH, '//*[@id="j_id7"]/img')
                        voltarISS.click()
                        time.sleep(2)
                        erro_encontrado = True
                        break

                except:
                    print("Nenhuma mensagem de erro encontrada.")

            if erro_encontrado:
                return 'inicio'

        except Exception as e:
            print(f"⚠ Erro ao verificar mensagens: {e}")
            print("🔄 Continuando o processo normalmente...")

        try:
            clickNewDocument = driver.find_element(By.XPATH, '//*[@id="j_id163:novo"]')
            clickNewDocument.click()
            print("✅ Nota escriturada com sucesso")

            time.sleep(7)
            return 'continua'
        except:
            print("❌ Erro ao tentar clicar no botão de novo documento.")
            return 'erro'   


    except Exception as e:
        print(f'Erro na função escrituracaoFinalStretch reinicie a aplicaçao {e}')