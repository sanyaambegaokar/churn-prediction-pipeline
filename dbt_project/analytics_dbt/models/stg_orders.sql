with source as (

    select * from public.raw_orders

),

renamed as (

    select
        invoice as invoice_id,
        stock_code,
        description,
        cast(quantity as integer) as quantity,
        invoice_date,
        cast(price as numeric) as price,
        customer_id,
        country
    from source

),

filtered as (

    select *
    from renamed
    where quantity > 0
      and customer_id is not null
      and price > 0

)

select * from filtered
