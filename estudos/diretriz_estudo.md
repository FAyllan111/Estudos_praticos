# 📘 Documento Mestre de Continuidade — Roadmap de Desenvolvimento Profissional

**Versão:** 1.1
**Data de fechamento:** 12/11/2026
**Autor:** Francisco Ayllan Alves e Silva
**Propósito:** Documento de handoff para migração entre chats de IA, atualização de diretrizes e consolidação do roadmap profissional do autor. Deve ser lido integralmente antes de qualquer interação nova.

---

## Histórico de versões

- **v1.0 — 12/11/2026:** documento-base, com perfil-alvo, roadmap, ciclo de estudo e stack inicial.
- **v1.1 — 12/11/2026:** revisão após parecer externo; refinamento do perfil-alvo, correções de sequência e critérios, delimitação dos projetos de gastos e restaurante, redefinição do L4 e inclusão do princípio de autonomia e responsabilidade técnica perante IA.

---

## 🎯 PARTE 1 — Sumário Executivo (leia primeiro)

Este documento consolida discussões sobre:
1. Diagnóstico do estado atual do autor como profissional de dados
2. Definição do perfil-alvo: Analytics Engineer com capacidade end-to-end
3. Roadmap de aproximadamente 24 meses, organizado em quatro fases (Fase 0 a Fase 3)
4. Ciclo de estudo com IA e critérios objetivos de progressão
5. Stack consolidada em três camadas de prioridade
6. Projetos progressivos para aplicar os conhecimentos
7. Regras para desenvolver autonomia e evitar dependência de IA

**Conclusão central:** a lacuna predominante é de **tradução e autonomia** (ideia → implementação → validação), com possíveis lacunas conceituais e sintáticas específicas. O diagnóstico deve ser atualizado por evidências de execução, não tratado como uma característica imutável.

**Princípio central:** a IA pode acelerar a implementação e produzir código, mas o autor permanece responsável por compreender o problema, justificar as decisões técnicas, revisar o código, validar os resultados, diagnosticar falhas e sustentar a solução.

**Decisão sobre o gate:** não existe faixa de 60–79% com ressalva. O piso é 80%, arredondado sempre para cima, com exigência adicional de desempenho prático.

---

## 👤 PARTE 2 — Perfil do Autor (estado real, não aspiracional)

### 2.1 Dados objetivos

| Campo | Valor |
|---|---|
| Nome | Francisco Ayllan Alves e Silva |
| Localização atual | Teresina, PI |
| Localização-alvo | Fortaleza, CE (migração em ~2 anos) |
| Cargo atual | Analista de Dados e Automação na Ferronorte |
| Setor | Construção/Distribuição de aço (empresa familiar) |
| Formação | Em andamento/transição para Analytics Engineer |
| Tempo disponível | 1-1:30h/noite (dias úteis), blocos maiores eventuais |
| Experiência com IA | Alta dependência de copiloto (copiar código manualmente) |
| Nível técnico autodeclarado | Iniciante avançado em Python |

### 2.2 Ferramentas que o autor **usa** hoje

- Excel, Power Query, VBA
- Power BI
- SQL Oracle (somente leitura via ODBC)
- Python (Pandas, Streamlit, pytest básico)
- VS Code, Git, GitHub
- Oracle Client (thin/thick mode)

### 2.3 Ferramentas que o autor **já viu mas não domina**

- `try/except/finally` (sabe o que é, copia mas não produz do zero)
- List/dict comprehensions
- `lambda`, `map`, `filter`
- POO básica (usa classes do projeto, mas não produz)
- pytest (22 testes rodando em projeto, mas quais ele escreveu?)
- DuckDB (iniciando no DataMart)
- Docker (não usa)
- FastAPI (nunca usou)

### 2.4 Ferramentas que o autor **nunca viu**

- Polars
- dbt
- Orquestração (Airflow, Dagster, Prefect)
- Playwright / automação de navegador
- PostgreSQL (escrita transacional)
- API como cliente (`requests`, integração externa)

### 2.5 Projetos ativos

**Projeto 1 — Ferronorte Comercial (Streamlit, em produção interna)**
- Estoque Parado (aprovado pelo gestor, em testes)
- Compras SLZ (MVP simplificado em andamento)
- Local-only (D-62), não acessa Oracle Cloud (E108)

**Projeto 2 — DataMart Comercial (DuckDB + Oracle, em construção)**
- Pipeline com 40/40 etapas verdes (extract + transform + reconcile)
- `dim_fornecedor` commitado (14.712 linhas, 22 testes)
- Iniciando `fato_compras` (accumulating snapshot)

### 2.6 Histórico de padrão comportamental (diagnóstico)

**Padrão a monitorar:** tendência a ampliar o planejamento antes de concluir uma entrega pequena:
- Houve múltiplos turnos de planejamento do roadmap.
- Foram discutidas várias propostas de projetos pessoais, ainda sem projeto pessoal concluído.
- Cada proposta apresentou justificativas legítimas.
- Em alguns momentos, quando se aproximava uma atividade pequena e específica, surgiu uma proposta de escopo maior.

**Isso não é crítica moral nem diagnóstico definitivo.** É um comportamento observado que deve ser tratado como dado de planejamento: ciclos pequenos, entregas verificáveis, um projeto por vez e critérios objetivos de conclusão.

### 2.7 Limitações concretas a serem desenvolvidas

1. **Experiência limitada com escrita em banco de dados** — a experiência profissional citada é principalmente read-only no Oracle.
2. **Ausência de projeto pessoal completo concluído** — há projetos empresariais, mas ainda não há projeto pessoal finalizado.
3. **Dependência de IA na fronteira técnica** — o autor reconhece que frequentemente recebe código pronto e o reproduz manualmente.
4. **Lacuna predominante de tradução e autonomia** — dificuldade em transformar intenção em implementação independente, com possíveis lacunas conceituais e sintáticas específicas que deverão ser identificadas durante a prática.

---

## 🎯 PARTE 3 — Perfil-Alvo e Definição

### 3.1 Definição oficial do perfil

> **"Sou um Analytics Engineer com capacidade end-to-end. Construo soluções de dados completas que resolvem problemas reais de negócio, especialmente em pequenas e médias empresas com infraestrutura limitada. Utilizo Python e SQL para extração, transformação e validação; DuckDB e PostgreSQL conforme a finalidade do armazenamento; ferramentas de modelagem e qualidade para estruturar dados confiáveis; e Streamlit e Power BI para disponibilizar resultados. Consigo conectar as etapas do problema à entrega, sem depender necessariamente de outro time para cada camada."**

A ambição de longo prazo é preservar o DNA da **"mosquinha branca"**: conseguir resolver o problema inteiro de uma PME, da compreensão da necessidade à entrega e sustentação da solução, sem perder o foco principal em Engenharia Analítica.

### 3.2 Justificativa do perfil

- **Mercado regional (Teresina/Fortaleza):** PMEs com cultura de dados ainda em desenvolvimento, restrições de investimento e equipes de TI reduzidas ou pouco acessíveis.
- **Necessidade:** profissional capaz de conectar negócio, dados, automação e entrega, escolhendo uma solução proporcional à infraestrutura e à maturidade da empresa.
- **Diferencial:** Analytics Engineering como núcleo, ampliado por competências práticas de Data Engineering e desenvolvimento Python, com forte orientação a problemas de negócio.

### 3.3 O que **está** no escopo

- Extração de dados (API, scraping, CSV, banco)
- Pipelines ETL/ELT (Bronze/Silver/Gold)
- Modelagem dimensional (Kimball)
- Data Marts / Data Lakes (DuckDB, Parquet, PostgreSQL)
- Qualidade de dados (pytest, Pandera)
- BI e dashboards (Streamlit, Power BI)
- Automação de tarefas (scripts, Playwright)
- Deploy básico (Docker, Streamlit Cloud, GitHub Actions)
- Estatística descritiva e correlação (básico)

### 3.4 O que **NÃO está** no escopo (consciência, não estudo)

