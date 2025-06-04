LabFlow
LabFlow é um sistema de controle de laboratórios desenvolvido como parte do Trabalho de Conclusão de Curso (TCC) no curso de Análise e Desenvolvimento de Sistemas do SENAI - Itumbiara. O objetivo principal é oferecer uma solução digital para o gerenciamento eficiente de laboratórios, facilitando o controle de equipamentos, agendamentos e registros de atividades.
GitHub

📋 Sumário
Funcionalidades

Tecnologias Utilizadas

Instalação

Uso

Contribuição

Licença

Autor

✅ Funcionalidades
Cadastro e gerenciamento de laboratórios.

Registro de equipamentos e seus respectivos detalhes.

Agendamento de uso dos laboratórios.

Geração de relatórios de atividades.

Interface intuitiva para facilitar a navegação e uso do sistema.

🛠 Tecnologias Utilizadas
Python: Linguagem principal do backend.

Django: Framework web utilizado para o desenvolvimento do backend.

SQLite: Banco de dados leve e de fácil configuração.

HTML/CSS: Estrutura e estilização das páginas web.
GitHub

💻 Instalação
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/ariel-barbosa/labcontrol.git
GitHub

Navegue até o diretório do projeto:

bash
Copiar
Editar
cd labcontrol
GitHub

Crie e ative um ambiente virtual:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Para Unix/Linux
venv\Scripts\activate  # Para Windows
GitHub

Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Aplique as migrações do banco de dados:

bash
Copiar
Editar
python manage.py migrate
GitHub

Inicie o servidor de desenvolvimento:

bash
Copiar
Editar
python manage.py runserver
O sistema estará disponível em http://127.0.0.1:8000/.

🚀 Uso
Acesse a interface web através do navegador.

Utilize as funcionalidades disponíveis para cadastrar laboratórios, equipamentos e agendamentos.

Gere relatórios conforme necessário para análise e controle.

🤝 Contribuição
Contribuições são bem-vindas! Se você deseja contribuir com melhorias ou correções:
GitHub

Fork este repositório.

Crie uma branch para sua feature: git checkout -b minha-feature.

Faça commit das suas alterações: git commit -m 'Minha nova feature'.

Envie para o repositório remoto: git push origin minha-feature.

Abra um Pull Request detalhando suas alterações.
GitHub

📄 Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

#############################################################################################
#############################################################################################

# Dependências do Projeto LabControl

## Requisitos do Sistema

- Python 3.8 ou superior
- Django 5.1 ou superior
- Banco de dados (SQLite3 padrão ou PostgreSQL para produção)
- Node.js (para recursos frontend opcionais)

## Dependências Principais

### Core Django
- `Django` (>=5.1.7) - Framework web principal
- `django-crispy-forms` (>=2.0) - Para formulários estilizados
- `crispy-bootstrap5` (>=2022.1) - Template pack para Bootstrap 5
- `django-widget-tweaks` (>=1.5.0) - Para personalização de widgets de formulários

### Banco de Dados
- `psycopg2-binary` (>=2.9.0) - Adaptador PostgreSQL (opcional para produção)
- `sqlite3` - Incluído no Python (para desenvolvimento)

### Desenvolvimento
- `black` (>=22.0) - Formatador de código Python
- `pytest` (>=7.0) - Framework de testes
- `pytest-django` (>=4.5.0) - Plugin para testar projetos Django
- `Faker` (>=12.0) - Geração de dados de teste

### Frontend
- `Bootstrap 5` (>=5.1.3) - Framework CSS
- `jQuery` (>=3.6.0) - Biblioteca JavaScript
- `Font Awesome` (>=5.15.4) - Ícones
- `DataTables` (>=1.11.3) - Para tabelas interativas (opcional)

## Instalação

1. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Instale as dependências:
```bash
pip install django crispy-forms crispy-bootstrap5 django-widget-tweaks psycopg2-binary
```

3. Para desenvolvimento, instale também:
```bash
pip install black pytest pytest-django Faker
```

## Arquivo requirements.txt exemplo

```
Django==5.1.7
django-crispy-forms==2.0
crispy-bootstrap5==2022.1
django-widget-tweaks==1.5.0
psycopg2-binary==2.9.0
black==22.0
pytest==7.0
pytest-django==4.5.0
Faker==12.0
```

## Configuração Adicional

Para usar PostgreSQL em produção, descomente a configuração do banco de dados em `settings.py` e certifique-se de ter o `psycopg2-binary` instalado.

Para recursos frontend adicionais, inclua os arquivos CSS/JS do Bootstrap, jQuery e outras bibliotecas no diretório `static/` do seu projeto.



👨‍💻 Autor
Desenvolvido por Ariel Barbosa Santos, estudante de Análise e Desenvolvimento de Sistemas no SENAI - Itumbiara.
GitHub
