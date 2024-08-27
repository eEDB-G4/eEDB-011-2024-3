WITH raw_complaints AS (
SELECT * fROM {{ref('raw_complaints')}}
)

SELECT

CAST(`Ano`	                                              AS INTEGER ) AS ano                                       ,    
CAST(`Trimestre`                                          AS STRING  ) AS trimestre                                 ,
CAST(`Categoria`                                          AS STRING  ) AS categoria                                 ,
CAST(`Tipo`	                                              AS STRING  ) AS tipo                                      ,
CAST(`CNPJ IF`	                                          AS STRING  ) AS cnpj_if                                   ,
CAST(`Instituicao financeira`	                          AS STRING  ) AS instituicao_financeira                    ,
CAST(`Índice`	                                          AS STRING  ) AS indice                                    ,
CAST(`Quantidade de reclamacoes reguladas - outras`	      AS INTEGER ) AS quantidade_de_reclamacoes_reguladas_outras,
CAST(`Quantidade de reclamacoes nao reguladas`	          AS INTEGER ) AS quantidade_de_reclamacoes_nao_reguladas   ,
CAST(`Quantidade total de reclamacoes`	                  AS INTEGER ) AS quantidade_total_de_reclamacoes           ,
CAST(`Quantidade total de clientes – CCS e SCR`	          AS STRING  ) AS quantidade_total_de_clientes_ccs_scr      ,
CAST(`Quantidade de clientes – CCS`	                  	  AS STRING  ) AS quantidade_de_clientes_ccs                ,
CAST(`Quantidade de clientes – SCR`                       AS STRING  ) AS quantidade_de_clientes_scr                

FROM schema.2021_tri_01

UNION all

SELECT

CAST(`Ano`	                                              AS INTEGER ) AS ano                                       ,    
CAST(`Trimestre`                                          AS STRING  ) AS trimestre                                 ,
CAST(`Categoria`                                          AS STRING  ) AS categoria                                 ,
CAST(`Tipo`	                                              AS STRING  ) AS tipo                                      ,
CAST(`CNPJ IF`	                                          AS STRING  ) AS cnpj_if                                   ,
CAST(`Instituicao financeira`	                          AS STRING  ) AS instituicao_financeira                    ,
CAST(`Índice`	                                          AS STRING  ) AS indice                                    ,
CAST(`Quantidade de reclamacoes reguladas - outras`	      AS INTEGER ) AS quantidade_de_reclamacoes_reguladas_outras,
CAST(`Quantidade de reclamacoes nao reguladas`	          AS INTEGER ) AS quantidade_de_reclamacoes_nao_reguladas   ,
CAST(`Quantidade total de reclamacoes`	                  AS INTEGER ) AS quantidade_total_de_reclamacoes           ,
CAST(`Quantidade total de clientes – CCS e SCR`	          AS STRING  ) AS quantidade_total_de_clientes_ccs_scr      ,
CAST(`Quantidade de clientes – CCS`	                  	  AS STRING  ) AS quantidade_de_clientes_ccs                ,
CAST(`Quantidade de clientes – SCR`                       AS STRING  ) AS quantidade_de_clientes_scr                

FROM schema.2021_tri_02
UNION all

SELECT

CAST(`Ano`	                                              AS INTEGER ) AS ano                                       ,    
CAST(`Trimestre`                                          AS STRING  ) AS trimestre                                 ,
CAST(`Categoria`                                          AS STRING  ) AS categoria                                 ,
CAST(`Tipo`	                                              AS STRING  ) AS tipo                                      ,
CAST(`CNPJ IF`	                                          AS STRING  ) AS cnpj_if                                   ,
CAST(`Instituicao financeira`	                          AS STRING  ) AS instituicao_financeira                    ,
CAST(`Índice`	                                          AS STRING  ) AS indice                                    ,
CAST(`Quantidade de reclamacoes reguladas - outras`	      AS INTEGER ) AS quantidade_de_reclamacoes_reguladas_outras,
CAST(`Quantidade de reclamacoes nao reguladas`	          AS INTEGER ) AS quantidade_de_reclamacoes_nao_reguladas   ,
CAST(`Quantidade total de reclamacoes`	                  AS INTEGER ) AS quantidade_total_de_reclamacoes           ,
CAST(`Quantidade total de clientes – CCS e SCR`	          AS STRING  ) AS quantidade_total_de_clientes_ccs_scr      ,
CAST(`Quantidade de clientes – CCS`	                  	  AS STRING  ) AS quantidade_de_clientes_ccs                ,
CAST(`Quantidade de clientes – SCR`                       AS STRING  ) AS quantidade_de_clientes_scr                

FROM schema.2021_tri_03
UNION all

SELECT