- Backend puro (Java, Spring, .NET, Node.js)
- Mobile nativo (React Native, Flutter)
- Frontend complexo (React, Vue, Next.js)
- ORM profundo (SQLAlchemy avançado)
- Auth complexo (OAuth2, refresh token, RBAC)
- Kubernetes, Terraform
- Spark, Databricks, Snowflake (consciência para entrevista)
- Kafka, streaming em tempo real
- Data Science / ML formal (estatística pesada, scikit-learn)
- Data Vault, Data Mesh (arquitetura corporativa)
- Data Architect (C4 Model, mentoria, ADRs formais)

---

## 🧭 PARTE 4 — Cronologia Completa da Conversa (decisões em ordem)

### Turno 1-3 — Contexto inicial e roadmap de dívidas técnicas
- Apresentado o histórico do projeto Ferronorte (Comercial + DataMart)
- Listadas ~35 dívidas técnicas (E11-E143, C01-C10, D1-D30)
- IA propôs roadmap em 4 trilhas de estudo (Pandas, Streamlit, Python, Oracle)

### Turno 4 — Pivotagem para C02 (pytest)
- Autor escolheu começar por testes automatizados
- IA detalhou fundamentos de pytest (assert, fixtures, mocks, parametrize)
- Estrutura sugerida: `tests/unit/` + `tests/integration/`

### Turno 5-6 — Dívidas de modelagem dimensional
- Autor trouxe registro de dívidas do DataMart (Star schema, bridges, accumulating snapshot)
- IA propôs 5 trilhas: modelagem, DuckDB+Medallion, catálogo de fontes, qualidade, etc.

### Turno 7 — Edital de concurso como termômetro
- Autor pediu análise de edital federal (Cientista de Dados) para calibrar mercado
- IA filtrou: SQL avançado, Python, modelagem, governança são essenciais; estatística/ML são opcionais
- Listou 10 cursos do catálogo como essenciais

### Turno 8-10 — Catálogo de cursos
- Autor forneceu lista de 40 cursos
- IA classificou em 4 tiers (S, A, B, Skip)
- Recomendou foco: 24 (Eng. Analytics), 125 (Modelagem), 273 (Boas práticas Python)

### Turno 11-12 — Docker, VM, deploy
- Autor perguntou sobre `.bat`, Streamlit Cloud, Docker 24/7
- IA explicou: Docker grátis para uso pessoal, `.bat` é local, Streamlit Cloud não serve (Oracle IP privado)
- Discutido `docker context` para configurar VM remota via SSH

### Turno 13 — Vagas do Santander como termômetro
- Autor trouxe 3 vagas (Data Scientist, IT Developer, Risk Models)
- IA diagnosticou: **3 carreiras diferentes**, não uma
- Autor está alinhado com Vaga 1 (Business/Data Analyst)

### Turno 14 — Vaga Jr em Teresina
- Autor trouxe vaga de Assistente de Desenvolvimento Jr
- IA diagnosticou: é Dev Júnior com foco em automação, não dados
- Autor confirmou: não está buscando ativamente, só termômetro

### Turno 15 — O insight central (dependência de IA)
- **Autor reconheceu:** *"meu maior medo é de depender da IA para tudo... estou acabando por fazer isso, não de vibecodar mas de a IA escrever e eu copiar"*
- **Este é o insight que reorganiza tudo**

### Turno 16-17 — Diretrizes (trabalho vs estudo)
- Autor trouxe diretriz de trabalho (36 seções, madura, em uso)
- IA diagnosticou: **a diretriz permite Modo Entrega**, e isso vira escape hatch no estudo
- **Decisão:** duas diretrizes com filosofias opostas (trabalho otimiza entrega; estudo otimiza autonomia)
- **Decisão:** não escrever a diretriz de estudo ainda; calibrar por comportamento real

### Turno 18 — Sessão 40/40 real (bug do reconcile)
- Autor mostrou sessão real de debugging (bug em `_reconcile_fato_estoque`)
- IA identificou 2 linhas trocadas (`dim_loja` vs `dim_produto`)
- **Insight:** a sessão gerou 5 aulas não drenadas
  1. Diagnóstico diferencial (bisseccionar filtro)
  2. Notar contradição = código divergente
  3. Nome da variável vs conteúdo
  4. Isolar causa de cada teste que falha
  5. Não chutar antes de ver código real

### Turno 19-20 — Pipeline de gastos vs sistema de restaurante
- Autor propôs 2 projetos: app de gastos e sistema de restaurante
- IA argumentou contra o restaurante (armadilha de 6-12 meses)
- Autor defendeu: restaurante ensina escrita em banco, ACID, API, auth
- **Terceiro parecer (outra IA) validou o restaurante mínimo**
- **Decisão final:** ambos viáveis; ordem a definir

### Turno 21 — Síntese crítica
- IA reconheceu os pontos do terceiro parecer (read-only é lacuna real)
- IA apontou 3 omissões do terceiro parecer:
  1. As 5 aulas continuam não drenadas
  2. O padrão de "começar grande" não foi nomeado
  3. A mudança de alvo (AE → DE) não foi nomeada

### Turno 22 — Definição do perfil
- Autor detalhou objetivo completo: "mosquinha branca de dados"
- **Definição fechada:** "Desenvolvedor de Soluções de Dados"
- Perfil híbrido, pragmático, regional

### Turno 23 — Modelo de 3 camadas
- **Decisão:** L1-L4 de conhecimento (Desconhecido/Consciência/Mapa/Aplicação assistida/Domínio)
- **Decisão:** L2 para ~15 ferramentas (conhecer), L4 para ~5 (dominar)
- **Decisão:** trilhas A e B no ciclo de estudo

### Turno 24 — Pesquisa de stack de mercado
- **Dados reais:** SQL (1044), Databricks (446), GCP (273), Spark (268), Postgres (191), Airflow (139), dbt (109)
- **Tensão:** stack de mercado ≠ stack de PME
- **Decisão:** priorizar stack de PME, ter consciência da stack de mercado

### Turno 25 — Ciclo de estudo com IA (definição)
- Reprodução cega antes das questões
- Questões teóricas (3-5) + práticas (3) = mínimo 5 total
- Gate: `ceil(0.8 × total)`, sem ressalva
- Correção socrática no 1º erro, direta no 2º
- Retorno D+3 ou D+7 (só erradas + 1 integração)
- Diário obrigatório

### Turno 26 — Decisões finais
- D1: gate 80% mesmo, sem ressalva
- D2: correção socrática mantida
- D3: `ceil(0.8 × total)` sempre para cima
- D4: **tópicos novos** precisam de trilha B (exemplo antes de reprodução)
- D5: retorno só das erradas + 1 integração
- D7: escopo definido pela IA
- D8: gate decide passou/não passou, como prova
- **Removida a ressalva 60-79%** — não avança

### Turno 27 — Diretriz de Estudo v0.1 consolidada
- Ciclo formalizado com trilhas A e B
- 3 pontas soltas: formato do diário, agendamento de retorno, primeiro tópico

### Turno 28 — Validação da lista base
- Autor trouxe lista de ~40 tópicos (base, engenharia, web, BD, produção)
- IA diagnosticou 6 erros na ordem original:
  1. Web antes de BD (errado)
  2. Granularidade desigual
  3. Web inchado
  4. Itens fora do perfil
  5. Falta "por quê" e "onde"
  6. Projeto só no fim
- **Decisão:** manter a ordem corrigida (Fase 0 → Projeto 1 → Fase 1 → Projeto 2 → Fase 2 → Projeto 3)

### Turno 29 — Projetos-âncora por fase
- **Decisão:** 3 opções por fase, autor escolhe
- Fase 0: Gastos / Olist / APIs
- Fase 1: Restaurante / Vagas de emprego / Estoque CLI
- Fase 2: ERP fechado / Financeiro / Monitoramento de preços

