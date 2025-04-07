# 🤖 Robô de Download - TMS Praxio

Automatiza o download de planilhas do sistema TMS Praxio.

## 📋 Pré-requisitos
- Python 3.8+
- Chrome instalado
- ChromeDriver (versão compatível)
- Git (opcional)

## ⚙️ Configuração

1. Crie e ative o ambiente virtual:
```bash
python -m venv .venv
# Windows:
.\.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure o arquivo `.env`:
```ini
PRAXIO_USER=seu_usuario
PRAXIO_PASSWORD=sua_senha
DOWNLOADS_PATH=caminho/opcional  # Deixe vazio para usar a pasta padrão
```

## 🚀 Como Usar

### Execução normal:
```bash
python src/main.py
```

### Gerar executável:
```bash
pyinstaller --onefile --add-data "src;src" --collect-all selenium --collect-all pandas --collect-all pywin32 --hidden-import win32con --hidden-import win32gui --hidden-import pywintypes src/main.py
```

## 📂 Estrutura
```
projeto/
├── src/
│   ├── main.py
│   ├── Tables/
│   └── Utils/
├── .env
└── README.md
```

## ⚠️ Atenção
- Nunca compartilhe o arquivo `.env`
- Mantenha o ChromeDriver atualizado
- Recomendado usar ambiente virtual
