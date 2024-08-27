WITH raw_employees AS (
SELECT * fROM {{ref('raw_employees')}}
)

SELECT 

CAST(`employer_name`                   AS STRING  ) AS employer_name                   ,
CAST(`reviews_count`                   AS INTEGER ) AS reviews_count                   ,
CAST(`culture_count`                   AS INTEGER ) AS culture_count                   ,
CAST(`salaries_count`                  AS INTEGER ) AS salaries_count                  ,
CAST(`benefits_count`                  AS INTEGER ) AS benefits_count                  ,
CAST(`employer-website`                AS STRING  ) AS employer_website                ,
CAST(`employer-headquarters`           AS STRING  ) AS employer_headquarters           ,
CAST(`employer-founded`                AS DECIMAL ) AS employer_founded                ,
CAST(`employer-industry`               AS STRING  ) AS employer_industry               ,
CAST(`employer-revenue`                AS STRING  ) AS employer_revenue                ,
CAST(`url`                             AS STRING  ) AS url                             ,
CAST(`Geral`                           AS DECIMAL ) AS geral                           ,
CAST(`Cultura e valores`               AS DECIMAL ) AS cultura_e_valores               ,
CAST(`Diversidade e inclusão`          AS DECIMAL ) AS diversidade_e_inclusao          ,
CAST(`Qualidade de vida`               AS DECIMAL ) AS qualidade_de_vida               ,
CAST(`Alta liderança`                  AS DECIMAL ) AS alta_lideranca                  ,
CAST(`Remuneração e benefícios`        AS DECIMAL ) AS remuneracao_e_beneficios        ,
CAST(`Oportunidades de carreira`       AS DECIMAL ) AS oportunidades_de_carreira       ,
CAST(`Recomendam para outras pessoas`  AS DECIMAL ) AS recomendam_para_outras_empresas ,
CAST(`Perspectiva positiva da empresa` AS DECIMAL ) AS perspectiva_postiva_da_empresa  ,
CAST(`Segmento`                        AS STRING  ) AS segmento                        ,
CAST(`Nome`                            AS STRING  ) AS nome                            ,
CAST(`match_percent`                   AS INTEGER ) AS match_percent                   

FROM schema.glassdoor_consolidado_join_match_v2