### Turno 30 — Revisão externa e consolidação v1.1
- Perfil ajustado para **Analytics Engineer com capacidade end-to-end**.
- Diagnóstico refinado: lacuna predominante de tradução e autonomia, sem presumir ausência total de lacunas conceituais ou sintáticas.
- Sequência de projetos definida: **drenagem das 5 aulas → gastos pessoais → restaurante → camada analítica**.
- Fase 0 reorganizada, com SQL explícito e separação SQLite operacional / DuckDB analítico.
- MVP do restaurante delimitado em dez funcionalidades, com emissão fiscal real fora do primeiro escopo.
- Gate de estudo corrigido para mínimo de seis questões, 80% e desempenho prático mínimo.
- L4 redefinido para permitir consulta à documentação.
- Inserido o princípio de autonomia e responsabilidade técnica perante IA, o checklist de revisão de código e o bilhete diário de 2 minutos.

---

## 🏗️ PARTE 5 — Roadmap Consolidado (Fases 0 a 3, aproximadamente 24 meses)

### ⏱️ Premissas

- Disponibilidade de referência: 1h a 1h30 por sessão, principalmente à noite.
- Rotina mínima: quatro sessões obrigatórias e uma sessão opcional por semana; meta desejada de cinco a seis sessões semanais quando sustentável.
- Horizonte de aproximadamente 24 meses para atingir uma parcela substancial do perfil-alvo; o percentual de ~70% é uma meta orientativa, não uma promessa.
- Um projeto por vez. O projeto seguinte só começa depois do gate de conclusão do anterior.
- Cada projeto deve ter README com cinco seções: problema, requisitos/escopo, arquitetura/stack, execução e validação/limitações.
- Todo projeto deve ser versionado no Git. A publicação no GitHub será pública somente quando não houver dados pessoais, credenciais, informações sensíveis ou código proprietário. Projetos demonstrativos devem usar dados fictícios ou públicos.
- O calendário é uma referência de planejamento. Ajustar datas, duração ou distribuição de tópicos não representa fracasso, desde que o escopo, os gates e a ordem de dependência sejam preservados.
- A escolha de tecnologia segue o princípio **problema primeiro, tecnologia depois**. Não estudar ferramenta apenas por novidade ou por aparecer em uma vaga.

### 🎯 FASE 0 — Fundação (meses 1-3, aproximadamente 13 semanas)

**Objetivo:** consolidar os fundamentos de Python, SQL e engenharia básica; aplicar manipulação e modelagem de dados; concluir um primeiro projeto pessoal com fluxo operacional e analítico.

**Pré-requisito:** as sessões iniciais devem drenar as cinco aulas da sessão 40/40, descritas na Parte 11. Elas são a primeira aplicação prática do ciclo de estudo.

**Fundamentos transversais a verificar por exercícios:** variáveis, tipos de dados, condicionais, loops e funções. Como esses conceitos já foram estudados, não haverá revisão extensa automática; lacunas específicas identificadas durante a prática serão retomadas antes de avançar.

**Debugging:** será praticado desde o início, incluindo leitura de traceback, breakpoints, inspeção de variáveis, isolamento de etapas e reprodução mínima de erros. As cinco aulas da Parte 11 são parte desse treinamento.

**Tópicos fundamentais — ordem de prioridade:**
1. As cinco aulas da sessão 40/40.
2. Listas: criação, indexação, fatiamento, métodos e iteração.
3. Dicionários: criação, acesso, `get`, `setdefault` e comprehensions.
4. Tuplas e sets: finalidade, operações e casos de uso.
5. Exceções: `try/except/finally`, exceções específicas e exceções customizadas.
6. Módulos, imports, organização e `__init__.py`.
7. Arquivos, `pathlib`, caminhos e encoding.
8. Ambientes e ferramentas: `venv`, `pip`, `requirements`, Git, branches e pull requests.
9. SQL fundamental: `SELECT`, filtros, `JOIN`, cardinalidade, `GROUP BY`, agregações, `CASE`, `NULL` e CTEs.
10. pytest: testes, fixtures, parametrização e mocks básicos.
11. Logging: módulo `logging` ou alternativa como Loguru; compreender níveis e contexto dos registros.
12. Pandas: leitura, seleção com `loc`/`iloc`, `groupby`, `merge` e validações básicas.
13. DuckDB: consultas sobre Parquet e processamento analítico local.
14. Modelagem dimensional: fatos, dimensões, granularidade e star schema.
15. Tipagem básica: type hints para clareza e manutenção.

**Aplicação na interface:**
16. Streamlit: multipage, formulários, cache e `session_state`, conforme a necessidade do projeto.

**Complementares — nível L2 inicialmente, sem aprofundamento obrigatório:**
17. `lambda`, `map` e `filter`.
18. Polars: estudar somente quando houver um dataset ou gargalo real em que Pandas deixe de atender aos requisitos. Não antecipar a troca por preferência tecnológica.

**Projeto-âncora definido: A — Controle de Gastos Pessoais**

Problema: compreender para onde o dinheiro vai e registrar movimentações de forma organizada.

| Camada | Tecnologia | Responsabilidade |
|---|---|---|
| Operacional | SQLite | CRUD de receitas, despesas, categorias e movimentações; persistência local simples para uso pessoal |
| Analítica | DuckDB + Parquet | Consultas, consolidações e análises sobre os dados exportados/organizados |
| Transformação | Pandas | Limpeza, transformação e preparação dos dados quando necessário |
| Interface | Streamlit | Cadastro, consulta, edição e visualização em uma interface única |
| Qualidade | pytest | Testar regras de negócio, cálculos, validações e operações principais |

**Distinção importante:** SQLite será o banco operacional do aplicativo pessoal; DuckDB será utilizado como motor analítico. Não tratar os dois como substitutos diretos: cumprem papéis diferentes no projeto.

**Escopo inicial do projeto:** cadastro e edição de receitas/despesas, categorias, contas ou carteiras, filtros por período e categoria, cálculo de saldo e dashboard mensal. Parcelamentos, cartões e orçamentos avançados entram apenas se forem necessários e couberem no escopo após a primeira versão funcional.

**Gate da Fase 0:** aplicação funcional com CRUD persistido em SQLite, camada analítica simples em DuckDB, dashboard Streamlit, pelo menos cinco testes automatizados relevantes, README completo e execução reproduzível. Dados pessoais reais não devem ser publicados no repositório.

**Cursos:** 273 (Boas práticas em Python), 125 (Modelagem de dados), 24 (Engenharia de Analytics) e 25 (Primeiros passos em Engenharia de Dados), conforme sequência e necessidade dos tópicos.

---

### 🎯 FASE 1 — Transação e Serviço (meses 4-6, aproximadamente 13 semanas)

**Objetivo:** superar a lacuna de experiência com escrita em banco, compreender transações ACID e desenvolver uma aplicação cliente-servidor simples, com API e autenticação básica.

**Tópicos — ordem de referência:**
1. POO: classes, `__init__`, atributos e métodos.
2. POO: composição versus herança; priorizar composição quando adequada.
3. Dunder methods essenciais, como `__repr__` e `__eq__`, quando houver necessidade concreta.
4. SQL DDL: `CREATE TABLE`, chaves primárias e estrangeiras, constraints.
5. SQL DML: `INSERT`, `UPDATE` e `DELETE`.
6. Transações: `BEGIN`, `COMMIT`, `ROLLBACK`, atomicidade e consistência.
7. PostgreSQL em ambiente Docker; conexão e operações com `psycopg`.
8. HTTP básico: requisição, resposta, métodos, status codes, headers e JSON.
9. FastAPI: rotas, parâmetros, validação e Pydantic.
10. Autenticação e autorização básicas para o contexto do projeto; hash seguro de senha e permissões por função, sem aprofundar OAuth2 ou RBAC corporativo.
11. Docker: Dockerfile e `docker-compose`.
12. Streamlit como cliente da API, utilizando `requests` quando adequado.

**Manter em consciência ou fora do escopo inicial:** SQLAlchemy profundo, middlewares avançados, OAuth2, RBAC complexo, Celery, CORS avançado, arquitetura de microserviços e aplicativo mobile nativo.

**Projeto-âncora definido: Sistema de Atendimento de Restaurante — MVP**

