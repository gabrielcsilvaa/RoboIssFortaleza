
# RoboIss


📌 **Sobre o Projeto**  
Este projeto realiza automação de escrituração de notas fiscais relacionadas ao ISS utilizando Python e Selenium, otimizando tarefas e aumentando a produtividade.

Um dos passos essenciais para o funcionamento do robô é alimentar corretamente a planilha do projeto com os dados das notas fiscais. Nela, você deve inserir informações como:
- Código CNAE
- CNPJ da empresa
- Número da nota
- Data de emissão
- Valor
- Outros dados obrigatórios conforme o modelo da planilha

O robô irá ler esses dados da planilha e realizar automaticamente o processo de escrituração no sistema ISS, preenchendo os campos necessários e gerando os documentos conforme solicitado.

---

🚀 **Tecnologias Utilizadas**  
- Python  
- Selenium  
- GitHub  

---

📖 **Manual de Instalação**

### 🛠️ 1. Pré-requisitos  
Antes de começar, certifique-se de ter os seguintes requisitos instalados:  
✅ Python 3.10+  
✅ Git  
✅ Google Chrome  

### 📥 2. Clonando o Repositório  
Abra o terminal ou Prompt de Comando e execute:  
```powershell
git clone https://github.com/gabrielcsilvaa/RoboIss
cd RoboIss
```

### 📦 3. Instalando Dependências  
Com o Python instalado, execute:  
```powershell
pip install -r requirements.txt
```
Se quiser usar um ambiente virtual (recomendado):  
```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 🚀 4. Executando o Projeto  
Para iniciar o script de automação, execute:  
```powershell
python app.py
```

### 🛠️ 5. Possíveis Erros e Soluções

| Erro | Solução |
|------|---------|
| ModuleNotFoundError: No module named 'X' | Execute `pip install -r requirements.txt` novamente. |
| chromedriver not found | Baixe o ChromeDriver correspondente à versão do seu Chrome. |
| Navegador não abre | Atualize o navegador Chrome para a última versão. |




