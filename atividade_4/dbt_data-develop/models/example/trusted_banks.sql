WITH raw_banks AS (
SELECT * fROM {{ref('raw_banks')}}
)

SELECT 

CAST(`Segmento` AS STRING)  AS segmento ,
CAST(`CNPJ`     AS INTEGER) AS cnpj     ,
CAST(`Nome`     AS STRING)  AS nome

FROM schema.EnquadramentoInicia_v2