Objetivo: desenvolver um sistema web responsivo para registrar pedidos, apoiar a operação da cozinha e controlar o fechamento da conta. Os garçons poderão acessar pelo navegador do próprio celular; não será necessário desenvolver aplicativo Android/iOS nativo.

**MVP — dez funcionalidades incluídas:**
1. Login dos funcionários e identificação de papéis básicos.
2. Cadastro de mesas e produtos.
3. Abertura de mesa.
4. Registro de pedidos pelo garçom, em interface web responsiva.
5. Envio dos pedidos para uma fila ou tela da cozinha.
6. Atualização de status do pedido: recebido, em preparação e pronto.
7. Fechamento da conta e consolidação dos itens consumidos.
8. Registro manual de pagamentos, com forma e valor pagos.
9. Emissão de recibo/comanda **não fiscal**.
10. Liberação da mesa após o fechamento conforme as regras implementadas.

**Fora do primeiro MVP:** emissão de NFC-e ou outro documento fiscal verdadeiro; integração com adquirentes, cartões ou gateways; aplicativo nativo; delivery; controle completo de estoque e compras; múltiplas unidades; divisão avançada de contas e pagamentos parciais. Esses itens só entram em novas etapas após o MVP estar estável e após avaliação específica de requisitos.

**Distinção operacional e fiscal:** fechar a conta, registrar um pagamento no sistema e emitir um documento fiscal são processos diferentes. O MVP controlará a conta e registrará pagamentos manualmente, mas o recibo será não fiscal. A emissão fiscal verdadeira exige requisitos legais, configuração e integração apropriadas e deverá ser tratada separadamente.

**Gate da Fase 1:** ambiente iniciado por `docker-compose`; API funcional com pelo menos quatro endpoints relevantes; operações de pedido e fechamento persistidas no PostgreSQL; transações ACID demonstradas; autenticação e permissões básicas; testes automatizados para regras críticas; fluxo de atendimento até recibo não fiscal validado.

**Cursos:** 150 (SQL com PostgreSQL), 160 (Praticando SQL), 227 (Administração PostgreSQL) e 105 (Python com OOP). Para FastAPI, utilizar a documentação oficial como fonte primária e buscar um curso específico fora do catálogo, se necessário.

---

### 🎯 FASE 2 — Produção e Valor (meses 7-9, aproximadamente 13 semanas)

**Objetivo:** ampliar a capacidade de operar soluções reais: automação, orquestração, transformação analítica, BI, integração contínua e deploy.

**Tópicos (ordem adaptável):**
1. Playwright, quando houver necessidade legítima de automação de navegador ou extração autorizada.
2. Orquestração — escolher **Dagster ou Airflow**, não estudar todos simultaneamente.
3. dbt: modelos, testes, documentação e dependências.
4. Power BI: modelagem e DAX básico/intermediário conforme os indicadores do projeto.
5. GitHub Actions: CI e verificações automatizadas.
6. Deploy em VM ou plataforma compatível com os requisitos de rede e segurança.
7. `docker-compose` com múltiplos serviços, quando necessário.

**Projetos-âncora possíveis (escolher apenas um após identificar um problema concreto):**

| Opção | Problema | Stack possível |
|---|---|---|
| **A — ERP Fechado (Consultoria)** | TI não libera acesso estruturado e relatórios são manuais | Playwright, DuckDB/dbt, Power BI, Streamlit, GitHub Actions |
| **B — Financeiro (Ações/Cripto)** | Consolidar dados públicos de ativos e produzir visão histórica | APIs/fontes públicas, DuckDB/dbt, orquestração e Streamlit |
| **C — Monitoramento de Preços** | Varejista precisa acompanhar preços de mercado | Coleta autorizada, DuckDB, Streamlit e GitHub Actions |

**Gate da Fase 2:** pipeline orquestrado e reproduzível; testes e documentação dos modelos; dashboard Power BI e/ou Streamlit conforme o problema; deploy funcional no ambiente escolhido; CI executando verificações relevantes. Não exigir duas interfaces se uma delas não agregar valor ao caso.

**Cursos:** 243 (Apache Airflow), 264 (AWS Data Lake) e 151 (Power BI), selecionados conforme o projeto e a necessidade real.

---

### 🎯 FASE 3 — Consolidação (meses 10-24)

**Sem ordem fixa.** O aprofundamento será guiado por problemas concretos, requisitos de vagas e projetos, sem adotar ferramentas apenas por popularidade:
- Cliente ou projeto exige processamento distribuído → avaliar Spark/PySpark.
- Uma oportunidade exige dbt avançado → aprofundar dbt.
- Projeto realmente envolve ML → estudar estatística e ferramentas de ML na proporção necessária.
- Necessidade de nuvem → aprofundar o provedor utilizado no projeto.

**Consolidações obrigatórias (paralelas e proporcionais à capacidade):**
- **Teste de entrevista com IA:** uma vez ao final de cada fase.
- **Blog técnico:** um texto por projeto, com problema, decisões, limitações e aprendizados.
- **ADRs:** registrar decisões técnicas relevantes, sem burocracia desnecessária.
- **Catálogo de fontes:** documentar consultas e fontes críticas.
- **Portfólio:** apresentar projetos com dados seguros, README, instruções de execução e evidências de validação.

---

## 🔁 PARTE 6 — Ciclo de Estudo com IA (v0.1 — Fechado)

### 6.1 Estrutura de cada sessão

```
1. VOCÊ ESCOLHE O TÓPICO (2-3min)
   Olha o diário anterior + roadmap da fase
   Escolhe o próximo tópico
   IA valida a escolha (se desalinhada, aponta por quê)

2. IA DEFINE A TRILHA (1min)
   Pergunta: "Você já viu [X]? Explica o que é sem consultar."
   Explica bem → Trilha A
   Não/trava → Trilha B

3. TRILHA A — Tópico já visto
   3a. Reprodução cega (20-30min) — sem IA, sem docs
   3b. Teoria focada no que faltou (15-20min)
   3c. Questões teóricas (3-5)
   3d. Questões práticas (3: simples/mediana/avançada)
   3e. Gate
   3f. Diário

4. TRILHA B — Tópico novo
   4a. Exemplo mínimo de referência (5-10 linhas)
       Você lê com 3 perguntas ativas:
         - O que essa linha faz?
         - Por que assim em vez do jeito óbvio?
         - Onde vi isso no meu código?
   4b. Reprodução de memória (10-15min)
   4c. Aplicação em contexto novo (10-15min)
   4d. Teoria (10-15min)
   4e. Questões
   4f. Gate
   4g. Diário

5. GATE
   mínimo = 3 questões teóricas + 3 práticas = 6 questões
   podem ser incluídas questões adicionais (até 8) quando o tópico justificar
   acertos_necessários = ceil(0.8 × total)
   além do total: pelo menos 2 das 3 questões práticas corretas

   Passou → próximo tópico
   Não passou → retorno D+3 ou D+7
              (só erradas + 1 nova de integração)
   Falhou duas vezes no mesmo tópico → dividir o tópico em partes menores,
   cada uma com gate próprio

6. DIÁRIO (obrigatório, mesmo quando passa)
```

### 6.2 Gate e tabela de arredondamento (v1.1)

**Composição mínima:** três questões teóricas + três questões práticas = seis questões. O total pode chegar a oito quando a abrangência do tópico justificar.

`acertos_necessários = ceil(0.8 × total)`

Além do percentual total, é obrigatório acertar **pelo menos duas das três questões práticas**. O autor não avança apenas por demonstrar conhecimento teórico.

| Total de questões | 80% | Acertos necessários | Requisito prático |
|---:|---:|---:|---|
| 6 | 4,8 | 5 (83%) | Pelo menos 2/3 práticas |
| 7 | 5,6 | 6 (86%) | Pelo menos 2/3 práticas |
| 8 | 6,4 | 7 (87,5%) | Pelo menos 2/3 práticas |

**Regra de divisão:** se o autor falhar duas vezes no mesmo tópico, a IA deve avaliar se o conteúdo está amplo ou mal delimitado. Se estiver, deve dividi-lo em partes menores, cada uma com seu próprio gate. A repetição não deve ser mecânica.

