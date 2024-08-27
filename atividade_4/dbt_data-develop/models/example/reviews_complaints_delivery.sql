with
    trusted_banks as (select * from {{ ref("trusted_banks") }}),

    trusted_complaints as (select * from {{ ref("trusted_complaints") }}),

    trusted_employees as (select * from {{ ref("trusted_employees") }})

select *
from trusted_banks
