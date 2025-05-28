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

👨‍💻 Autor
Desenvolvido por Ariel Barbosa Santos, estudante de Análise e Desenvolvimento de Sistemas no SENAI - Itumbiara.
GitHub