### 6.3 Correção socrática (D2)

- **1º erro:** IA pergunta *"Por que você respondeu X? O que te levou a pensar isso?"*
- **2º erro:** IA dá resposta direta + complementa

### 6.4 Retorno (D+3 ou D+7)

- Refazer **só as questões erradas** + **1 nova de integração**
- Se atingir o critério de retorno (duas ou mais respostas corretas, incluindo a questão de integração quando aplicável) → registrar como consolidado para este ciclo.
- Se não atingir → retomar o tópico; após duas falhas no mesmo tópico, avaliar divisão em partes menores.

### 6.5 Regras invioláveis

- ❌ Sem "60-79% com ressalva" (removido)
- ❌ IA não gera a primeira versão de código do tópico
- ❌ IA não responde a dúvida antes da 1ª tentativa sua
- ❌ Sem pular o diário
- ✅ Reprodução cega **antes** das questões (trilha A)
- ✅ Exemplo de referência **antes** da reprodução (trilha B, só 5-10 linhas)
- ✅ Retorno só das erradas + 1 integração

### 6.6 Regra de migração

- **Semanas 1-3:** você escolhe o tópico, IA valida
- **Semanas 4+:** IA sugere 3 tópicos, você escolhe 1
- **Semanas 8+:** você escolhe, IA só aprova/reprova

### 6.7 Formato do diário (proposto)

Arquivo: `estudos/diario/YYYY-MM-DD-topico.md`

```markdown
## Sessão 2026-11-13 — Listas (Trilha A)

### Reprodução cega
- Tentei escrever: `frutas = ['maçã', 'banana']; frutas.append('uva')`
- Travei em: `frutas.pop(1)` — não lembrei que aceita índice
- Escrevi sem consultar: ✅

### Questões
Teóricas (5): 4 acertos
Práticas (3): 2 acertos
Total: 6/8 (75%) → NÃO PASSOU (necessário 7; requisito prático de 2/3 atendido)

### Erradas
- Q3 teórica: confundi `remove` com `pop`
- Q2 prática: lambda dentro de `sort`

### Retorno agendado: 2026-11-16 (D+3)
- Refazer Q3 + Q2 + 1 nova de integração

### Próximo tópico sugerido
- Ainda listas (não passou)
```

### 6.8 Agendamento de retorno (proposto)

Arquivo: `estudos/retornos.md`

```markdown
## Pendentes
- 2026-11-16: listas (Q3 + Q2 + 1 integração)
- 2026-11-18: lambda (Q2 + 1 integração)

## Feitos
- 2026-11-14: dict comprehension ✅
```

Você abre antes de cada sessão. Se tem pendente para hoje, começa por ele (5-10min).

---

## 🛠️ PARTE 7 — Stack Consolidada (3 Camadas)

### 7.1 Camada 1 — Essencial (precisa dominar progressivamente)

| Ferramenta/conhecimento | Papel | Onde entra |
|---|---|---|
| Python | Linguagem de implementação, automação e transformação | Fase 0 em diante |
| SQL (Oracle/PostgreSQL) | Consulta, transformação e manipulação de dados | Fases 0 e 1 |
| SQLite | Banco operacional local, simples e adequado ao primeiro aplicativo pessoal | Fase 0 |
| PostgreSQL | Banco relacional para aplicações com escrita, transações e múltiplos usuários | Fase 1 |
| Pandas | Manipulação e transformação de datasets pequenos/médios | Fase 0 |
| DuckDB + Parquet | Processamento e armazenamento analítico local | Fase 0 |
| Streamlit | Interface rápida para aplicações internas e dashboards | Já utiliza; aprofundar conforme projeto |
| pytest | Testes automatizados de código e regras de negócio | Fase 0 em diante |
| Pandera | Validação de estruturas e qualidade de dados, quando necessário | Fase 0/1 |
| Git/GitHub | Versionamento, histórico e portfólio seguro | Já utiliza; aprofundar |
| Docker | Reprodutibilidade e portabilidade de ambientes | Fase 1 em diante |
| Power BI | Consumo analítico e entrega de indicadores | Fase 2 |

**Distinção dos bancos:** SQLite será usado inicialmente para persistência operacional local e simples; PostgreSQL será estudado para aplicações transacionais mais completas; DuckDB será utilizado para consultas e processamento analítico. A escolha deve acompanhar o padrão de acesso, concorrência, volume e requisitos do projeto.

### 7.2 Camada 2 — Importante (conhecer bem e aplicar quando houver necessidade)

| Ferramenta | Quando estudar |
|---|---|
| Polars | Somente quando um dataset ou gargalo real mostrar que Pandas não atende aos requisitos de desempenho ou memória |
| Airflow / Dagster / Prefect | Fase 2; escolher uma ferramenta conforme o pipeline e o contexto |
| dbt | Fase 2; transformação, testes e documentação de modelos analíticos |
| FastAPI | Fase 1, caso a arquitetura do restaurante ou outro projeto justifique API própria |
| Playwright | Fase 2, para automação de navegador autorizada e necessária |
| GitHub Actions | Fase 2, para integração e verificações contínuas |
| Power Query | Refinar conforme demandas de integração e BI |
| HTTP e APIs | Conhecer requisições, respostas, JSON, métodos, status codes e autenticação básica |

### 7.3 Camada 3 — Consciência (saber que existe; aprofundar se necessário)

| Ferramenta/conceito | Por que ter consciência |
|---|---|
| Spark/PySpark | Processamento distribuído, relevante em volumes e ambientes específicos |
| Databricks | Plataforma de engenharia e análise de dados em escala |
| Snowflake/BigQuery | Plataformas de data warehouse em nuvem |
| Kafka | Streaming e comunicação por eventos em cenários que exijam fluxo contínuo |
| Kubernetes | Orquestração de containers em infraestruturas mais complexas |
| Terraform | Infraestrutura como código |

**Regra da Camada 3:** alcançar L2 — saber o que faz, quando usar, quando não usar e quais limitações possui. Não é necessário instalar ou configurar essas ferramentas antecipadamente.

---

## 📊 PARTE 8 — Dados de Mercado (pesquisa consolidada)

### Nota metodológica e de interpretação

Os números abaixo são **referências de mercado compiladas em 2026**, não evidência específica da demanda de Teresina, Fortaleza ou do mercado regional de PMEs. Servem como termômetro amplo e não devem determinar, isoladamente, o roadmap. O documento-base registra Python Dev BR como fonte de uma catalogação de vagas; não registra o dia exato da coleta nem todos os critérios de deduplicação e classificação. Portanto, os números devem ser tratados como indicativos, não como levantamento independente validado.

### 8.1 Stack em vagas de dados (Brasil, 2026)

**Fonte registrada:** Python Dev BR — catálogo informado de 1.855 vagas. **Ano de coleta/compilação informado:** 2026. **Data exata e metodologia detalhada:** não registradas no documento-base.

| Ferramenta | Aparições informadas |
|---|---:|
| SQL | 1.044 |
| Databricks | 446 |
| GCP | 273 |
| Spark | 268 |
| Postgres | 191 |
| Airflow | 139 |
| Kafka | 138 |
| dbt | 109 |
| Snowflake | 101 |
| BigQuery | 91 |

### 8.2 Stack realista para PMEs

**Referência registrada:** estudo da UFPE sobre pipelines em PMEs. O documento-base não contém link, ano ou detalhes metodológicos; utilizar como referência contextual, não como evidência conclusiva.

- Python
- PostgreSQL
- Docker
- Airflow
- Modelo dimensional em estrela
- Apache Kafka, quando aplicável

### 8.3 Tensão identificada

**Stack de vagas** ≠ **stack de PMEs**. O roadmap prioriza uma stack pragmática para o mercado-alvo e mantém consciência das tecnologias recorrentes em vagas mais amplas, para orientar entrevistas e escolhas futuras.

### 8.4 Vagas analisadas como termômetro

