# taxas-rendimento-escolar-data-analysis

## Descrição do Projeto:

Estou utilizando dados disponibilizados pelo governo que contêm informações detalhadas sobre as taxas de rendimento dos alunos, incluindo taxas de aprovação, reprovação e abandono. Esses dados são coletados na segunda etapa do Censo Escolar da Educação Básica, conhecido como módulo Situação do Aluno.

Ao final do ano letivo, os alunos são avaliados quanto ao preenchimento dos requisitos de aproveitamento e frequência. Eles podem ser considerados:

- Aprovados: Alunos que alcançaram os critérios mínimos para a conclusão satisfatória da etapa de ensino e estão aptos a cursar a série seguinte.
- Reprovados: Alunos que não atenderam aos requisitos mínimos e, portanto, não foram aprovados.
- Abandonos: Alunos que deixaram de frequentar a escola antes do término do ano letivo sem solicitar formalmente a transferência.

O indicador apresenta o percentual de alunos em cada uma dessas categorias. Os dados estão disponíveis em planilha nos formatos Excel® (xlsx).

---

### Pasta onde ficar os arquivos para análise dos dados
![arquivos](https://github.com/user-attachments/assets/c2a8d3d5-bcd8-4d56-9a8b-6a745cc11831)

---

### Arquivo principal onde exercutamos a nossa aplicação para mostra os dados
![arquivo_da_aplicação](https://github.com/user-attachments/assets/372e1908-7ec8-48b4-9ae1-4cb5183d07b8)

---

### Arquivo onde os dados são analisados
![arquivo_de_analise_dos_dados](https://github.com/user-attachments/assets/3c16e180-0f94-4809-84aa-24f77f57f7c4)

---

### Onde fica as bibliotecas usados no projeto
![blibliotecas_usadas_no_projeto](https://github.com/user-attachments/assets/7e7e0525-d6eb-47d1-b825-75db7bad9ba7)

---
## Passos para rodar a aplicação em seu servidor local:
 - 1° Var para pasta raiz do projeto
    ![pasta_raiz_do_projeto](https://github.com/user-attachments/assets/c440e3a6-5c1b-4488-b828-fbaddfd61646)

 - 2° Abra o terminal no vs code ou em um terminal de sua preferencia
    ![terminal](https://github.com/user-attachments/assets/9bd379b6-67ae-4b3b-9352-c81b1aa35919)

 - 3º Inicei um ambiente virtual em seu terminal
     ```
     python -m venv nome_do_ambiente
     ```
 - 4° Ative o ambiente virtual
     ```
     nome_do_ambiente\Scripts\activate
     ```
 - 5º Instale as bibliotecas usadas:
    ```
    pip install -r requirements.txt 
    ```
 - 6° Agora em seu terminal digite esse comanda para rodar a aplicação em seu navegar:
   
   ```
     streamlit run app.py
   ```