CAST(`Ano`	                                              AS INTEGER ) AS ano                                       ,    
CAST(`Trimestre`                                          AS STRING  ) AS trimestre                                 ,
CAST(`Categoria`                                          AS STRING  ) AS categoria                                 ,
CAST(`Tipo`	                                              AS STRING  ) AS tipo                                      ,
CAST(`CNPJ IF`	                                          AS STRING  ) AS cnpj_if                                   ,
CAST(`Instituicao financeira`	                          AS STRING  ) AS instituicao_financeira                    ,
CAST(`Índice`	                                          AS STRING  ) AS indice                                    ,
CAST(`Quantidade de reclamacoes reguladas - outras`	      AS INTEGER ) AS quantidade_de_reclamacoes_reguladas_outras,
CAST(`Quantidade de reclamacoes nao reguladas`	          AS INTEGER ) AS quantidade_de_reclamacoes_nao_reguladas   ,
CAST(`Quantidade total de reclamacoes`	                  AS INTEGER ) AS quantidade_total_de_reclamacoes           ,
CAST(`Quantidade total de clientes – CCS e SCR`	          AS STRING  ) AS quantidade_total_de_clientes_ccs_scr      ,
CAST(`Quantidade de clientes – CCS`	                  	  AS STRING  ) AS quantidade_de_clientes_ccs                ,
CAST(`Quantidade de clientes – SCR`                       AS STRING  ) AS quantidade_de_clientes_scr                

FROM schema.2021_tri_04

UNION all

SELECT

CAST(`Ano`	                                              AS INTEGER ) AS ano                                       ,    
CAST(`Trimestre`                                          AS STRING  ) AS trimestre                                 ,
CAST(`Categoria`                                          AS STRING  ) AS categoria                                 ,
CAST(`Tipo`	                                              AS STRING  ) AS tipo                                      ,
CAST(`CNPJ IF`	                                          AS STRING  ) AS cnpj_if                                   ,
CAST(`Instituicao financeira`	                          AS STRING  ) AS instituicao_financeira                    ,
CAST(`Índice`	                                          AS STRING  ) AS indice                                    ,
CAST(`Quantidade de reclamacoes reguladas - outras`	      AS INTEGER ) AS quantidade_de_reclamacoes_reguladas_outras,
CAST(`Quantidade de reclamacoes nao reguladas`	          AS INTEGER ) AS quantidade_de_reclamacoes_nao_reguladas   ,
CAST(`Quantidade total de reclamacoes`	                  AS INTEGER ) AS quantidade_total_de_reclamacoes           ,
CAST(`Quantidade total de clientes – CCS e SCR`	          AS STRING  ) AS quantidade_total_de_clientes_ccs_scr      ,
CAST(`Quantidade de clientes – CCS`	                  	  AS STRING  ) AS quantidade_de_clientes_ccs                ,
CAST(`Quantidade de clientes – SCR`                       AS STRING  ) AS quantidade_de_clientes_scr                

FROM schema.2022_tri_01

UNION all

SELECT

CAST(`Ano`	                                              AS INTEGER ) AS ano                                       ,    
CAST(`Trimestre`                                          AS STRING  ) AS trimestre                                 ,
CAST(`Categoria`                                          AS STRING  ) AS categoria                                 ,
CAST(`Tipo`	                                              AS STRING  ) AS tipo                                      ,
CAST(`CNPJ IF`	                                          AS STRING  ) AS cnpj_if                                   ,
CAST(`Instituicao financeira`	                          AS STRING  ) AS instituicao_financeira                    ,
CAST(`Índice`	                                          AS STRING  ) AS indice                                    ,
CAST(`Quantidade de reclamacoes reguladas - outras`	      AS INTEGER ) AS quantidade_de_reclamacoes_reguladas_outras,
CAST(`Quantidade de reclamacoes nao reguladas`	          AS INTEGER ) AS quantidade_de_reclamacoes_nao_reguladas   ,
CAST(`Quantidade total de reclamacoes`	                  AS INTEGER ) AS quantidade_total_de_reclamacoes           ,
CAST(`Quantidade total de clientes – CCS e SCR`	          AS STRING  ) AS quantidade_total_de_clientes_ccs_scr      ,
CAST(`Quantidade de clientes – CCS`	                  	  AS STRING  ) AS quantidade_de_clientes_ccs                ,
CAST(`Quantidade de clientes – SCR`                       AS STRING  ) AS quantidade_de_clientes_scr                

FROM schema.2022_tri_03

UNION all

SELECT

CAST(`Ano`	                                              AS INTEGER ) AS ano                                       ,    
CAST(`Trimestre`                                          AS STRING  ) AS trimestre                                 ,
CAST(`Categoria`                                          AS STRING  ) AS categoria                                 ,
CAST(`Tipo`	                                              AS STRING  ) AS tipo                                      ,
CAST(`CNPJ IF`	                                          AS STRING  ) AS cnpj_if                                   ,
CAST(`Instituicao financeira`	                          AS STRING  ) AS instituicao_financeira                    ,
CAST(`Índice`	                                          AS STRING  ) AS indice                                    ,
CAST(`Quantidade de reclamacoes reguladas - outras`	      AS INTEGER ) AS quantidade_de_reclamacoes_reguladas_outras,
CAST(`Quantidade de reclamacoes nao reguladas`	          AS INTEGER ) AS quantidade_de_reclamacoes_nao_reguladas   ,
CAST(`Quantidade total de reclamacoes`	                  AS INTEGER ) AS quantidade_total_de_reclamacoes           ,
CAST(`Quantidade total de clientes – CCS e SCR`	          AS STRING  ) AS quantidade_total_de_clientes_ccs_scr      ,
CAST(`Quantidade de clientes – CCS`	                  	  AS STRING  ) AS quantidade_de_clientes_ccs                ,
CAST(`Quantidade de clientes – SCR`                       AS STRING  ) AS quantidade_de_clientes_scr                

FROM schema.2022_tri_04