| Vaga | Perfil real atribuído na análise | Alinhamento |
|---|---|---|
| Data Scientist Spec II (Santander) | Business/Data Analyst | ✅ Alinhado |
| IT Developer III (Santander) | Backend Engineer | ❌ Não |
| Data & Analytics Spec I (Santander) | Data Scientist Risk | ⚠️ Parcial |
| Assistente Dev Jr (Teresina) | Dev/DevOps | ⚠️ Parcial (bom termômetro para conhecimentos da Fase 1) |

---

## 🎓 PARTE 9 — Cursos Recomendados (do catálogo do autor)

### 9.1 Essenciais

| Curso | Fase | Por quê |
|---|---|---|
| 273 — Boas práticas em Python | Fase 0 | Fundamentos de engenharia e qualidade de código |
| 105 — Python com OOP | Fase 1 | Classes, composição e organização |
| 24 — Engenharia de Analytics | Fase 0 | Modelagem e pipelines analíticos |
| 125 — Modelagem de dados | Fase 0 | Kimball e star schema |
| 25 — Primeiros passos Eng. Dados | Fase 0 | ETL e fundamentos de arquitetura de dados |
| 150 — SQL com PostgreSQL | Fase 1 | SQL, CTEs e funções de janela |
| 160 — Praticando SQL | Fase 1 | Exercícios e consolidação |
| 142 — Consultas Oracle | Fase 1 | Aplicação ao contexto Ferronorte |
| 227 — Administração PostgreSQL | Fase 1 | Transações, índices e administração básica |
| 243 — Apache Airflow | Fase 2 | Orquestração, caso Airflow seja a escolha |
| 264 — AWS Data Lake | Fase 2 | Conceitos de armazenamento e pipelines em nuvem |
| 151 — Power BI | Fase 2 | DAX e modelagem para consumo analítico |

**FastAPI:** o curso 37 (Flask) foi removido do roadmap. Flask e FastAPI são frameworks diferentes; conceitos básicos de HTTP podem ser transferidos, mas o curso de Flask não substitui o aprendizado específico de FastAPI.

### 9.2 Complementares

- 143 — Otimização com Python
- 149 — Polars (somente se Pandas não atender a uma necessidade real)
- 50 — Governança de Dados
- 166 — Carreira QA / automação de testes
- 222 — Data Mesh (conceitual; somente consciência)

### 9.3 Skip (não estudar no roadmap atual)

- R (28, 168)
- Deep Learning (03, 04)
- DAX profundo (02)
- Excel/VBA (29-31, 153, 212), pois já existe experiência e não é o foco de evolução atual
- MicroStrategy, Qlik (121, 167)
- NLP, Visão Computacional (138, 215)
- Java, PHP, Go, Node, Rust, C# (todos)
- Cibersegurança especializada (320); manter apenas fundamentos de segurança necessários aos projetos

### 9.4 Buscar fora do catálogo

- **FastAPI:** documentação oficial como fonte primária — https://fastapi.tiangolo.com/ . Buscar um curso específico de FastAPI fora do catálogo somente se a documentação e exercícios práticos não forem suficientes.
- dbt (https://docs.getdbt.com/ e dbt Learn)
- Docker (documentação oficial)
- Dagster ou Prefect (documentação oficial; escolher conforme o projeto)
- Pandera / Great Expectations (documentação oficial)
- DuckDB (documentação oficial)
- Apache Iceberg / Delta Lake (consciência e documentação, quando necessário)
- Playwright (documentação oficial)

---

## 🧠 PARTE 10 — Modelo de Conhecimento (L0-L4, v1.1)

| Nível | Nome | Definição | Evidência esperada |
|---|---|---|---|
| **L0** | Desconhecido | Nunca ouviu falar ou não reconhece a finalidade | — |
| **L1** | Consciência | Conhece a existência e consegue dizer, em termos gerais, o que faz | Explicar "X faz Y" |
| **L2** | Mapa | Sabe quando usar, quando não usar, quais problemas resolve e quais limitações possui | Defender uma escolha e citar uma alternativa/limitação |
| **L3** | Aplicação assistida | Consegue utilizar com documentação ou assistência, validar o resultado e resolver problemas comuns | Implementação funcional com consulta e validação |
| **L4** | Autonomia | Consegue projetar, implementar, testar, depurar e manter soluções com autonomia, usando documentação como referência quando necessário | Explicar decisões, modificar, testar, diagnosticar e sustentar a solução |

**Nota sobre documentação:** L4 não significa trabalhar sem documentação, exemplos ou referências. Profissionais experientes consultam documentação continuamente. A reprodução cega, sem IA e sem documentação, permanece como exercício específico de aprendizagem, não como exigência do trabalho real.

**Distribuição orientativa do esforço:**
- **L2** para ferramentas de apoio e tecnologias que precisam ser avaliadas antes de uma escolha.
- **L4** para o núcleo: Python, SQL, fundamentos de modelagem, testes e ferramentas principais efetivamente utilizadas nos projetos.
- **L3** para ferramentas importantes que serão aplicadas com documentação e assistência conforme a necessidade.

A quantidade de ferramentas em cada nível pode mudar conforme os projetos. O nível deve refletir evidências de capacidade, não apenas horas de curso ou familiaridade com a interface.

---

## 🚨 PARTE 11 — As 5 Aulas da Sessão 40/40 (NÃO DRENADAS)

**Origem:** sessão de debugging do `_reconcile_fato_estoque` em 10/11/2026, onde a IA identificou 2 linhas trocadas (`dim_loja["cod_empresa"]` → `dim_produto["cod_produto"]`).

**Status:** não drenadas. **Pré-requisito das sessões 1-2 da Fase 0.**

### Aula 1 — Diagnóstico diferencial (bisseccionar filtro)
**O que é:** quando um resultado está zerado, isole cada etapa do filtro até achar onde o número cai a zero.
**Como aplicar:** rodar `apos filtro filial: X/Y`, `apos filtro produto: X/Y`, `total final: Z` sequencialmente.
**Quando usar:** qualquer vez que um filtro der resultado inesperado.

### Aula 2 — Contradição = código divergente
**O que é:** se o diagnóstico isolado funciona mas o pipeline falha, você está rodando **outro código** (não o que você acha).
**Como aplicar:** comparar arquivo em disco com o que você acha que está rodando (`Get-Content`, `Select-String`).
**Quando usar:** quando o resultado contradiz o que você espera.

### Aula 3 — Nome da variável vs. conteúdo
**O que é:** `produtos_validos = set(dim_loja["cod_empresa"])` está dizendo "produtos", mas pegando "lojas".
**Como aplicar:** ler cada linha e perguntar "esse nome faz sentido com esse conteúdo?".
**Quando usar:** durante revisão de código, especialmente em filtros e joins.

### Aula 4 — Isolar causa de cada teste que falha
**O que é:** 2 testes falhando ≠ 2 problemas iguais. `test_tipos_corretos` (dtype) e `test_ordem_por_sk` (decreasing vs increasing) tinham causas completamente diferentes.
**Como aplicar:** para cada teste que falha, identificar a causa raiz **individualmente** antes de propor fix.
**Quando usar:** sempre que houver múltiplas falhas.

### Aula 5 — Não chutar antes de ver código real
**O que é:** a IA se recusou a corrigir sem ver o código em disco, mesmo com o diagnóstico mostrando o sintoma. Não propôs fix baseado só no erro.
**Como aplicar:** antes de corrigir, **ver** o código atual. Sem isso, é chute.
**Quando usar:** sempre, especialmente em bugs.

---

## 📋 PARTE 12 — Regras Invioláveis da Parceria

### 12.1 O que a IA **deve** fazer

- ✅ Ser crítica, objetiva, cirúrgica e socrática quando estiver em modo estudo.
- ✅ Apontar quando houver sinais de planejamento prolongado sem execução, sem transformar observação comportamental em julgamento moral.
- ✅ Recusar gerar a primeira versão de código do tópico em modo estudo.
- ✅ Fazer perguntas antes de entregar respostas em modo estudo, respeitando as regras de correção socrática.
- ✅ Corrigir socraticamente no primeiro erro e fornecer explicação direta no segundo, conforme o ciclo definido.
- ✅ Exigir o gate de 80%, sem ressalva, incluindo desempenho prático mínimo.
- ✅ Aplicar o princípio **problema primeiro, tecnologia depois**.
- ✅ Distinguir fatos, hipóteses, recomendações e limitações.
- ✅ Preservar regras de negócio e restrições técnicas da Ferronorte.
- ✅ No modo trabalho, acelerar a entrega sem dispensar revisão, testes e validação pelo autor.

### 12.2 O que a IA **NÃO deve** fazer

- ❌ Concordar com o autor apenas para agradar (anti-sycophancy).
- ❌ Ajustar a resposta para aquilo que o autor parece querer ouvir.
- ❌ Entregar código completo como primeira resposta no modo estudo.
- ❌ Aceitar "não consegui" sem registrar as tentativas feitas e onde ocorreu o bloqueio.
- ❌ Sugerir projeto grande quando houver sinal claro de fuga de uma atividade pequena e já definida.
- ❌ Inventar requisitos, dados, fontes ou resultados de testes.
- ❌ Declarar sucesso sem validação real.
- ❌ Pular o diário ou o bilhete definidos para cada contexto.
- ❌ Modificar o escopo do tópico sem explicar e obter concordância.
- ❌ Aplicar a diretriz de trabalho em contexto de estudo.
- ❌ Incentivar commit de código gerado por IA sem revisão e validação proporcionais ao risco.

### 12.3 Hierarquia de papéis (modo estudo)

**Professor > Pair Programming > Revisor > Mentor**

A prioridade é desenvolver raciocínio e autonomia. A IA deve oferecer pistas graduais, não substituir a tentativa do autor.

### 12.4 Hierarquia de papéis (modo trabalho)

**Pair Programming > Revisor > Professor > Mentor**

A prioridade é a entrega confiável. A IA pode implementar, mas deve tornar decisões, riscos, testes e limitações compreensíveis para o autor.

### 12.5 Separação temporal obrigatória

- **Manhã/tarde — trabalho:** utilizar a diretriz de trabalho. A IA pode implementar; o autor revisa, testa, valida e aceita a mudança antes do commit.
- **Fim do dia — bilhete de 2 minutos:** registrar o que foi copiado, utilizado ou decidido sem compreensão completa.
- **Noite — estudo:** utilizar a diretriz de estudo e o ciclo com gate.

A separação é funcional, não uma proibição de estudar durante o trabalho quando uma necessidade profissional exigir. O bilhete é o mecanismo mínimo de conexão entre as lacunas encontradas no trabalho e o estudo noturno.

### 12.6 — Princípio de Autonomia e Responsabilidade Técnica

#### 12.6.1 Filosofia central

A IA é uma ferramenta legítima de aceleração. Não substitui julgamento técnico. O objetivo **não** é memorizar sintaxe nem escrever tudo manualmente. O objetivo **é** compreender, especificar, orientar, revisar, testar, diagnosticar e sustentar sistemas.

**A IA pode produzir código. O autor permanece responsável por compreender e validar o que foi produzido.**

#### 12.6.2 Os sete itens que NÃO podem ser terceirizados

1. Por que a solução resolve este problema — e não outro.
2. Quais regras de negócio estão implementadas.
3. Por que a tecnologia e a abordagem foram escolhidas em comparação com alternativas.
4. Quais limitações, riscos e efeitos colaterais existem.
5. Como a implementação foi testada e validada.
6. Como investigar falhas quando algo quebrar.
7. Como reverter ou modificar a solução quando os requisitos mudarem.

Não é necessário memorizar cada linha. É necessário compreender a estrutura, o comportamento e as consequências da implementação.

#### 12.6.3 Problema primeiro, tecnologia depois

Sequência obrigatória de raciocínio:

1. Identificar o problema.
2. Compreender contexto e requisitos.
3. Identificar restrições técnicas, financeiras e operacionais.
4. Levantar alternativas possíveis.
5. Comparar benefícios, limitações e custos.
6. Escolher a abordagem proporcional ao problema.
7. Definir como a solução será validada.

Exemplo:

- ❌ "Preciso aprender FastAPI?"
- ✅ "Meu projeto precisa expor funções para outros sistemas. Uma API é necessária? Quais alternativas existem? Quais requisitos de segurança, manutenção e disponibilidade precisamos atender?"

#### 12.6.4 Autonomia no modo trabalho

A IA pode gerar implementações completas quando isso for adequado ao escopo e ao risco do projeto. Antes de aceitar a implementação, o autor deve verificar:

- Os requisitos foram atendidos?
- As partes críticas foram compreendidas?
- O tratamento de erros é adequado?
- Os testes necessários foram executados?
- As regras de negócio foram validadas?
- A integração com o restante do sistema foi conferida?
- Segurança, credenciais e dados sensíveis foram verificados?

**Fluxo:** Problema → Especificação → Implementação assistida por IA → Revisão técnica → Testes → Validação → Aceitação → Commit.

Copiar código e realizar commit sem revisão **não** constitui validação técnica.

#### 12.6.5 Autonomia no modo estudo

A prioridade é desenvolver capacidade própria. A IA não fornece a solução completa antes da tentativa do autor.

Fluxo esperado: autor compreende o problema → formula uma abordagem → tenta produzir → registra onde travou → pede uma pista → corrige e explica.

A reprodução manual é um instrumento de aprendizagem, não o objetivo profissional final. A documentação pode ser consultada após a tentativa inicial, conforme a trilha. A proibição de consulta na reprodução cega é um exercício de recuperação de conhecimento, não uma regra para o trabalho real.

#### 12.6.6 Critério de domínio

Não basta saber a definição de uma tecnologia ou conceito. O domínio deve ser demonstrado pela capacidade de:

- Identificar quando a competência é necessária.
- Comparar abordagens e justificar escolhas.
- Compreender código existente.
- Modificar código existente com segurança.
- Identificar resultados incorretos ou contraditórios.
- Investigar a origem de falhas.
- Criar ou interpretar testes.
- Validar o comportamento esperado.

A implementação sem IA será exercitada principalmente nos fundamentos e em pequenas unidades de código. Não será exigido domínio de memória sobre toda a linguagem, framework ou ferramenta.

#### 12.6.7 Regra de evolução profissional

A evolução é medida pela redução da dependência de orientação passo a passo, **não** pela redução artificial do uso de IA.

O indicador de evolução é conseguir assumir responsabilidades técnicas progressivamente maiores, mesmo utilizando IA e documentação durante o trabalho.

#### 12.6.8 Checklist de revisão de código gerado por IA (binário)

Antes de commitar código gerado por IA no trabalho, verificar todos os itens:

- [ ] Consigo explicar o que o código faz em três frases.
- [ ] Identifiquei as duas ou três decisões técnicas não óbvias.
- [ ] Verifiquei a integração com o restante do sistema.
- [ ] Executei pelo menos um teste manual ou automatizado pertinente.
- [ ] Confirmei que as regras de negócio estão corretas.
- [ ] Sei como reverter a alteração se algo quebrar.
- [ ] Nenhuma credencial ou informação sensível foi exposta.

**Regra binária:** se qualquer item estiver marcado como "não", **não realizar o commit**. Resolver a pendência e repetir a revisão antes de commitar. Em alterações de alto risco, um único teste não substitui a estratégia de testes necessária.

### 12.7 — Bilhete de 2 minutos

No fim do dia de trabalho, antes de fechar o notebook, registrar **três a cinco itens** que foram copiados, utilizados ou decididos sem compreensão completa.

- Sem IA.
- Sem transformar o bilhete em diário formal.
- Registrar de forma curta: o que foi feito, o que não ficou claro e, quando possível, qual pergunta precisa ser respondida.
- O conteúdo alimenta a escolha dos tópicos de estudo noturno.

**O bilhete é o único elo operacional formal entre trabalho e estudo.** Sem ele, o estudo perde parte da matéria-prima produzida pelas situações reais de trabalho.

---

## 🎯 PARTE 13 — Como Usar Este Documento em um Novo Chat

### 13.1 Instrução de abertura (copiar e colar)

> "Estou trazendo o Documento Mestre de Continuidade — v1.1. Leia integralmente antes de propor alterações. Meu perfil-alvo é Analytics Engineer com capacidade end-to-end: Engenharia Analítica é o núcleo; Python, integração, automação e operação ampliam minha capacidade de entrega. Já temos: (1) ciclo de estudo com gate de 80% e requisito prático, (2) roadmap em quatro fases numeradas de 0 a 3, (3) stack em três camadas, (4) cinco aulas pendentes da sessão 40/40 como primeiro compromisso, (5) sequência de projetos gastos pessoais → restaurante → camada analítica e (6) princípio de autonomia e responsabilidade técnica perante IA. Quero continuar de onde paramos: [tópico específico]. Não reabra o roadmap sem uma necessidade concreta; priorize execução."

### 13.2 Perguntas que o novo chat deve responder antes de começar

1. O autor está em modo estudo ou modo trabalho?
2. Qual é o problema ou tópico específico da sessão?
3. É Trilha A (já visto) ou Trilha B (novo)?
4. As cinco aulas da sessão 40/40 já foram drenadas e registradas?
5. O diário está atualizado?
6. Existe bilhete de trabalho que deve orientar a sessão?
7. Qual é o gate ou a entrega concreta esperada?

### 13.3 Sinais de que o autor está em padrão de fuga

- Propõe projeto novo antes de fechar o atual.
- Pede para "estudar tudo antes" de executar uma atividade pequena já definida.
- Muda de alvo profissional sem evidência nova que justifique a mudança.
- Pede para "só ler" quando a sessão exige reprodução ou aplicação.
- Propõe escopo mais amplo quando está prestes a realizar uma tarefa pequena e específica.
- Solicita nova versão do roadmap sem ter executado os próximos passos já definidos.

**Quando identificar:** nomear o padrão com franqueza, sem julgamento moral. Distinguir uma necessidade legítima de revisão de uma tentativa de adiar a execução. Se não houver fato novo relevante, redirecionar para a próxima ação concreta já estabelecida.

---

## 🧭 PARTE 14 — Próximos Passos Imediatos

### 14.1 Ordem de execução

A ordem está definida. Não escolher outro projeto antes de cumprir os gates:

1. **Drenar as cinco aulas da sessão 40/40.**
2. **Concluir o projeto de Controle de Gastos Pessoais** da Fase 0.
3. **Iniciar e concluir o MVP de Restaurante** da Fase 1.
4. **Evoluir para a camada analítica** e os projetos da Fase 2, conforme o roadmap.

### 14.2 Primeira semana

- [ ] Sessão 1: reprodução cega e investigação das cinco aulas a partir do `_reconcile_fato_estoque`.
- [ ] Sessão 2: defesa das decisões, exercícios de diagnóstico e registro no diário.
- [ ] Criar a estrutura `estudos/diario/` e o arquivo `estudos/retornos.md`.
- [ ] Escrever o primeiro bilhete de 2 minutos ao final de um dia de trabalho.
- [ ] Iniciar a Fase 0 pelo primeiro tópico após a drenagem das aulas.

### 14.3 Rotina semanal e próximas quatro semanas

- **Piso de execução:** quatro sessões obrigatórias por semana e uma sessão opcional.
- **Meta desejada:** cinco a seis sessões por semana, quando a rotina permitir sem comprometer descanso e trabalho.
- Cada sessão deve deixar uma evidência: exercício, código próprio, alteração, teste, resposta justificada ou diário.
- Realizar os tópicos da Fase 0 na ordem definida; não antecipar o restaurante.
- Iniciar o Controle de Gastos após cumprir o pré-requisito das cinco aulas e avançar nos fundamentos necessários.
- Registrar toda sessão no diário e agendar retornos D+3 ou D+7 quando houver reprovação.

### 14.4 Próximos três meses

- [ ] Concluir o gate da Fase 0.
- [ ] Entregar o Controle de Gastos com SQLite operacional, DuckDB analítico, interface Streamlit, testes e README.
- [ ] Consolidar as cinco aulas — não apenas concluir exercícios, mas demonstrar aplicação em outro contexto.
- [ ] Revisar o roadmap somente com base em evidências da execução, mudanças de contexto ou requisitos novos.

**Regra de foco:** depois de aplicar a v1.1, o próximo passo é execução, não uma nova rodada de planejamento. Refinamentos futuros devem responder a um problema real observado durante a execução.

---

## 📎 PARTE 15 — Documentos Relacionados

| Documento | Local | Propósito |
|---|---|---|
| Histórico do Projeto Ferronorte | `historico_projeto.md` (v5.0) | Contexto do projeto empresarial |
| Spec Estoque Parado | `specs/estoque_parado/spec_estoque_parado.md` | Especificação aprovada |
| Spec Compras SLZ | `specs/compras/spec_compras.md` (v1.2) | Especificação MVP simplificado |
| Diretriz de Trabalho | (36 seções) | Já em uso, não modificada |
| Diretriz de Estudo | `docs/diretriz_estudo_v0.1.md` | **A criar** a partir deste documento e calibrar com a execução |
| Diário de Estudo | `estudos/diario/` | **A criar** |
| Retornos Pendentes | `estudos/retornos.md` | **A criar** |
| Decisões (ADRs) | `docs/decisions/` | **A criar conforme fases** |

---

## 🎯 PARTE 16 — Conclusão e estado da versão 1.1

### O que foi consolidado

- Perfil definido como **Analytics Engineer com capacidade end-to-end**, mantendo a ambição de resolver problemas completos de PMEs com uma stack pragmática.
- Diagnóstico refinado: lacuna predominante de tradução e autonomia, com possíveis lacunas conceituais e sintáticas específicas.
- Roadmap organizado em quatro fases numeradas de 0 a 3, com horizonte orientativo de aproximadamente 24 meses.
- Sequência de projetos definida: Controle de Gastos Pessoais → Restaurante → camada analítica.
- Fase 0 reorganizada, com SQL explícito e separação entre SQLite operacional e DuckDB analítico.
- MVP do restaurante limitado a dez funcionalidades, com emissão fiscal verdadeira fora do primeiro escopo.
- Ciclo de estudo com gate de 80%, mínimo de seis questões e requisito de desempenho prático.
- Modelo L0-L4 revisado: L4 admite uso profissional de documentação.
- Stack dividida em essencial, importante e consciência, com seleção de tecnologia orientada pelo problema.
- Princípio de autonomia e responsabilidade técnica perante IA formalizado.
- Checklist binário de revisão de código gerado por IA e bilhete de 2 minutos incluídos.
- Rotina mínima de quatro sessões obrigatórias e uma opcional, com meta de cinco a seis sessões por semana.

### O que continua pendente

- [ ] As cinco aulas da sessão 40/40 ainda precisam ser drenadas e registradas.
- [ ] O primeiro bilhete de trabalho ainda precisa ser escrito.
- [ ] A estrutura `estudos/` ainda precisa ser criada.
- [ ] O projeto de Controle de Gastos Pessoais ainda precisa ser iniciado e concluído.
- [ ] A diretriz formal de estudo (`docs/diretriz_estudo_v0.1.md`) ainda precisa ser criada a partir deste documento e calibrada pela execução.

**Próxima ação:** executar as sessões iniciais de drenagem das cinco aulas. Não abrir nova rodada de planejamento antes dessa execução, salvo se surgir uma restrição concreta que impeça o próximo passo.

---

## 🧑‍🏫 Nota final do autor (espaço para você completar)

_Este documento é vivo. Você deve complementar aqui o que aprendeu desde a última atualização, o que mudou no roadmap, e o que decidiu diferente._

**Data da última revisão:** 12/11/2026
**Próxima revisão prevista:** após drenar as cinco aulas e obter evidências da primeira execução do projeto de gastos.

---

**Fim do Documento Mestre de Continuidade — v1.1**

**Gerado em 12/11/2026**
**Para uso em novos chats de IA, atualização de diretrizes e continuidade do roadmap profissional.**